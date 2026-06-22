class Vehicle:
    def __init__(self, plate, make, model, year) -> None:
        self.plate = plate
        self.make = make
        self.model = model
        self.year = year
        self.kilometres = 0

    def drive(self, km: int) -> None:
        if km > 0:
            self.kilometres += km
        else:
            raise ValueError("Enter a positive number!!")

        

    def describe(self):
        return f"<{self.year}> <{self.make}> <{self.model}> <{self.plate}>)"
    
v= Vehicle("B-AB-1234", "Volkswagen", "Golf", 2022)
v.drive(50)
print(v.describe())
print(v.kilometres)
