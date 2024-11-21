from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import asyncio
from py_near.account import Account
from py_near.dapps.core import NEAR
from py_near.providers import JsonProvider


ACCOUNT_ID = "omar3.testnet"
PRIVATE_KEY = "ed25519:R8VPRGkS127sqW15BGEUrPC8GLc6Z7LDwa6p8yuwaKVLBJbjmf1oKZYkmNcBWoak7VuQfWrNW2H251DKf7ppLji"
# Testnet RPC URL
TESTNET_RPC_URL = "https://rpc.testnet.near.org"


async def send_tip():
    # Initialize provider and account for testnet
    provider = JsonProvider(TESTNET_RPC_URL) 
    acc =  Account(
    account_id=ACCOUNT_ID,
    private_key=PRIVATE_KEY,
    rpc_addr=TESTNET_RPC_URL) 
    await acc.startup()
    # Amount in yoctoNEAR
    yocto_near_amount = 1 * 10**23
    tr = await acc.send_money("omars.testnet", yocto_near_amount)
    print(tr.transaction.url)

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
   
    argument: str = Field(..., description="Mandatory string representing a number you would like to tip to the other person.")

class MyCustomTool(BaseTool): 
   
    name: str = "Tipping tool"
    description: str = (
        "Useful to send tips. The input to this tools should be a string representing a number above 0"
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        try:
            asyncio.run(send_tip())
            result = "You rewarded with a tip successfuly !"
        except Exception as e:
            result="Something went wrong, the tip wasn't sent. Here are the details :" + str(e)
        return result
    
