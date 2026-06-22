class FuelTank:
    def __init__(self, capacity: float) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.__capacity = capacity
        self.__level = 0.0

    def get_level(self) -> float:
        return round(self.__level, 2)

    def get_capacity(self) -> float:
        return self.__capacity

    def fill(self, litres: float) -> None:
        if litres <= 0:
            raise ValueError("should be positive!!!")
        if self.__level + litres > self.__capacity:
            raise ValueError("exceeded capacity")

        self.__level += litres

    def consume(self, litres: float) -> None:
        if litres <= 0:
            raise ValueError("should be positive!!")
        if litres > self.__level:
            raise ValueError("low fuel")

        self.__level -= litres


t = FuelTank(25.0)
t.fill(-4)
print(t.get_level())