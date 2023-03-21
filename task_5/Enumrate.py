languages=['English','Spanish','Japanese']
enumerate_prime= enumerate(languages)
print(list(enumerate_prime))

#----working of enumerate ---
#to show enumerate class
languages=['English','Spanish','Japanese']
enumerate_prime= enumerate(languages)
print(type(enumerate_prime))

#converting to list
print(list(enumerate_prime))

#changing the default counter 
enumerate_Prime=enumerate(languages,10)
print(list(enumerate_Prime))

#--- looping over an enumerate object
for item in enumerate(languages):
    print(item)

#to count by using loops
for count, item in enumerate(languages):
    print(count,item)
# changing default start value 
for count,item in enumerate(languages,100):
    print(count,item)
