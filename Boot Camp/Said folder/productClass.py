""" Create product class eac product has name , category, and price --> instance vaiable 
class is able to return a discribtion of product --> method
for each product be abke ti compute discount of  given mount (compute price after dscount of amount%)
"""

class Product :
    #Constructor
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
    def discribtion(self): 
        return f''' The name of teh product is {self.name}
        category of the procuct is {self.category}
        price of the product is is {self.price}'''

    def discount(self, discount):
        self.price = self.price - (self.price * (discount/100))
        if self.category == "Electronic":
            self.price +=  10 
    # creat getter and setter        
    
    def get_price(self):
        return self.price
    def get_name(self):
        return self.name
    def get_category(self):
        return self.category
    
    def set_price(self, newp):
        self.price = newp
    def set_name(self, newn):
        self.name = newn
    def set_category(self, newcat):
        self.category = newcat
    
        
        
        
        
        