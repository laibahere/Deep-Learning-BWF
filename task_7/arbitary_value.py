#8-9
def show_magicians(magicians):
 for magician in magicians:
  print(magician)

magicians = ['Houdini', 'David Blaine', 'David Copperfield', 'Penn and Teller']
show_magicians(magicians)

#8-10 
def make_great(magicians):
 for i in range(len(magicians)):
  magicians[i] = "The Great " + magicians[i]
  return magicians

magicians = ['Houdini', 'David Blaine', 'David Copperfield', 'Penn and Teller']
great_magicians = make_great(magicians[:]) # pass a copy of the list
show_magicians(great_magicians)

#8-11
magicians = ['Houdini', 'David Blaine', 'David Copperfield', 'Penn and Teller']
great_magicians = make_great(magicians[:]) # pass a copy of the list
show_magicians(magicians) # original list is unchanged
show_magicians(great_magicians) # new list with "The Great" added to each magician's name

#8-12. Sandwiches
def make_sandwich(*items):
 print("Making a sandwich with the following items:")
 for item in items:
  print("- " + item)

make_sandwich('cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'bacon', 'mayo', 'avocado')
make_sandwich('peanut butter', 'jelly')

#8-13. User Profile
def build_profile(first, last, **user_info):
 profile = {}
 profile['first_name'] = first
 profile['last_name'] = last
 for key, value in user_info.items():
  profile[key] = value
  return profile

my_profile = build_profile('John', 'Doe', age=30, location='USA', occupation='Engineer')
print(my_profile)

#8-14. Cars
def make_car(manufacturer, model, **car_info):
 car = {}
 car['manufacturer'] = manufacturer
 car['model'] = model
 for key, value in car_info.items():
  car[key] = value
 return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)