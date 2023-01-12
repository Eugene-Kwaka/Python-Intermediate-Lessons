class SoftwareEngineer:
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        
    # DUNDER METHODS
    # The string method will ensure that the object instance is returned as a string when instantiated
    def __str__(self) -> str:
        return f"name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}"

    # the __eq__ method ensures that the object instances (self, other) created are equal.
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age

# initiate an object instance
se1 = SoftwareEngineer("Eugene", 25, "Mid-level", 500000)
se2 = SoftwareEngineer("Halle", 20, "Junior", 250000)
print(se1)
print(se1.name)
print(se1 == se2) # -> Returns False as the ages and names are not the same