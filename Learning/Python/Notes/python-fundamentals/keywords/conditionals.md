# Conditional keywords: `if`, `elif`, and `else`

Conditional statements choose which block of code to run based on conditions.

- `if` runs its indented block when its condition is true.
- `elif` checks another condition when preceding conditions were false. It is
  short for “else if.”
- `else` runs when none of the preceding conditions were true.

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "Keep practicing"
```

Python uses indentation to mark code blocks. Four spaces per indentation level
is the common convention; keep indentation consistent.
