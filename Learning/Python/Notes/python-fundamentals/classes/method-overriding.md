# Method overriding

I override a method when a child class defines a method with the same name as
one in its parent class. The child object's method is used instead of the
parent's version.

```python
class Dog:
    def make_noise(self):
        return "Some noise"


class RobotDog(Dog):
    def make_noise(self):
        return "Woof woof!"


my_dog = RobotDog()
print(my_dog.make_noise())  # Woof woof!
```

`RobotDog` overrides `Dog.make_noise()`. I can call `super().make_noise()`
inside the child method if I also want to use the parent's version.
