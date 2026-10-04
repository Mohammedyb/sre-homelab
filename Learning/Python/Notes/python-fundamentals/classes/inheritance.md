# Class inheritance

I use inheritance when one class should reuse or extend another class. The
child class names the parent class in parentheses.

```python
class Dog:
    def bark(self):
        return "Woof!"

class RobotDog(Dog):
    def charge(self):
        return "Charging"

my_dog = RobotDog()
print(my_dog.bark())    # Inherited from Dog
print(my_dog.charge())
```

`RobotDog` inherits `bark()` from `Dog` and adds its own `charge()` method.
I can use `super()` in a child class to call a method from its parent.
