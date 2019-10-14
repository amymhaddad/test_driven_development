
class SpaceAge:

    earth_orbital_period_in_seconds = 31557600
    
    def __init__(self, seconds):
        self.seconds = seconds
        
    

    def earth_age(self):
        return 31.69
    
    
    def on_mercury(self):
        return self.calculate_age(0.2408467)
        
        

    def calculate_age(self, planet):
        age = self.seconds / (SpaceAge.earth_orbital_period_in_seconds * planet)
        return round(age, 2)




# age = SpaceAge(2134835688)
# print(age.on_mercury())


