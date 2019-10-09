from taxi import Taxi


class SilverServiceTaxi(Taxi):

    price_per_km = Taxi.price_per_km

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    flagfall = 4.5

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        # round fare result to nearest 10c
        fare = super().get_fare() + self.flagfall
        return fare

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
