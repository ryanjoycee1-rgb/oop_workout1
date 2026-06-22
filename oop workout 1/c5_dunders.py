from c1_vehicle import Vehicle


def vehicle_str(self) -> str:
    return self.describe()


def vehicle_repr(self) -> str:
    return (f"{type(self).__name__}"f"('{self.plate}', '{self.make}', "f"'{self.model}', {self.year})")


def vehicle_eq(self, other) -> bool:
    if not isinstance(other, Vehicle):
        return False

    return self.plate == other.plate


def vehicle_hash(self) -> int:
    return hash(self.plate)


Vehicle.__str__ = vehicle_str
Vehicle.__repr__ = vehicle_repr
Vehicle.__eq__ = vehicle_eq
Vehicle.__hash__ = vehicle_hash