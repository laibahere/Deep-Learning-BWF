#9.10
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


# main.py
from restaurant import Restaurant

restaurant = Restaurant("Pizza Planet", "Italian")
restaurant.describe_restaurant()
#9.11
# user.py
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and has an email of {self.email}.")


# privileges.py
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# admin.py
from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()

# main.py
from admin import Admin

admin = Admin("John", "lee", 35, "johnlee@example.com")
admin.privileges.show_privileges()

#9.12
# user.py
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and has an email of {self.email}.")


# admin.py
from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()


# privileges.py
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# main.py
from admin import Admin

admin = Admin("John", "Doe", 35, "johndoe@example.com")
admin.privileges.show_privileges()
