# Methods

I define a method inside a class to describe something its objects can do.
When I call an instance method on an object, Python passes that object as the
first argument, usually named `self`.

```python
class RobotDog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

my_dog = RobotDog("Sheriff")
print(my_dog.bark())
```

I call a method with dot notation, like `my_dog.bark()`. Unlike a regular
function, a method belongs to a class and can use the instance's attributes.
