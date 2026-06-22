from c1_vehicle import Vehicle
from c2_tank import FuelTank


class FuelledVehicle(Vehicle):
    def __init__(self,plate,make,model,year,capacity,consumption,) -> None:
        super().__init__(plate, make, model, year)
        self.tank = FuelTank(capacity)
        self.consumption = consumption  # litres per hundred km

    def refuel(self, litres: float) -> None:
        self.tank.fill(litres)

    def drive(self, km: int) -> float:
        litres_required = (self.consumption * km) / 100

        self.tank.consume(litres_required)  #raises Value error if not enough fuel
        super().drive(km)

        return litres_required


class Car(FuelledVehicle):
    def __init__(self,plate, make, model, year, seats, int = 5) -> None:
        super().__init__(plate, make, model, year, capacity=50.0, consumption=6.0)
        self.seats = seats

    def describe(self):
        return f"{super().describe()}, car, {self.seats} seats"


class Truck(FuelledVehicle):
    def __init__(self, plate, make, model,year, payload_kg) -> None:
        super().__init__(plate, make, model, year, capacity=200.0, consumption=18.0)
        self.payload_kg = payload_kg

    def describe(self):
        return f"{super().describe()}, truck, {self.payload_kg} kg payload"


class Motorcycle(FuelledVehicle):
    def __init__(self, plate, make, model, year ) -> None:
        super().__init__(plate, make, model, year, capacity=15.0, consumption=3.5)

    def describe(self):
        return f"{super().describe()}, motorcycle"