from typing import Literal

from pydantic import BaseModel


SUBSTRUCT_FROM = Literal[
    "balance",
    "amount"
]

class PayoffCreate(BaseModel):
    """Ответ метода payoff/create
    """
    id: str
    subtract_from: str
    method: str
    amount_currency: str
    amount: str
    rub_amount: str
    receive_amount: str
    deduction_amount: str
    commission_amount: str
    wallet: str
