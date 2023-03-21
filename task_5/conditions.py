#example !
cars=['audi','bmw','sabaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#---- Try it yourself of Chapter 5 topic conditions -----
# 5-1. Conditional Tests:
# Test 1: Is 5 greater than 3?
print("Is 5 > 3? I predict True.")
print(5 > 3)

# Test 2: Is 2 plus 2 equal to 5?
print("Is 2 + 2 == 5? I predict False.")
print(2 + 2 == 5)

# Test 3: Is the string "hello" equal to "Hello"?
print('Is "hello" == "Hello"? I predict False.')
print("hello" == "Hello")

# Test 4: Is the string "python" in the list ['java', 'c++', 'python']?
print('Is "python" in ["java", "c++", "python"]? I predict True.')
print("python" in ["java", "c++", "python"])

# Test 5: Is 6 less than or equal to 6?
print("Is 6 <= 6? I predict True.")
print(6 <= 6)

# Test 6: Is the boolean value True equal to the integer value 1?
print("Is True == 1? I predict True.")
print(True == 1)

# Test 7: Is the variable x not equal to 10?
x = 5
print("Is x != 10? I predict True.")
print(x != 10)

# Test 8: Is the length of the string "apple" equal to the length of the string "banana"?
print('Is len("apple") == len("banana")? I predict False.')
print(len("apple") == len("banana"))

# Test 9: Is 3 less than 4 and 4 less than 5?
print("Is 3 < 4 < 5? I predict True.")
print(3 < 4 < 5)

# Test 10: Is 7 greater than or equal to 10 or 5 less than 2?
print("Is 7 >= 10 or 5 < 2? I predict False")
print(7>=10 or 5<2)
      
#5-2. More Conditional Tests
# Tests for equality and inequality with strings
fruit = "apple"
print("Is the fruit 'banana'? I predict False")
print(fruit == "banana")
print("\nIs the fruit 'apple'? I predict true")
print(fruit == "apple")

# Tests using the lower() function
name = "Hassan"
print("Is the name 'Hassan'? I predict True.")
print(name.lower() == "Hassan")
print("\nIs the name 'Hamza'? I predict False.")
print(name.lower() == "Hamza")

# Numerical tests
age = 25
print("Is age equal to 25? I predict True.")
print(age == 25)
print("\nIs age not equal to 30? I predict True.")
print(age != 30)
print("\nIs age greater than 18 and less than 30? I predict True.")
print(18 < age < 30)
print("\nIs age greater than or equal to 25? I predict True.")
print(age >= 25)
print("\nIs age less than or equal to 30? I predict True.")
print(age <= 30)
print("\nIs age less than 18 or greater than 30? I predict False.")
print(age < 18 or age > 30)

# Test whether an item is in a list
fruits = ["apple", "banana", "orange"]
print("Is 'apple' in the list of fruits? I predict True.")
print("apple" in fruits)
print("\nIs 'grape' in the list of fruits? I predict False.")
print("grape" in fruits)

# Test whether an item is not in a list
numbers = [1, 2, 3, 4, 5]
print("Is 6 not in the list of numbers? I predict True.")
print(6 not in numbers)
print("\nIs 3 not in the list of numbers? I predict False.")
print(3 not in numbers)
