# # Create this structure:
# # Class Person
# # attribute: name
# # method: introduce() →
# # "Hi, I am {name}"

# # class Person:

# #     def __init__(self, name):
# #         self.name = name

# #     def introduce(self):
# #         print(f"Hi, I am {self.name}")

# class Person():

#     def __init__(self,name):
#         self.name = name

#     def introduce(self):
#         print(f"Hi, I am {self.name}")

# # Class Employee (inherits Person)
# # attribute: salary
# # override introduce()
# # It should:
# # Call parent introduce()
# # Then add: "I earn {salary}"

# # class Employee(Person):

# #     def __init__(self, name, salary):
# #         super().__init__(name)
# #         self.salary = salary

# #     def introduce(self):
# #         super().introduce()
# #         print(f"I earn {self.salary}")

# class Employee(Person):

#     def __init__(self,salary,name):
#         super().__init__(name)
#         self.salary = salary

#     def introduce(self):
#         super().introduce()
#         print(f"I earn {self.salary}")

# # Class DataEngineer (inherits Employee)
# # attribute: tech_stack
# # override introduce()
# # It should:
# # Use super()
# # Add: "I work on {tech_stack}"

# # class DataEngineer(Employee):

# #     def __init__(self, name, salary, tech_stack):
# #         super().__init__(name, salary)
# #         self.tech_stack = tech_stack

# #     def introduce(self):
# #         super().introduce()
# #         print(f"I work on {self.tech_stack}")

# class DataEngineer(Employee):

#     def __init__(self, name, salary, tech_stack):
#         super().__init__(salary,name)
#         self.tech_stack = tech_stack

#     def introduce(self):
#         super().introduce()
#         print(f"I work on {self.tech_stack}")    

# de = DataEngineer("Geeth", 90000, "PySpark")
# de.introduce()

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I am {self.name}")


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print(f"I earn {self.salary}")


class DataEngineer(Employee):

    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def introduce(self):
        super().introduce()
        print(f"I work on {self.tech_stack}")

de = DataEngineer("Geeth", 90000, "PySpark")
de.introduce()