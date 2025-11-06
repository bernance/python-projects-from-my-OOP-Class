class Vehicle:
    def __init__(self, brand, model, max_speed, mileage):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}| Model: {self.model} | Max speed: {self.max_speed} | Mileage: {self.mileage}")

    def fare(self):
        return self.mileage * 0.5
    


class Car(Vehicle):
    def __init__(self, brand, model, max_speed, mileage, num_doors):
        super().__init__(brand, model, max_speed, mileage)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}| Model: {self.model} | Max speed: {self.max_speed} | Mileage: {self.mileage} | Number of doors: {self.num_doors} | Fare: {self.fare()}")

    def fare(self):
        return super().fare()
    

class Bus(Vehicle):
    def __init__(self, brand, model, max_speed, mileage):
        super().__init__(brand, model, max_speed, mileage)

    def fare(self):
        return ((self.mileage * 0.5 *10)/100) + (self.mileage * 0.5)
    
    def display_info(self):
        total_fare = self.fare()
        print(f"Vehicle Brand: {self.brand}| Model: {self.model} | Speed: {self.max_speed} | Mileage: {self.mileage} | Total fare(after maintenance): {total_fare}")




car = Car("Toyota", "Corolla", 180, 15000, 4)
bus = Bus("Volvo", "Intercity", 120, 40000)



car.display_info()
bus.display_info()
