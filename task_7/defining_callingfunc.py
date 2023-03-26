#Try It Yourself

#8-1. Message: Write a function called display_message() that prints one sen- tence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly
def display_message():
    """Prints a message about what I'm learning in this chapter."""
    print("In this chapter, I am learning about functions in Python.")
display_message()

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
def favourite_book():
     """Print message about what my favourite book is """
     fav_book=input("What is your favourite book:")
     print("Favourite book is "+fav_book)
favourite_book()