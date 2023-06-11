class Vehicle:
    pass


class WaterVehicle(Vehicle):
    pass


class Boat(WaterVehicle):
    pass


class LandVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


class CarBoat(Car, Boat):
    pass
