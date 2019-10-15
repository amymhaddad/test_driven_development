import random
from string import ascii_uppercase as upper
from string import digits as digit

class Robot():

    # def __init__(self):
    #     self.name = create_random_name()
    
    def create_random_name(self):
        return "".join(random.sample(upper, 2) + random.sample(digit, 3))



r = Robot()

print(r.create_random_name())