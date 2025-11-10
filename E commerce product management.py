# Challenge: E commerce product management system
from datetime import datetime as dt
class Product:
# This is the base class
    def __init__(self, product_name, product_price):
        self.name = product_name
        self.price = product_price

    def display_info(self):
        #This method allows for users to view the product info
        print(f"Product name: {self.name} | Price: ${self.price}")


class Electronics(Product):
    #This a derived class from the product class, this handles just electronic products
    def __init__(self, product_name, product_price, warranty_period):
        super().__init__(product_name, product_price)
        self.warranty = warranty_period
    
    def apply_discount(self,discount):
        self.price -= (self.price * discount)/100
        return self.price
        

    def display_info(self):
        super().display_info()
        #print(f"Product name: {self.name} | Price: {self.price} | Warranty: {self.warranty}yrs")


class Clothing(Product):
    def __init__(self, product_name, product_price, size, color):
        super().__init__(product_name, product_price)
        self.size = size
        self.color = color

    def apply_discount(self,discount):
        #This function adds a discount and return the price after adding the discount.
        self.price -= (self.price * discount)/100
        print(f"After applying discount, your bill is ${self.price}")
        return self.price
    
    def display_info(self):
        super().display_info()
        #print(f"Product name: {self.name} | Price: {self.price} | Discount: {discount}")

class Grocery(Product):
    def __init__(self, product_name, product_price, expiry_date):
        super().__init__(product_name, product_price)  
        self.expiry = expiry_date

    def check_freshness(self):
        # This function checks if the product is expired or not by checking if the expiry date is greater than the current date(today())
        if self.expiry < dt.today().strftime("%m/%Y"):
            print(f"The product is expired")
        else:
            print("Your product is fresh")

    def display_info(self):
        super().display_info()
        #print(f"Product name: {self.name} | Price: {self.price} | Warranty: {self.warranty}yrs")




television = Electronics("Hisense Smart TV", 35000, 2)
television.apply_discount(10)
television.display_info()

apples = Grocery("Apples", 20, "07/2025")
apples.check_freshness()
apples.display_info()