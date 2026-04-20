# Model_validator runs after passing the values and pydentic model has checked all the rules
# validates multiple fiels and also logic 

from pydantic import BaseModel, Field, model_validator
from typing import Optional, Dict


class API_auth(BaseModel):
    email : str = Field(..., description="Email address of the user")
    password : str = Field(..., description="Password of the user")
    confirm_password : str = Field(..., description="Confirm password of the user")


    @model_validator(mode="after")
    def validate_passwords(cls, values):
        
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values

pyd_ins = API_auth(**{"email":"geethanjali@example.com","password":"secret123","confirm_password":"secret123"})

def main(para:API_auth):
    print("email:", para.email)
    print("password:", para.password)
    print("confirm_password:", para.confirm_password)

main(pyd_ins)

