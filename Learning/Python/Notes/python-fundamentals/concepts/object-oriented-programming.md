# Object-oriented programming

Object-oriented programming (OOP) is a way to organize code around objects.
Objects combine data (attributes) with actions (methods). I define a
[`class`](../classes/classes.md) to describe the objects I want to create.

```python
class Movie:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return f"Movie: {self.title}"

movie = Movie("The Grinch")
print(movie.describe())
```

Here, `Movie` is the class, `movie` is an object, `title` is an attribute,
and `describe()` is a method. OOP helps me keep related data and behavior
together. For simpler data, I can also use a
[dictionary](../data-types/dictionaries-as-objects.md).
