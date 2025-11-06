#Challenge: Smart Vehicle system
# Designing a system that models different types of vehicles with multiple abilities like driving, flying, floating. 
# Using multiple inheritance


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped")

    
class Flyable:
    def move(self):
        print("Flying in the sky....")

class Floatable:
    def move(self):
        print("Floating on water...")

class Drivable:
    def move(self):
        print("Driving on the road.....")



class AmphibiousCar(Vehicle, Drivable, Floatable):
    pass
    



class FlyingCar(Vehicle, Flyable, Drivable):
    pass


amphi = AmphibiousCar("Gibbs", "Aquada")


amphi.start_engine()
amphi.move()
amphi.stop_engine()



flycar = FlyingCar("Terrafugia", "Transition")

flycar.start_engine()
flycar.move()
flycar.stop_engine()

