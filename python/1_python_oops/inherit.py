#Inheritence
#single level , Multi level, Multiple level

# this is single level inheretence
# class company():

#     def company_name(self):
#         print("Company name is DXC")

# class employee(company): #single level Inheritence

#     def emp_info(self):
#         print("Employee name is geeth")

# emp1 = employee()

# emp1.emp_info()
# emp1.company_name()  #without calling company class we are calling method in company class this is interitence

#This below is multiple inheretence below example 2 parents and 1 child
# class company():

#     def __init__(self,comp_name):
#         self.comp_name = comp_name
        
#     def company_info(self):
#         print(f"Company name is {self.comp_name}")

# class country():

#     def __init__(self,country_name):
#         self.country_name = country_name

#     def country_info(self):
#         print(f"this is my country{self.country_name}")

# class employee(company,country):

#     def __init__(self, emp_name,comp_name,country_name):
#         self.emp_name = emp_name
#         #self.comp_name = comp_name # call parent attribute
#         company.__init__(self,comp_name) # getting company name from employee init # this is efficient method to call parent attribute
#         country.__init__(self,country_name)

#     def emp_info(self):
#         print(f"Employee name is {self.emp_name}")

#     def full_info(self):
#         print(f"Employee name is {self.emp_name} and company name is {self.comp_name} and country name is {self.country_name}")

#     def company_info(self):  #overriding or calling the method of parent 
#         print("this is running from employee")
#         company.company_info(self)
#         #country.country_info(self)
#         #super().company.info()

# emp1 = employee("Geeth","dxc","India")

# #emp1.company_info()
# emp1.full_info() 

#print(employee.__mro__)

# multi level inheritence
class company():

    def __init__(self,comp_name):
        self.comp_name = comp_name
        
    def company_info(self):
        print(f"Company name is {self.comp_name}")


class department(company):

    def __init__(self, dept_name, comp_name):
        self.dept_name = dept_name
        company.__init__(self,comp_name)

    def dept_info(self):
        print(f"Im from {self.dept_name} and company {self.comp_name} ")

class employee(department):

    def __init__(self, emp_name, dept_name, comp_name):
        self.emp_name = emp_name
        department.__init__(self,dept_name,comp_name)

    def all_info(self):
        department.dept_info(self)
        print(f"Employee name is {self.emp_name} and department is {self.dept_name} and company is {self.comp_name}")


e1 = employee("Geeth","development","DXC")

e1.all_info()