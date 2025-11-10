class Vehicle:
    def __init__(self, brand, model, capacity):
        self.brand = brand #brand of the vehicle
        self.model = model #model of the vehicle
        self.capacity = capacity #number of passengers



class Electric(Vehicle): #Electric vehicle class
    def __init__(self, brand, model, capacity, battery_capacity):
        Vehicle.__init__(self, brand, model, capacity)
        self.battery_capacity = battery_capacity #battery capacity in kWh

    
    def charge(self):       #Method to charge the electric vehicle
        print(f"{self.brand} {self.model} is plugged in and charging. Est time to full charge: 2hrs")

class Fuel(Vehicle): #Fuel-based vehicle class
    def __init__(self, brand, model, capacity, fuel_type):
        Vehicle.__init__(self, brand, model, capacity)
        self.fuel_type = fuel_type

    def refuel(self): #Method to refuel the vehicle
        print(f"Your car is being refueled. Est time to full tank: 7mins")

class HybridVehicle(Electric, Fuel):#Hybrid vehicle class inheriting from both Electric and Fuel classes
    def __init__(self, brand, model, capacity, battery_capacity, fuel_type):
        Electric.__init__(self, brand, model, capacity, battery_capacity)
        Fuel.__init__(self, brand, model, capacity,fuel_type)

    def switch_mode(self,mode): #Switches between electric and fuel mode
        if mode.lower() == "electric": 
            print(f"Mode switch to Electric, You can now charge the battery and use")
        elif mode.lower() == "fuel":
            print(f"Mode switch to Fuel, You'll need petrol to use the car")
        else:
            print("Invalid mode choosen")

car = HybridVehicle("Toyota", "Prius", 4, 8.8, "Petrol")
car.charge()
car.switch_mode('electric')