import numpy as np

# vamos a ver operaciones matematicas con numpy

# adicion

np_array_from_list = np.array([1,2,3])

print('original array ', np_array_from_list)

# sumamos 10 a todas las posiciones del array
ten_plus_array = np_array_from_list + 10

print(ten_plus_array)

# subtraction

ten_minus_array = np_array_from_list - 10
print(ten_minus_array)

# multiplication

ten_times_array = np_array_from_list * 10
print(ten_times_array)

# division

ten_times_array_div = np_array_from_list / 10
print(ten_times_array_div)

# module

module_by_3_array = np_array_from_list % 3
print(module_by_3_array)

# floor division
ten_times_array_div_floor = np_array_from_list // 2
print(ten_times_array_div_floor)

# exponential
ten_times_array_exp = np_array_from_list ** 3
print(ten_times_array_exp)


