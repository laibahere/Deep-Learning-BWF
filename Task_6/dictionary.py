#---------Examples-------
#a simple dictionary 
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

#accessing value in dictionaries
new_points= alien_0['points']
print("you just earned " + str(new_points)+ " points")

# Adding new key value pair:
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#starting with empty dictionary 
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 8
print(alien_1)

#Modifying Values in a Dictionary
#consider an alien that changes from green to yellow as a game progresses:
alien_0={'color':'Green'}
print("The alien is "+alien_0['color'] +".")
alien_0['color']='Yellow'
print("The alien is now "+alien_0['color'] +".")

#removing key value pair 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
#looping in dictictonaries
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
 print("\nKey: " + key)
 print("Value: " + value)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
 print(name.title() + "'s favorite language is " +language.title() + ".")

#Looping through all the key in a dictionary 
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
 print(name.title())

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(name.title())
if name in friends:
 print("Hi"+name.title()+",I see your favorite language is"+favorite_languages[name].title()+"!")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
 print(name.title() + ", thank you for taking the poll.")

# looping through all values in a dictionary 
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())

 #a list of dictionaries
alien_3={'color':'green','points':5}
alien_4={'color':'Yellow','points':10}
alien_5={'color':'Red','points':15}
aliens=[alien_3,alien_4,alien_5]
for alien in aliens:
    print(aliens)

#a list in dictionaries
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
for topping in pizza['toppings']:
 print("\t" + topping)

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
 print("\n" + name.title() + "'s favorite languages are:")
 for language in languages:
     print("\t" + language.title())

#for dic in dic 
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
 
for username, user_info in users.items():
  print("\nUsername: " + username)
  full_name = user_info['first'] + " " + user_info['last']
  location = user_info['location']
  print("\tFull name: " + full_name.title())
  print("\tLocation: " + location.title())