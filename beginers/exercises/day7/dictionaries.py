# Create an empty dictionary called dog
empty_dictionary = {}
# Add name, color, breed, legs, age to the dog dictionary
dog ={
    'name':'mickey',
    'color':'brown',
    'breed':'pues breed',
    'legs': 4,
    'age ':10,
}
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'',
    'last_name':'',
    'gender':'',
    'age':'',
    'marital status':'',
    'skills':['fps','mmo'],
    'country':'',
    'city':'',
    'address':'',
}
# Get the length of the student dictionary

print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student.get('skills'), type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('take care')


# Get the dictionary keys as a list
keys_of_student = student.keys()
# Get the dictionary values as a list
values_of_student = student.values()

# Change the dictionary to a list of tuples using items() method
changing = student.items()

# Delete one of the items in the dictionary
student.pop()

# Delete one of the dictionaries
del dog