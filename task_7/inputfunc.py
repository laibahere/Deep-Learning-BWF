#------ CH :7 "INPUT FUNCTION TRY IT YOURSELF" -----------------
#7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
car_type=input("What kind of car would you like:")
print("Let me see If I can you a "+ car_type.title())

#7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message say-ing they’ll have to wait for a table. Otherwise, report that their table is ready.
people_count=input("How many People are in their dinner group?")
people_count=int(people_count)
if people_count>=8:
 print("You will have to wait for a table")
else:
 print("Your table is ready ")

#7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
number=input("Enter your number :")
number=int(number)
if number%10==0:
 print("This number is multiple of 10")
else:
 print("This number is not multiple of 10")