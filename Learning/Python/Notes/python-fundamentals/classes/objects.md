# Objects

An object is a value I can work with in Python. Objects have a type and can
hold data or provide behavior. When I create an object from a class, I call
it an instance of that class.

```python
class Movie:
    def __init__(self, title):
        self.title = title

movie = Movie("The Grinch")
print(movie.title)
```

Here, `movie` is an object and an instance of `Movie`. I use dot notation to
read its `title` attribute. The class defines how its instances are created
and what data or methods they have.
