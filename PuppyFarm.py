"""
***************************************
*             Puppy Farm              *
*  Created by: Tommy H. Yeargin, Jr.  *
*           August 23, 2022           *
***************************************
"""

class Puppy:
    def __init__(self, name, breed, color, disposition):
        self.name           = name
        self.breed          = breed
        self.color          = color
        self.disposition    = disposition

    def meetYourPuppy(self):
        print("This is {}, a {} {} with a {} disposition.".format(self.name, self.color.lower(), self.breed, self.disposition.lower()))

Willie = Puppy("Willie", "Beagle", "Brown and White", "Happy")

Willie.meetYourPuppy()

# Output:
# This is Willie, a brown and white Beagle with a happy disposition.