"""
simple oo example
"""


class Pet:
    def __init__(self, name):
        self.name = name
        self.hello = None

    def speak(self):
        """ sample - maybe lots of code in this """
        return self.hello


class Dog(Pet):
    def __init__(self, name, license_num):
        Pet.__init__(self, name)
        self.hello = "woof"

        # i can specialize and add to subclass
        self.license_num = license_num

    def speak(self):
        """ reuse or embelish code from superclass """
        return Pet.speak(self)


mypet = Pet("Goldie")
print(mypet.name)
print(mypet.speak())

mypet = Dog("Bogart", "AB56674")
print(mypet.name)

# i just tell it to speak
print(mypet.speak())

print(mypet.license_num)
