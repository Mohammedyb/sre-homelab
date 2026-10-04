# Class inheritance

I use inheritance when one class should reuse or extend another class. The
child class names the parent class in parentheses.

- A [parent class](parent-class.md) provides behavior that another class can
  inherit.
- A [child class](child-class.md) inherits and can add or change behavior.

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

See [method overriding](method-overriding.md) for replacing an inherited
method with a child class's version.
