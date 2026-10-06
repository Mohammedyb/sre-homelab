# Exercise: Robot Dog
#
# Create a simple robot dog class and demonstrate its behavior.
#
# Concepts:
# - Classes
# - Objects
# - Attributes
# - Methods
# - Instance creation

class Robot_Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Bark,Bark!")

# Create an instance of the robot dog and display its attributes.
def main():
    my_dog = Robot_Dog("Sherrif", "Labrador")
    print(my_dog.name)
    print(my_dog.breed)
    my_dog.bark()

main()