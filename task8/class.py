#9.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Pizza Place", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("Pizza Place", "Italian")
restaurant2 = Restaurant("Mc Donalds", "American")
restaurant3 = Restaurant("Burger Clock", "English")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9.3
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.city}.")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! How are you doing today?")

user1 = User("John", "Lee", 35, "New York")
user2 = User("Jane", "Austen", 27, "Los Angeles")
user3 = User("Bob", "Marley", 42, "Chicago")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

#9.4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant("La Piazza", "Italian")
print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")
restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(25)
print(f"Number of customers served: {restaurant.number_served}")

#9.5
class User:
    def __init__(self, first_name, last_name, age, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.city}, {self.country}")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("John", "Lee", 30, "New York", "USA")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
