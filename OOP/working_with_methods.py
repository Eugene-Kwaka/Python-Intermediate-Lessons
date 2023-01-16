class A:
    def a(self):
        return "Function inside A"
    
class B(A):
    def a(self):
        return "Function inside B"
    
class C(B,A):# Class C inherits from classes B and A. When I don't find any function a() inside class C, I should search for classes B and A and its important that I do it in that order.
    pass

c = C()
print(c.a())

################################### ANOTHER EXAMPLE #####################################
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(B, A):
    pass

class D(C):
    pass

d = D()
print(d.b()) 

# In this case, since there is no value in class C,  object instance d will inherit from class B which is class C's preceding superclass

###################### ANOTHER EXAMPLE ##############################
class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self):
        return "Function inside C"

class D(A, C): # -> Returns an error due to wrong Method Resolution Order as A is not the immediate superclass of D
    pass

d = D()
print(d.a)

