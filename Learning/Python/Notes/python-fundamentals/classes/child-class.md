# Child classes

A child class (also called a subclass) inherits from a parent class. I put
the parent class name in parentheses. The child can use inherited methods and
add its own behavior.

```python
class Dog:
    def bark(self):
        return "Woof!"


class RobotDog(Dog):
    def charge(self):
        return "Charging"
```

Here, `RobotDog` inherits from `Dog`, so its instances can use `bark()` as
well as `charge()`.
