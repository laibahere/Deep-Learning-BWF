#CHAP 3 TRY IT YOURSELF 
#3-1. Names
friends=['Joey','David','Bilal','Hamza']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

#3.2 Greetings

names =['Joey','David','Bilal','Hamza']
print("Hello, {}! How are you today?".format(names[0]))
print("Hello, {}! How are you today?".format(names[1]))
print("Hello, {}! How are you today?".format(names[2]))
print("Hello, {}! How are you today?".format(names[3]))


#3-3 Your Own List
transportation = ["Honda motorcycle", "Yamaha", "Suzuki"]
print("I would like to own a " + transportation[0] + ".")
print("I have always wanted a " + transportation[1] + ".")
print("My first car was a " + transportation[2] + ".")

#3.4 Guest list
guests = ["Albert Einstein", "Emma Watson", "Katrina Kaif"]

print("Dear {}, I would like to invite you to dinner at my house on Sunday evening.".format(guests[0]))
print("Dear {}, I would be honored if you could join me for dinner on Sunday night.".format(guests[1]))
print("Dear {}, please accept my invitation to dinner at my home on Sunday.".format(guests[2]))

#3-5. Changing Guest List
guests = ["Albert Einstein", "Emma Watson", "Katrina Kaif"]

print("Dear {}, I would like to invite you to dinner at my house on Sunday evening.".format(guests[0]))
print("Dear {}, I would be honored if you could join me for dinner on Sunday night.".format(guests[1]))
print("Dear {}, please accept my invitation to dinner at my home on Sunday.".format(guests[2]))

print("{} can't make it to dinner, unfortunately.".format(guests[1]))

#who couldnt replace below guest with them
guests[1] = "Klaus Mikealson"

# Print updated invitation messages
print("Dear {}, I would like to invite you to dinner at my house on Saturday evening.".format(guests[0]))
print("Dear {}, please accept my invitation to dinner at my home on Saturday.".format(guests[1]))
print("Dear {}, please accept my invitation to dinner at my home on Saturday.".format(guests[2]))



#3.6 more guest
guests = ["Albert Einstein", "Emma Watson", "Katrina Kaif"]
print("Good news! We found a bigger dinner table.")

guests.insert(0, 'Albert Einstein')
guests.insert(2, 'Emma Watson')
guests.append('Katrina Kaif ')

print(f"Dear {guests[0]}, please come to my dinner party!")
print(f"Dear {guests[1]}, please come to my dinner party")
print(f"Dear {guests[2]}, please come to my dinner party!")

#3.7 Shrinking guest list
ValueErrorguests = ["Albert Einstein", "Emma Watson", "Katrina Kaif", "Klaus Mikealson"]
print(f"Dear {guests[0]}, I would like to invite you to my dinner party.")
print(f"Dear {guests[1]}, I would like to invite you to my dinner party.")
print(f"Dear {guests[2]}, I would like to invite you to my dinner party.")
print(f"Dear {guests[3]}, I would like to invite you to my dinner party.")

# One guest can't make it
cannot_attend = guests.pop(2)
print(f"Unfortunately, {cannot_attend} can't make it to the dinner.")

# Add new guests
guests.insert(0, 'Albert Einstein')
guests.insert(3, 'Katrina Kaif')
guests.append('Klaus Mikealson')

# Print new invitation messages
print(f"Dear {guests[0]}, I found a bigger dinner table, so you're invited to the dinner party!")
print(f"Dear {guests[1]}, I found a bigger dinner table, so you're invited to the dinner party!")
print(f"Dear {guests[2]}, I found a bigger dinner table, so you're invited to the dinner party!")
print(f"Dear {guests[3]}, I found a bigger dinner table, so you're invited to the dinner party!")

# The table won't arrive in time, can only invite two guests
print("Sorry, I can only invite two guests to the dinner party.")

# Remove guests until only two remain
cannot_attend = guests.pop()
print(f"Sorry, {cannot_attend}, I can't invite you to the dinner party.")
cannot_attend = guests.pop()
print(f"Sorry, {cannot_attend}, I can't invite you to the dinner party.")

# Print invitation to the remaining guests
print(f"Dear {guests[0]}, you're still invited to the dinner party!")
print(f"Dear {guests[1]}, you're still invited to the dinner party!")