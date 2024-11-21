from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import asyncio
from py_near.account import Account
from py_near.dapps.core import NEAR
from py_near.providers import JsonProvider
import os

ACCOUNT_ID = "omar3.testnet"

# Testnet RPC URL
TESTNET_RPC_URL = "https://rpc.testnet.near.org"


async def send_tip(tip_amount:int):
    # Initialize provider and account for testnet
    provider = JsonProvider(TESTNET_RPC_URL) 
    acc =  Account(
    account_id=ACCOUNT_ID,
    private_key=os.getenv("PRIVATE_KEY"),
    rpc_addr=TESTNET_RPC_URL) 
    await acc.startup()
    # Amount in yoctoNEAR
    yocto_near_amount = tip_amount * 10**22
    tr = await acc.send_money("omars.testnet", yocto_near_amount)
    print(tr.transaction.url)

class TipSenderToolInput(BaseModel):
    """Input schema for TipSenderTool."""
   
    argument: int = Field(..., description="Mandatory integer representing a number you would like to tip to the other person.")

class TipSenderTool(BaseTool): 
   
    name: str = "Tipping tool"
    description: str = (
        "Useful to send tips. The input to this tools should be a integer representing a number above 0"
    )
    args_schema: Type[BaseModel] = TipSenderToolInput

    def _run(self, argument: int) -> str:
        try:
            asyncio.run(send_tip(argument))
            result = "You rewarded with a tip successfuly !"
        except Exception as e:
            result="Something went wrong, the tip wasn't sent. Here are the details :" + str(e)
        return result
    
