
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filter_numbers = [i for i in numbers if i > 0]

print(filter_numbers)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

one_dimension_list = [number for paquet in list_of_lists for row in paquet for number in row  ]



print(one_dimension_list)

tuplations = [(i, 1, i, i**2,i**3,i**4,i**5) for i in range(11)]

print(tuplations)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_countries = [[i[0], i[0][0:3],i[1]] for country in countries for i in country]

dictionary_countries = [[{'country':i[0], 'city':i[1]}] for country in countries for i in country]

print(flat_countries)

print(dictionary_countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

names_flat = [ f'{i[0]} {i[1]}' for name in names for i in name]

print(names_flat)