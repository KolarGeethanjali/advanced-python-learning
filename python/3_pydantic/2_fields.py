# requirements.txt file that lists all Python packages required for a project.
# then you can install all the packages listed in the requirements.txt file using pip install -r requirements.txt command.
# pip freeze > requirements.txt --> pip freeze Lists all installed packages in current environment.
# The > symbol means:Redirect output into a file.
# We must run this inside your virtual environment.

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any, Literal

class Personal_info(BaseModel):
    name : str = Field(..., min_length=3, max_length=20, description="Name of the person")
    age : int | None = Field(..., gt=0, description="Age of the person")
    email : EmailStr = Field(..., description="Email address of the person")
    genger : Literal["male", "female", "other"] = Field(..., description="Gender of the person")
    salaries : List[int] = Field(...,description="List of salaries for the person")
    additional_info : Optional[Dict[str, Any]] = Field(None, description="Additional information about the person")

pyd_ins = Personal_info(**{"name":"geethanjali","age":25,"email":"geethanjali@example.com","genger":"female","salaries":[10000,200000,30000],"additional_info":{"department":"IT"}})

def main(para:Personal_info):
    #print(f"Name: {Personal_info.name}")
    print("name:", para.name)
    print("age:", para.age)
    print("email:", para.email)
    print("gender:", para.genger)
    print("salaries:", para.salaries)
    print("additional_info:", para.additional_info)

main(pyd_ins)
    
