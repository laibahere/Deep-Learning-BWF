#5-3. Alien Colors #1
alien_color = ['Green', 'Yellow', 'Red']
if 'Green' in alien_color:
    print("You earned 5 points")

#5-4. Alien Colors #2:
alien_color = ['Green', 'Yellow', 'Red']
if 'Green' in alien_color:
    print("You earned 5 points")
else :
    print("You earned 10 points")

#5-5. Alien Colors #3:
alien_color = 'Green'

if alien_color == 'Green':
    print("You earned 5 points")
elif alien_color == 'Yellow':
    print("You earned 10 points")
else:
    print("You earned 15 points")


#5-6. Stages of Life:


age = 30

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
#5-7. Favorite Fruit:

favorite_fruits = ['banana', 'apple', 'mango']

if 'banana' in favorite_fruits:
    print("You really like bananas!")
    
if 'apple' in favorite_fruits:
    print("You really like apples!")
    
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
    
if 'watermelon' in favorite_fruits:
    print("You really like watermelons!")
    
if 'orange' in favorite_fruits:
    print("You really like oranges!")

#5-8. Hello Admin:
user_name=['David','Emma','Harry','John','Admin']
for user_name in user_name:
    if user_name == 'Admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello" + user_name.title() +"thank you for log-ging in again.")

#5-9. No Users
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")

#5-10. Checking Usernames:


# create a list of current users
current_users = ['john', 'mary', 'peter', 'emma', 'david']

# create a list of new users
new_users = ['peter', 'susan', 'lisa', 'DAVID', 'steve']

# convert all usernames in current_users to lowercase
current_users_lower = [user.lower() for user in current_users]

# check if each new user already exists in the list of current users
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, the username '{user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{user}' is available.")

#5-11. Ordinal Numbers:

numbers = list(range(1, 10))
for number in numbers:
    if number % 10 == 1 and number != 11:
        print(f"{number}st")
    elif number % 10 == 2 and number != 12:
        print(f"{number}nd")
    elif number % 10 == 3 and number != 13:
        print(f"{number}rd")
    else:
        print(f"{number}th")
