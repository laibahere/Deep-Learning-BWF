#Try It Yourself

#7-4.
# Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.
prompt = "Enter a pizza topping to add to your pizza, or enter 'quit' to end the program: "
message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print("I'll add " + message + " to your pizza!")

#7-5.
#  Movie Tickets: A movie theater charges different ticket prices depending ona person’s age. If a person is under the age of 3, the ticket is free; if they arebetween 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
while True:
    age = input("Please enter your age (or 'quit' to exit): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
#7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5that do each of the following at least once: • Use a conditional test in the while statement to stop the loop.• Use an active variable to control how long the loop runs. • Use a break statement to exit the loop when the user enters a 'quit' value.

#7-5 --Using a conditional test to stop the loop:

active = True
while active:
    age = input("Please enter your age (or 'quit' to exit): ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")

#Using an active variable to control how long the loop runs:age = ''
while age != 'quit':
    age = input("Please enter your age (or 'quit' to exit): ")
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
#Using a break statement to exit the loop:

while True:
    age = input("Please enter your age (or 'quit' to exit): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
#7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
while True:
    print("This loop will never end!")


#7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-ous sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
sandwich_orders = ['Chicken Sandwich', 'Shawarma Sandwich', 'Beef Sandwich', 'Tuna Sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order}.")
    finished_sandwiches.append(current_order)

print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)

