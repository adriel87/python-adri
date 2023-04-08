from random import randint, shuffle
from string import ascii_letters, digits,hexdigits

def rgb_color_gen():
    return f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})'


def hexa_color_gen():
    hexa_color=''
    for digit in range(6):
        hexa_color += hexdigits[randint(0,len(hexdigits)-1)]
    return '#'+hexa_color

def generate_colors(type , how_many):
    list_of_colors = []
    function_to_exec = rgb_color_gen if type == 'rgb' else hexa_color_gen
    for i in range(how_many):
        list_of_colors.append(function_to_exec())

    return list_of_colors


def shuffle_list(list):
    shuffle(list)
    return list

def seven_unique_random_numbers():
    number_set = set()
    while len(number_set) < 7:
        number_set.add(randint(0,9))
    
    return list(number_set)

print(seven_unique_random_numbers())