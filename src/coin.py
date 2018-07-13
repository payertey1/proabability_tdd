import random

class Coin:
    
    def __init__(self):
        self.states=['H','T']

        
    def flip (self):
        return self.states[random.randint(0,1)]



