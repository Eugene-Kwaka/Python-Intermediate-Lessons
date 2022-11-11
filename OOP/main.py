class Item:
    # create a method
    # Python passes the object(item1, item2 as the first argument in the class methods. Also other attributes the objects have that will be taken care of by the method)
    # To avoid hard coding the object instance's attributes, we use the __init__ method (Constructor method)
    def __init__(self, name, price, quantity=0):
        """Incase I am not sure of the exact number of values an object's attribute has, I can write the default as 0.
            e.g def __init__(self, name, price=0, quantity=0):
                item1 = Item("Phone", 100)      
        """
        # dynamically assign attributes to an instance using the constructor method
        self.name = name
        self.price = price
        self.quantity = quantity
        
    # Create a method
    # The method does not have parameters because the attributes have been assigned to the instance(self) once it was created 
    def calculate_total_price(self):
        return self.price * self.quantity

# Creating an instance(object item1) of the class Item with the corresponding attributes
item1 = Item("Phone", 100, 5)
# print(item1.name, item1.price, item1.quantity)
# print(f"The total price all the phones is: ", item1.calculate_total_price())

# Creating an instance object(item2) of the class Item with the corresponding attributes
item2 = Item("Laptop", 1000, 10, )






###################################### VALIDATING DATATYPES OF VALUES PASSED IN THE CLASS METHODS #############################################
# I can use typings in the parameters passed in the methods to ensure that the datatypes are specific i.e name=string, price=float, quantity=int

class Item:
    # Used datatyping to ensure that the attributes are of a certain datatype
    def __init__(self, name: str, price: float, quantity: int):
        # To run validations using "Assert statement" such that the price and quantity are not less than 0.
        # The two attributes will not accept negative numbers
        assert price >= 0
        assert quantity >= 0
        
        # dynamically assign attributes to an instance using the constructor method
        self.name = name
        self.price = price
        self.quantity = quantity
        
    # Create a method
    # The method does not have parameters because the attributes have been assigned to the instance(self) once it was created 
    def calculate_total_price(self):
        return self.price * self.quantity

# Creating an instance(object item1) of the class Item with the corresponding attributes
item1 = Item("Phone", 100, 5)
# item1 runs the method with the object's attributes as the arguments
# print(item1.calculate_total_price(item1.price, item1.quantity))
# print(item1.name, item1.price, item1.quantity)
# print(f"The total price all the phones is: ", item1.calculate_total_price())


# Creating an instance object(item2) of the class Item with the corresponding attributes
item2 = Item("Laptop", 1000, 10, )






############################################ USING A CLASS ATTRIBUTE #######################################################
# A class attribute is a class that is shared between all instances of a class. In this case, I apply a "discount"
class Item:
    pay_rate = 0.8 # Pay rate after  20% discount
    
    def __init__(self, name: str, price: float, quantity: int):
        assert price >= 0
        assert quantity >= 0
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        # We have to overwrite the price attribute to include the pay_rate attribute.
        # "Item.pay_rate" because the pay_rate variable is global.
        # This will be accessed by both item1 and item2
        self.price = self.price * Item.pay_rate
        return self.price
    
    def specific_item_discount(self):
        # Since I want to apply a specific discount rate to item2(Laptop), 
        # I will use "self.pay_rate" and while instantiating the item instance I will specify the pay_rate.
        # This method can still be applied on item1(phone) since we are using the class attribute "pay_rate".
        self.price = self.price * self.pay_rate
        return self.price
        

# Creating an instance(object item1) of the class Item with the corresponding attributes
item1 = Item("Phone", 100, 5)
item1.pay_rate = 0.5
# print(item1.apply_discount()) # -> 80
# print(item1.specific_item_discount()) # -> 50

item2 = Item("Laptop", 1000, 10, )
# specify the pay_rate for item2
item2.pay_rate = 0.7
print(item2.specific_item_discount()) # -> 700

# Accessing class variable from class level
# print(Item.pay_rate)
# Accessing class variable from instance level
# print(item1.pay_rate)

# To check for the attributes that are accessible to a class or a particular instance. In our case for example:
# print(Item.__dict__) # will display all attributes accessible by the class Item
# print(item1.__dict__) # will display all attributes accessible by the item1 instance