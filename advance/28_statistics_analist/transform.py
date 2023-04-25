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