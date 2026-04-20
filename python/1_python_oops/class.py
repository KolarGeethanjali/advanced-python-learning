class employee:

    company_name = 'DXC'

# calss method is used to interact with class attributes

    @classmethod
    def changeInClass(cls, new_company): 
        cls.company_name = new_company

#instance methods changes wrt object

    def update(self,new_company): # method to update class attribute but not the efficient method
        employee.company_name = new_company

#constructer for instance attributes
    def __init__(self,emp_name,emp_dept):
        
        self.emp_name = emp_name
        self.emp_dept = emp_dept


# instance method changes wrt object (acts as a getter as per just concept without getter decorator)
    # def info(self):
    #     print(f"Im {self.emp_name} belongs to {self.emp_dept} in company {self.company_name} ")

# now we want to use the above methos with actually getter decorative
    
    @property #getter (now this function is treated as attribute)
    def info(self):
        print(f"Im {self.emp_name} belongs to {self.emp_dept} in company {self.company_name} ")


# acts a setter as per just concept without setter decorator

    # def change_info(self,new_emp_name,new_emp_dept):
    #     self.emp_name = new_emp_name
    #     self.emp_dept = new_emp_dept

# actual setter 

    @info.setter #should have same name as getter method
    def info(self, newdetails): #should have same name as getter method

        new_emp_name = newdetails[0]
        new_emp_dept = newdetails[1]

        self.emp_name = new_emp_name
        self.emp_dept = new_emp_dept

# static method
    
    @staticmethod   # otherwise when we call object it actually take 3 aruments including object but we dont want that so we use static method
    def addition(x,y):
        return x+y

#if __name__ == "__main__":

emp1 = employee("Geeth", "DE")
emp2 = employee("Suresh", "QA")
#print(emp1.emp_name)
#emp1.info()  # employee.info(emp1)  # this is how it works internally
#emp2.info()

#employee.company_name = 'Google' # not rightway to change like this it should inside class
# emp1.update("Google")
#emp2.company_name = 'Google' # not rightway to change like this it should inside class

# emp1.info()
# emp2.info()

#emp1.addition(1,2)

#print(emp2.info)

emp2.info = ['geetesh','MS'] #setter

print(emp2.info) #Getter

# Instance attributes → belong to each object separately
# Class attributes → shared by all objects
# Getter & Setter → used to read and update instance attributes in a controlled way
# Class Methods → used to access or update class attributes (primarily for class-level data)
# Instance methods → perform operations using instance data 
# Constructor initializes instance (object) attributes for each object created from the class.


