#10.11
import json

filename = 'favorite_number.json'

# Prompt user for their favorite number
favorite_number = input("What is your favorite number? ")

# Store the favorite number in a file using JSON
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

**favorite_number_reader.py:**

```python
import json

filename = 'favorite_number.json'

# Read the favorite number from the file
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("You haven't set a favorite number yet!")
else:
    print(f"I know your favorite number! It's {favorite_number}.")

#10.12
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
        print(f"I know your favorite number! It's {favorite_number}.")
except FileNotFoundError:
    favorite_number = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print("Thanks, I'll remember that.")






#10.3
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
        correct = input("Is this the correct username? (y/n) ")
        if correct.lower() == 'n':
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
        else:
            print("Good to see you again, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
