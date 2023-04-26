import numpy as np

# get a value

# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

# get values of a position
first_row = two_dimension_array[:,0]
second_row = two_dimension_array[:,1]
third_row = two_dimension_array[:,2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

# slicing an array

first_two_rows_and_columns = two_dimension_array[0:2,0:2]
print(first_two_rows_and_columns)

print(two_dimension_array, ' normal 2 dimension')
print(10*'-'+'separator'+10*'-')
print(two_dimension_array[::-1, ::-1], ' reverse')
print(10*'-'+'separator'+10*'-')
print(two_dimension_array[::-1,], ' reverse column')
print(10*'-'+'separator'+10*'-')
print(two_dimension_array[::, ::-1], ' reverse row')
print(10*'-'+'separator'+10*'-')


# create arrays from default values

zeros_2_dimension = np.zeros((3,3), dtype=int, order='C')
print(zeros_2_dimension)
print(10*'-'+'separator'+10*'-')

ones_2_dimension = np.ones((4,3),dtype=bool,order='C')
print(ones_2_dimension)
print(10*'-'+'separator'+10*'-')
# change the shape of array

unformated_array = np.zeros((5,4),dtype=int,order='C')
print(unformated_array, ' original shape')
print(10*'-'+'separator'+10*'-')

change_array_shape = np.reshape(unformated_array,(2,10))
print(change_array_shape, ' array shaped')
print(10*'-'+'separator'+10*'-')

change_array_shape = np.reshape(unformated_array,(10,2))
print(change_array_shape, ' array reshaped')
print(10*'-'+'separator'+10*'-')

# flat arrays

flated_array = change_array_shape.flatten()
print(flated_array, ' flated')
print(10*'-'+'separator'+10*'-')

# add values
# horizontal

first_array = np.array([1,2,3])
second_array = np.array([4,5,6])

horizontal_fusion_array = np.hstack([first_array,second_array])
print(horizontal_fusion_array, ' fusion ha')
print(10*'-'+'separator'+10*'-')

# vertical
vertical_fusion_array = np.vstack([first_array,second_array])
print(vertical_fusion_array, ' vertical fusion')
print(10*'-'+'separator'+10*'-')

# generate random numbers

random_float = np.random.random()

random_array_float = np.random.random(10)

random_int = np.random.randint(1,10,10)

random_2d_int = np.random.randint(1,10, (4,4))
print(random_2d_int)
print(10*'-'+'separator'+10*'-')

# matrix

four_by_four_matrix = np.matrix(np.ones((4,4)), dtype=float)
print(four_by_four_matrix)
print(10*'-'+'separator'+10*'-')

# assing value to row
np.asanyarray(four_by_four_matrix)[1]=7
print(four_by_four_matrix)
print(10*'-'+'separator'+10*'-')

# arrange
simple_list_arrange = [i for i in range(0,10,3)]
print(simple_list_arrange)
print(10*'-'+'separator'+10*'-')

array_numpy_arrange = np.arange(0,20,3)
print(array_numpy_arrange)
print(10*'-'+'separator'+10*'-')

# sequence of number using linespace