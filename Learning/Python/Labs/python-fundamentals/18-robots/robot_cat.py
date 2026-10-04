from robot import Robot

class Robot_Cat(Robot):
    def make_noise(self):
        print("Meow, Meow!")

    def eat(self):
        super().eat()
        print("I like Milk!")

my_robot_cat = Robot_Cat("Sylvester")
my_robot_cat.walk(10)
my_robot_cat.make_noise()
my_robot_cat.eat()