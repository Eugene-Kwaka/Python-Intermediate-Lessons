class Recipe():
    # new method is responsible for creating and returning a new empty object
    # def __new__(cls: type[Self]) -> Self:
    #     pass
    
    # Used to specify the attributes for the object instances for the class.
    def __init__(self, dish:str, items:str, time:int) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    # I create a method to display all recipe for a restaurant 
    def contents(self):
        return f"The {self.dish} has {self.items} and takes {self.time} mins to prepare"
        
pizza = Recipe("Pizza", ["cheese", "pepperoni", "bread", "tomato"], 30)
print(pizza.contents())