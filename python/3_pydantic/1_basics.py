#NEW LIBRARY
#data validation , data Quality , data parsing
#pydantic is a library for data validation and settings management using Python type annotations.
#data parsing means converting data from one format to another, such as from JSON to a Python object.
#Data parsing means converting raw data into a structured format that your program can understand and use.

#virtual environment
#python -m venv .venv
#activate it by .venv\Scripts\activate
# delete the virtual environment by rmdir /s .venv
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -->for powershell to allow running scripts in windows current user scope
# delete virtual environment by Remove-Item -Recurse -Force .venv short rm -r -fo .venv
# install pydantic by pip install pydantic

from pydantic import BaseModel, Field, StrictInt

#pydantic model step1
class geeth(BaseModel): # this is like a custom data type or a class that inherits from BaseModel
    x : StrictInt = Field(...,description="This is the x value")
    #y : str = Field(...,description="This is the y value")
    y : str = Field(default="default_value",description="This is the y value")

#pyd_input  = geeth(**{"x":10,"y":"geethanjali"}) # this is the way to create an instance of the geeth class using a dictionary, the ** operator is used to unpack the dictionary into keyword arguments.
#pyd_input  = geeth(x=10,y="geethanjali") 
#pyd_input = geeth(x=10)
pyd_input  = geeth(**{"x":10,})


# step 2 creating main function to print the values of x and y
def main(z:geeth):

    #print("x value is and y value is",z.x,z.y)
    print(f"x value is {z.x} and y value is {z.y}") # this is the way to use f-string to print the values of x and y


main(pyd_input)
