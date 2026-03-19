# Dictionary Lookup

A Python function that searches through a list of user records and returns
the matching entry by ID. Returns a clear error message if the user is not found.

## What It Does
- Accepts a list of user dictionaries and a target ID
- Returns the matching user dictionary if found
- Returns `{"error": "User not found"}` if no match exists
- Raises a TypeError if input is not a list

## Sample Output
```python
get_user_info(users, 3)  # {'id': 3, 'name': 'Gold', 'age': 22}
get_user_info(users, 7)  # {'error': 'User not found'}
```

## Requirements
- Python 3.x

## Author
Ghani Regina Gold B. San Luis
```

---

## 2. 📁 `python-fibonacci-generator`
**Description:**
```
Python function that generates the first N numbers of the Fibonacci sequence.
