#string try it yourself
#2.3 Personal Message
name="Eric"
print("Hello " + name + " would you like to learn some Python today?")

#2.4 New cases
#uppercase
name="eric"
print(name.upper())
#lowercase 
print(name.lower())
#titlecase
print(name.title())

#2.5 famous quote

quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
print(author + ' once said, "' + quote + '"')

#2.6 famous quote 2
famous_person="Albert Einstein"
message = "A person who never made a mistake never tried anything new."
print(famous_person + ' once said, "' + message+ '"')

#2.7 stripping names
name = "\t\n   Bytewise Fellowship   \n\t"

# whitespace characters
print("Name with whitespace: " + name)

# Remove whitespace from the left side of the name
name_lstrip = name.lstrip()
print("Name with left-side whitespace removed: " + name_lstrip)

# Remove whitespace from the right side of the name
name_rstrip = name.rstrip()
print("Name with right-side whitespace removed: " + name_rstrip)

# Remove whitespace from both sides of the name
name_strip = name.strip()
print("Name with all whitespace removed: " + name_strip)

