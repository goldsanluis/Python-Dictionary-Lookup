def get_user_info(data, user_id):
    """Return user dictionary if found, otherwise return error message."""
    if not isinstance(data, list):
        raise TypeError("Data must be a list")

    for user in data:
        if user["id"] == user_id:
            return user

    return {"error": "User not found"}


users = [
    {"id": 1, "name": "Ghani", "age": 21},
    {"id": 2, "name": "Regina", "age": 28},
    {"id": 3, "name": "Gold", "age": 22},
    {"id": 4, "name": "Bernal", "age": 25},
    {"id": 5, "name": "San", "age": 30},
    {"id": 6, "name": "Luis", "age": 27}
]

print(get_user_info(users, 1)) # {'id': 1, 'name': 'Ghani', 'age': 21}
print(get_user_info(users, 2)) # {'id': 2, 'name': 'Regina', 'age': 28}
print(get_user_info(users, 3)) # {'id': 3, 'name': 'Gold', 'age': 22}
print(get_user_info(users, 4)) # {'id': 4, 'name': 'Bernal', 'age': 25}
print(get_user_info(users, 5)) # {'id': 5, 'name': 'San', 'age': 30}
print(get_user_info(users, 6)) # {'id': 6, 'name': 'Luis', 'age': 27}
print(get_user_info(users, 7))  # User not found
