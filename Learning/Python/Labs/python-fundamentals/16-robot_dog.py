class Robot_Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Bark,Bark!")

#Main Program
def main():
    my_dog = Robot_Dog("Sherrif", "Labrador")
    print (my_dog.name)
    print(my_dog.breed)
    my_dog.bark()

main()