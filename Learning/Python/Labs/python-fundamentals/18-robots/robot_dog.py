# Exercise: Robots
#
# Create subclasses of a base robot class and show inherited behavior.
#
# Concepts:
# - Classes
# - Inheritance
# - Methods
# - Method overriding
# - Object behavior

from robot import Robot


class Robot_Dog(Robot):
    def make_noise(self):
        print("Woof Woof!")

    def eat(self):
        super().eat()
        print("I like Bones!")


# Instantiate a dog robot and demonstrate the inherited and overridden actions.
my_robot_dog = Robot_Dog("Spot")
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()