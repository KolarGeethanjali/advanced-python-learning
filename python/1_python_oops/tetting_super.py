class A:
    def show(self):
        print("this is from A")

class B(A):
    def show(self):
        print("this is from B")
        #A.show(self)   # explicit call
        super().show()  # this is implicit call to parent method

class C(A):
    def show(self):
        print("this is from C")
        #A.show(self)   # explicit call
        super().show()  # this is implicit call to parent method

class D(B, C):
    pass

d = D()
# MRO calls the next method in the class’s MRO (Method Resolution Order).
print(D.__mro__)  # this is method resolution order 
d.show()