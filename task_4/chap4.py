
pizzas = ['Pepperoni', 'Tikka', 'Supreme']

print("Pizza Menu:")
for pizza in pizzas:
    print(pizza)

print("\nI like these pizzas:")
for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("\nPizza is my favorite food!")
print("I can eat pizza anytime, anywhere.")
print("It's just so delicious and satisfying.")
print("I really love pizza!")

#4.2 animals
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(animal)

for animal in animals:
    print("A"+ animal + "would make a great pet.")

print("Any of these animals would make a great pet!")

#4.3
for number in range(1, 21):
    print(number)

#4.4 counting till million
# list of numbers from 1 to 1,000,000
numbers = list(range(1, 1000001))
for number in numbers[:10]:
    print(number)

#Summing a Million:
numbers = list(range(1, 1000001))
print("Minimum number in the list: ", min(numbers))
print("Maximum number in the list: ", max(numbers))
print("Sum of all numbers in the list: ", sum(numbers))

#4-6. Odd Numbers:
odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

#4-7. Threes:
multiples_of_3 = list(range(3, 31, 3))

for num in multiples_of_3:
    print(num)

#4-8. Cubes:
cubes = []
for i in range(1, 11):
    cube = i ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

#4-9. Cube Comprehension
cubes = [num ** 3 for num in range(1, 11)]
print(cubes)

#4-10. Slices
numbers = list(range(1, 11))

# print the entire list
print("The full list of numbers:")
print(numbers)

# print the first three items
print("\nThe first three items in the list are:")
print(numbers[:3])

# print three items from the middle of the list
print("\nThree items from the middle of the list are:")
print(numbers[3:6])

# print the last three items in the list
print("\nThe last three items in the list are:")
print(numbers[-3:])

#4-11. My Pizzas, Your Pizzas:
# Original list of pizzas
pizzas = ['Pepperoni', 'Tikka', 'Supreme']

# Copying the list
friend_pizzas = pizzas[:]

# Adding a new pizza to the original list
pizzas.append('Vegetarian')

# Adding a different pizza to the friend's list
friend_pizzas.append('Hawaiian')

# Printing the two separate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
