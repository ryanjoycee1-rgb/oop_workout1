from c1_vehicle import Vehicle


class ElectricCar(Vehicle):
    def __init__(self, plate, make, model, year, battery_kwh, range_km) -> None:
        super().__init__(plate, make, model, year)

        self.battery_kwh = battery_kwh
        self.range_km = range_km
        self.__charge = 0.0

    def get_charge(self) -> float:
        return round(self.__charge, 2)

    def charge(self, kwh: float) -> None:
        if kwh <= 0:
            raise ValueError("shouyld be positive!!!")

        if self.__charge + kwh > self.battery_kwh:
            raise ValueError("battery capacity exceeded.")

        self.__charge += kwh

    def drive(self, km: int) -> float:   #power required for the trip
        if km <= 0:
            raise ValueError("should be positive!!!")

        kwh_used = (self.battery_kwh * km) / self.range_km

        if kwh_used > self.__charge:
            raise ValueError("Insufficient charge.")

        self.__charge -= kwh_used
        super().drive(km)

        return kwh_used

    def describe(self):
        return f"{super().describe()}, electric car"