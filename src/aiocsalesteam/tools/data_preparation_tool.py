from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from datasets import load_dataset
from transformers import AutoTokenizer

class DataPreparationToolInput(BaseModel):
    dataset_name: str = Field(..., description="Name of the dataset to load (e.g., 'imdb').")
    model_name: str = Field(..., description="Pretrained model name (e.g., 'bert-base-uncased').")
    max_length: int = Field(128, description="Maximum length of tokenized sequences.")

class DataPreparationTool(BaseTool):
    name: str = "Data Preparation Tool"
    description: str = "Loads and tokenizes a dataset for Hugging Face models."
    args_schema: Type[BaseModel] = DataPreparationToolInput

    def _run(self, dataset_name: str, model_name: str, max_length: int) -> dict:
        try:
            #override params
            {"dataset_name": "imdb", "model_name": "bert-base-uncased", "max_length": 128}
            # Load dataset
            dataset_name="imbd"
            dataset = load_dataset(dataset_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)

            # Tokenize the dataset
            def tokenize_fn(examples):
                return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=max_length)
            
            tokenized_dataset = dataset.map(tokenize_fn, batched=True)
            tokenized_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])

            return {"status": "success", "message": "Data prepared successfully.", "dataset": tokenized_dataset}
        except Exception as e:
            return {"status": "error", "message": str(e)}
