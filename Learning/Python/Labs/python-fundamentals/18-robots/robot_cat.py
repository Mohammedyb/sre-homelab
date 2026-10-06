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


class Robot_Cat(Robot):
    def make_noise(self):
        print("Meow, Meow!")

    def eat(self):
        super().eat()
        print("I like Milk!")


# Instantiate a cat robot and demonstrate the inherited and overridden actions.
my_robot_cat = Robot_Cat("Sylvester")
my_robot_cat.walk(10)
my_robot_cat.make_noise()
my_robot_cat.eat()