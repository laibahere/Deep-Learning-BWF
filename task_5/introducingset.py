#a set of integers  type 
student_id={122,123,125,126,124}
print('Student Id:', student_id)

#a set of string obj 
alphabets={'q','w','e','r','t','y'}
print("alphabets :",alphabets)

#set of a mixed types
mixed_set={"Hello",102,"o","23"}
print("set of mixed data types",mixed_set)

#an empty set
empty_set=set()
print("Data type of empty set is ", type(empty_set))

#duplicate items in a set 
numbers={2,4,4,8,8,6,6,9,8,6,4}
print(numbers)

# to add numbers into set 
numbers = {22, 33, 55, 11,44}
print('Initial Set:',numbers)
numbers.add(32)
print('Updated Set:', numbers) 

#updated python sets
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['Apple', 'Google', 'OpenAI']
companies.update(tech_companies)
print(companies)

#remove element from the sets

tech_Companies={'OpenAI', 'Apple', 'Lenovo', 'Samgsung', 'Google'}
print('Initial Set:',tech_Companies)
removedValue = tech_Companies.discard('Apple')
print('Set after remove():', tech_Companies)
