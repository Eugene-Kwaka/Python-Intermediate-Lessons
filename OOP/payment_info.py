class Payslips:
    def __init__(self, name, payment, amount):
        assert amount >= 0
        self.name = name
        self.payment = payment
        self.amount = amount
    
    # When this method is invoked, the paystatus becomes true
    def paystatus(self):
        self.payment = "yes"
        
    # method to check if the staff has been paid or not   
    def pay(self):
        if self.payment =="yes":
            return f"{self.name} has been paid {self.amount}"
        else:
            return f"{self.name} has not been paid"
        
Nathan = Payslips("Nathan", "yes", 10000)
Roger = Payslips("Roger", "no", 50000)

# calling the paystatus() method first changes the value of payment to True.
# This only affects the instance that has called the method
print(Roger.paystatus())
print(Roger.pay()) # -> Hence the pay() method returns that Roger has been paid 50000
