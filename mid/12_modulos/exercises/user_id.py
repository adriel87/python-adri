from random import randint
from string import ascii_letters, digits


def random_user_id():
    characters = ascii_letters + digits
    user_id_list=[]
    digits_range = int(input('introduce a range for id : '))
    number_of_ids = int(input('how many ids do you want : '))
    for id in range(number_of_ids):
        user_id_list.append('')
        for digit in range(digits_range):
            user_id_list[id] += characters[randint(0,len(characters))]
            # print(id, digit)
    
    return user_id_list

print(random_user_id())