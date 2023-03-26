#Try It Yourself

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
def make_shirt(size, message):
    print(f"\nMy shirt size is {size}.")
    print(f"My message is: {message}")
make_shirt('M', 'Python is fun!')
make_shirt(size='L', message='I heart Python')

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
#large
def make_shirt(size='large', message='I love Python'):
    print(f"\nMaking a {size} shirt with the message: {message}")
#medium
make_shirt()
make_shirt('medium')
make_shirt('small', 'Python is awesome!')

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city, country='USA'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('new york')
describe_city('los angeles')
describe_city('reykjavik', 'iceland')



