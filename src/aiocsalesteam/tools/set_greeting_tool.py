from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import asyncio
from py_near.account import Account
from py_near.providers import JsonProvider
import os

# Constants for NEAR setup
ACCOUNT_ID = "omar3.testnet"  # Replace with your contract's account ID
TESTNET_RPC_URL = "https://rpc.testnet.near.org"

async def set_greeting_on_contract(greeting: str):
    """Set a greeting in the NEAR contract using the `set_greeting` function."""
    # Initialize provider and account for testnet
    acc = Account(
        account_id=ACCOUNT_ID,
        private_key=os.getenv("PRIVATE_KEY"),  # Load private key from environment
        rpc_addr=TESTNET_RPC_URL
    )
    await acc.startup()

    # Call the contract's `set_greeting` function
    contract_id = ACCOUNT_ID
    method_name = "set_greeting"
    args = {"greeting": greeting}
    gas = 300_000_000_000_000  # Gas limit
    deposit = 0  # No deposit required for this method
    print(f"Account ID: {ACCOUNT_ID}")
    print(f"Contract ID: {contract_id}")
    print(f"Args: {args}")

    transaction = await acc.function_call(contract_id, method_name, args, gas, deposit)
    return transaction.transaction.url

class SetGreetingToolInput(BaseModel):
    """Input schema for SetGreetingTool."""
    greeting: str = Field(..., description="The greeting string to set in the contract.")

class SetGreetingTool(BaseTool):
    name: str = "Set Greeting Tool"
    description: str = (
        "Sets a new greeting in the NEAR smart contract. Use this tool to update the greeting message."
    )
    args_schema: Type[BaseModel] = SetGreetingToolInput

    def _run(self, greeting: str) -> str:
        try:
            # Invoke the asynchronous function
            transaction_url = asyncio.run(set_greeting_on_contract(greeting))
            result = f"Successfully set greeting to '{greeting}'. Transaction URL: {transaction_url}"
        except Exception as e:
            result = f"Failed to set greeting. Error: {str(e)}"
        return result
