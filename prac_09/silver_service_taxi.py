from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        price = Taxi.price_per_km * fanciness
        super().__init__(name, fuel, price)
        self.fanciness = fanciness

    def get_fare(self):
        """Rewrite, return fare plus flagfall"""
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Add flagfall information based on the parent class string"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"