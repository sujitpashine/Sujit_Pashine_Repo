class dog:
    def __init__(self, name):
        self.name = name
        print("Object with name: {} created".format(name))
    
    def talk(self):
        print("Woof!")

    def printname(self):
        print("My name is: {}".format(self.name))

Dog = dog("charlie")

Dog.talk()
Dog.printname()

import pyodbc
