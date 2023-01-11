class ParentClass:
    def __init__(self):
        print("Parent class instance")
        
    def parent_method(self):
        print("Parents money")
        
        
# Since the Child class is inheriting from the Parent Class, the Parent class will be passed as an argument in the Child class
class Child(ParentClass):
    pass

# Create an instance of the child class
child = Child()
# Pass a method from the Parent to the Child class
child.parent_method()


##### ANOTHER EXAMPLE ########
class RateOfInterest:
    interest = 0.09
    def __init__(self, name:str, loan:float):
        assert loan >= 0
        self.name = name
        self.loan = loan
        
    def calculate_interest(self):
        total_interest = self.loan * self.interest
        return f"Total interest is: {total_interest}"
    
# Create a Child class
class StudentInterest(RateOfInterest):
    # Specify that a student gets a 
    interest = 0.05
    
# Child instance
student = StudentInterest("Eugene", 100000)
print(student.calculate_interest())
    
    
#################################################### MULTIPLE INHERITANCE #############################################
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

##### Multiple-Level Inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

#################################################### SUPER() Function ####################################################
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        # From the Fruit's class fruit attribute, here it is specified to be Apple
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()
