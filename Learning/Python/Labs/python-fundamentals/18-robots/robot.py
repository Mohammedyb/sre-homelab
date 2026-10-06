# Exercise: Robot Base Class
#
# Define the shared robot behavior used by the robot examples.
#
# Concepts:
# - Classes
# - Methods
# - Attributes
# - Inheritance

# Base robot class with shared movement and eating behavior.
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        print("My name is", self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New position:", self.position)

    def eat(self):
        print("I'm Hungry!")