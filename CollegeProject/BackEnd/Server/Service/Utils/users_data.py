import json

def load_users():
    try:
        with open('../../Repository/users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    return users

# Save users to JSON file
def save_users(users):
    with open('../../Repository/users.json', 'w') as f:
        json.dump(users, f)