# Dictionary `.items()`

I use `.items()` to get a view of a dictionary's key-value pairs. I can loop
through the pairs by unpacking each one into two variables.

```python
schedule = {"Ada": "11:00", "Grace": "13:00"}

for name, time in schedule.items():
    print(name, time)
```
