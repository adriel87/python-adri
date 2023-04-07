# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26,1}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Exercises: Level 1

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['CCC','Bitbox'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(it_companies)

# What is the difference between remove and discard
'''
whit the remove method if we try to remove and the object dont exist the method throw an Error
dicard method don't throw error in the same case
'''

# Exercises: Level 2

# Join A and B

set_c = A.union(B)
print(set_c)

# Find A intersection B

intersection_a = A.intersection(B)
print(intersection_a)

# Is A subset of B

print('A is subset of B : ', A.issubset(B))

# Are A and B disjoint sets

print('A and  B disjoint : ', A.isdisjoint(B))

# Join A with B and B with A

# What is the symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)
'''
the symmetric difference are the values that not share between us
'''
# Delete the sets completely

del A,B

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
print("is list of ages greater than set of ages : ", len(age) > len(ages_set) )

# Explain the difference between the following data types: string, list, tuple and set
'''
string, is a list of one or more caracters
list, is a data structure modifiable accepts repeats values
tuple, is a data structure inmmutable accepts repeats values
set, is a data structure modifiable dont accepts repeats values
'''

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_set = set(sentence.split(' '))

print(f'the sentence:\n{sentence}\nHas {len(sentence_set)} unique words')

