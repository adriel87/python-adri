from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def to_upper(word):
    return word.upper()

def square_number(number):
    return number ** 2

def create_sentence(word_a,word_b):
    sentence = f'{word_a}, {word_b}'
    return f'{sentence}'

def sum(a,b):
    return a+b

country_has_land = lambda country: not country.__contains__('land')

country_in_six_letters = lambda country: len(country) == 6

country_in_six_letters_and_more = lambda country: len(country) >= 6

word_start_whit_E = lambda word: word[0] == 'E'

to_str = lambda t: str(t)

# Use map to create a new list by changing each country to uppercase in the countries list
upper_countries = map(to_upper,countries)
print(list(upper_countries))
# Use map to create a new list by changing each number to its square in the numbers list
the_square = list(map(square_number, numbers))
print(the_square)
# Use map to change each name to uppercase in the names list
print(list(map(to_upper,names)))
# Use filter to filter out countries containing 'land'.
print(list(filter(country_has_land, countries)))
# Use filter to filter out countries having exactly six characters.
print(list(filter(country_in_six_letters, countries)))
# Use filter to filter out countries containing six letters and more in the country list.
print(list(filter(country_in_six_letters_and_more, countries)))
# Use filter to filter out countries starting with an 'E'
print(list(filter(word_start_whit_E, countries)))
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print(list(map(to_upper,filter(country_in_six_letters, countries))))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
print(list(map(to_str,numbers)))
# Use reduce to sum all the numbers in the numbers list.
print(reduce(lambda a,b:a+b, numbers))

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print(reduce(create_sentence, countries))
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.