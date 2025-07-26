import random
from car import Car

class UnreliableCar(Car):
    """A car that does not always drive reliably, depending on a reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar, with reliability (0-100)."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on its reliability.
        Returns the actual distance driven (0 if it fails).
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0