from pydantic import BaseModel, Field, computed_field
from typing import Optional, Dict

class orders(BaseModel):
    id : int = Field(..., description="Order ID")
    units : int = Field(..., gt=0, description="Number of units ordered")
    amount : int = Field(..., gt=0, description="Total amount for the order")

    @computed_field
    @property
    def total_amount(self) -> int:
        return self.units * self.amount
    
pyd_ins = orders(**{"id":1,"units":10,"amount":100})

def main(para:orders):
    print("id:", para.id)
    print("units:", para.units)
    print("amount:", para.amount)
    print("total_amount:", para.total_amount)

main(pyd_ins)