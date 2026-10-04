# The `__init__()` method

I use `__init__()` to set up an object's attributes when I create an instance.
Python calls it automatically when I create the object.

```python
class Movie:
    def __init__(self, title, showtime):
        self.title = title
        self.showtime = showtime

movie = Movie("The Grinch", "11:00am")
print(movie.title)
```

`self` refers to the new instance. The values I pass when creating `movie`
are given to `title` and `showtime`, then saved as instance attributes.
`__init__()` initializes the instance; it is not the method that creates it.
