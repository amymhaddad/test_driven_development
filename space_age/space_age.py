class SpaceAge:

    earth_orbital_period_in_seconds = 31557600

    def __init__(self, seconds):
        self.seconds = seconds

    def earth_age(self):
        return self.calculate_age(1)

    def on_mercury(self):
        return self.calculate_age(0.2408467)

    def on_venus(self):
        return self.calculate_age(0.61519726)

    def on_mars(self):
        return self.calculate_age(1.8808158)

    def on_jupiter(self):
        return self.calculate_age(11.862615)

    def on_saturn(self):
        return self.calculate_age(29.447498)

    def on_uranus(self):
        return self.calculate_age(84.016846)

    def on_neptune(self):
        return self.calculate_age(164.79132)

    def calculate_age(self, planet):
        age = self.seconds / (SpaceAge.earth_orbital_period_in_seconds * planet)
        return round(age, 2)
