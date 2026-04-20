class Employee:
    
    company_name = "DXC"

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def info(self):
        return f"{self.name} works in {self.dept} at {self.company_name}"
    
# class DataEngineer(Employee):
#     print("Data Engineer class created")

class DataEngineer(Employee):

    def __init__(self, name, dept, skill):
        super().__init__(name, dept)  # call parent constructor
        self.skill = skill

    def show_skill(self):
        return f"My main skill is {self.skill}"

emp1 = DataEngineer("Geeth", "Data Engineering","Python")
print(emp1.info())
print(emp1.show_skill())


# MRO = Order Python searches for methods
#MRO — Method Resolution Order

print(DataEngineer.__mro__)