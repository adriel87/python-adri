# Day 2: 30 Days of python programming

first_name :str = 'Adriel'
last_name :str = 'Arocha'
full_name : str = f'{first_name} {last_name}'
country :str = 'Spain'
city: str = 'Las Palmas'
age : int = 36
year : int = 2023
is_married : bool = True
is_true : bool = True
is_light_on : bool = False

num_one, num_two , three, four = 5,4,3,4

print(
    type(first_name),
    type(last_name),
    type(full_name),
    type(country),
    type(city),
    type(age),
    type(year),
    type(is_married),
    type(is_true),
    type(is_light_on)
)

print(len(first_name), 'the firs name length')

print(len(first_name), len(last_name), sep='first name --- last name')


total = num_one+num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one/num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

pi = 3.1417
radio = 3
area_of_circle = pi * pow(radio,2)
circunference = 2*pi*radio

user_radio = input('introduce a radius')

area_of_circle = pi * pow(int(user_radio),2)

first_name = input('introduce first_name: ')
last_name = input('introduce last_name: ')
country = input('introduce country: ')
age = input('introduce age: ')

print('your personal info', first_name, last_name, country, age, sep='\n')


