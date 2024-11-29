from crewai.tools import BaseTool
from typing import Type, Any
from pydantic import BaseModel, Field
import flwr as fl
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset

class FederatedTrainingToolInput(BaseModel):
    model_name: str = Field(..., description="Pretrained model name (e.g., 'bert-base-uncased').")
    num_rounds: int = Field(3, description="Number of federated learning rounds.")
    local_epochs: int = Field(1, description="Number of local training epochs.")

class FederatedTrainingTool(BaseTool):
    name: str = "Federated Training Tool"
    description: str = "Conducts federated training using Flower and Hugging Face models."
    args_schema: Type[BaseModel] = FederatedTrainingToolInput

    def _run(self, model_name: str, num_rounds: Any, local_epochs: int) -> str:
        try:
            # Define Flower client
            class HuggingFaceClient(fl.client.NumPyClient):
                def __init__(self, model, tokenizer, train_dataset):
                    self.model = model
                    self.tokenizer = tokenizer
                    self.train_dataset = train_dataset
                
                def get_parameters(self):
                    return [val.cpu().numpy() for _, val in self.model.state_dict().items()]

                def set_parameters(self, parameters):
                    params_dict = zip(self.model.state_dict().keys(), parameters)
                    for name, param in params_dict:
                        self.model.state_dict()[name].copy_(torch.tensor(param))

                def fit(self, parameters, config):
                    self.set_parameters(parameters)
                    training_args = TrainingArguments(
                        output_dir="./results",
                        num_train_epochs=local_epochs,
                        per_device_train_batch_size=8,
                        save_strategy="no",
                    )
                    trainer = Trainer(
                        model=self.model,
                        args=training_args,
                        train_dataset=self.train_dataset,
                    )
                    trainer.train()
                    return self.get_parameters(), len(self.train_dataset), {}

                def evaluate(self, parameters, config):
                    self.set_parameters(parameters)
                    return 0.0, len(self.train_dataset), {}

            # Load model and tokenizer
            model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
            tokenizer = AutoTokenizer.from_pretrained(model_name)

            # Create dummy dataset for simulation
            dummy_data = {
                "text": ["dummy text"] * 100,
                "label": [0] * 100
            }
            tokenized_dataset = Dataset.from_dict(dummy_data).map(
                lambda x: tokenizer(x["text"], truncation=True, padding=True),
                batched=True
            )

            def client_fn(cid: str) -> fl.client.Client:
                return HuggingFaceClient(model, tokenizer, tokenized_dataset)

            fl.simulation.start_simulation(
                client_fn=client_fn,
                num_clients=10,
                num_rounds="2",
            )
            return "Federated training completed successfully."
        except Exception as e:
            return f"Federated training failed. Error: {str(e)}"
