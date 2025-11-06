class Product:
    def __init__(self, name, price):
        self.p_name = name
        self.price = price

    def display_info(self):
        print(f"{self.p_name} | ${float(self.price)}")

    def get_price(self):
        return(self.price)
    

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percentage):
        super().__init__(name, price)
        self.discount = discount_percentage

    def get_price(self):
        new_price =  self.price - ((self.price * self.discount)/100)
        return new_price
    
    def display_info(self):
        discounted_price = self.get_price()
        print(f"{self.p_name} | Original price ${self.price}| Discounted price ${float(discounted_price)}")


product1 = Product("Headphones", 150)
product2 = DiscountedProduct("Smartwatch", 300, 10)


product1.display_info()
product2.display_info()