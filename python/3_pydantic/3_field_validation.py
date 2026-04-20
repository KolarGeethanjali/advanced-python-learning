from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict

class Person(BaseModel):
    name: str = Field(..., description="Name of the person")
    age: int = Field(..., gt=0, description="Age of the person")
    email: str = Field(..., description="Email address of the person")
    
# Field validation using field_validator decorator
#field validator for email field to check if it contains "@" symbol and .com domain
# Field validator runs before pydantic model checks the rules

    @field_validator('email')
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        elif ".com" not in value:
            return value + ".com"  # Automatically append .com if it's missing
        else:
            return value
        
pyd_ins = Person(**{"name":"geethanjali","age":25,"email":"geethanjali@example"}) # this will automatically append .com to the email address

def main(para:Person):
    print("name:", para.name)
    print("age:", para.age)
    print("email:", para.email)

main(pyd_ins)