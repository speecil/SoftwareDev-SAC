# imports
import numpy as np

# Declare Class
class Questions:
    # Initialise class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass
    
    # function to generate questions for any user given
    def generateQuestions(self):
        # age check
        if int(self.age) < 9:
            # generate random int array
            randnums = np.random.randint(1, 6, 10)
            return randnums
        # age check
        elif int(self.age) > 8:
            # generate random int array
            randnums = np.random.randint(1, 12, 10)
            return randnums
