import numpy as np

# print('numpy ', np.__version__)

# print(dir(np))

# creando una lista en python

my_list = [1,2,3,4]

# comprobando la lista

print(type(my_list))

# array de 2 dimensiones

my_two_dimension_list = [[1,2,3],[4,5,6],[7,8,9]]

# creando una lista de numpy

numpy_array_from_list = np.array(my_list)

print(type(numpy_array_from_list))

print(numpy_array_from_list)

# creando una lista de numpy parseando a float

numpy_float_array_from_list = np.array(my_list, dtype=float)

print(numpy_float_array_from_list)

# una lista de booleanos

boolean_list = [0,1,-1,-0]

numpy_boolean_list = np.array(boolean_list, dtype=bool)
print(numpy_boolean_list)

# array multidimensional
numpy_multidimensional_list = np.array(my_two_dimension_list)
print(type(numpy_multidimensional_list))
print(numpy_multidimensional_list)

# convirtiendo numpy arrays to list

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print(np_to_list)

print('one dimension ', np_to_list)
print('n dimensions ', numpy_multidimensional_list.tolist())

# un array desde una tupla

my_tuple = (1,2,3,4,5)

np_array_from_tuple = np.array(my_tuple)
print(np_array_from_tuple)

# shape of numpy array
# devuelve la forma que tiene el array, donde el primer valor es el numero de la fila 
# y el segundo es el numero de la columna

print(np.array([[2,2,2],[3,3,3]]).shape)

# tipos de datos en los arrays de numpy

int_list = np.array([1,2,3])
float_list = np.array([1,2,3], dtype=float)

print(int_list, int_list.dtype,sep=' ')
print(float_list, float_list.dtype,sep=' ')

# size on numpy array

print(int_list.size, ' one dimesion array')
print(numpy_multidimensional_list.size, ' two dimension array')
