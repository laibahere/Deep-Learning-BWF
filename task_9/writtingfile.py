#10.1
filename = 'learning_python.txt'

# Reading the file and printing the contents by reading the entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# Reading the file and printing the contents by looping over each line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Reading the file and storing the lines in a list, and then printing the contents
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

