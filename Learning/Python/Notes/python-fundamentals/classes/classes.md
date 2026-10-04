# Classes

I use a class as a blueprint for creating objects. An object made from a
class is called an instance. A class can define data as attributes and
behavior as methods.

```python
class Movie:
    def __init__(self, title, showtime):
        self.title = title
        self.showtime = showtime

movie = Movie("The Grinch", "11:00am")
print(movie.title)
```

See [`__init__()`](init-method.md) for how I initialize an instance.
`self` refers to the instance being created or used.

See [objects](objects.md) for more about instances and attributes.
See [methods](../methods/methods.md) for how I define behavior on a class.
See [class inheritance](inheritance.md) to reuse or extend another class.
