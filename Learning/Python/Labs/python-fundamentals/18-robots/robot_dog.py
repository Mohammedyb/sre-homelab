from robot import Robot

class Robot_Dog(Robot):
    def make_noise(self):
        print("Woof Woof!")

    def eat(self):
        super().eat()
        print("I like Bones!")

my_robot_dog = Robot_Dog("Spot")
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()