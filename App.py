class Customer :

    def __init__(self , Name , Email , Address):

        self.Name = Name
        self.Email = Email
        self.Address = Address
    
    def __str__(self):
        return f"Name: {self.Name} \nEmail: {self.Email} \nAddress:{self.Address}"
                
class Pizza :

    def __init__(self , size , price , number_of_pizza):
        self.size = size
        self.price = price
        self.number_of_pizza = number_of_pizza       
       
    def total(self):
        total_price = self.price * self.number_of_pizza
        if self.number_of_pizza >= 3:
            total_price -= total_price * 0.15  
        return total_price

    def __str__(self):
        return f"Size: {self.size} \nPrice: ${self.price} \nQuantity: {self.number_of_pizza} \nTotal Price: {self.total()} "
    