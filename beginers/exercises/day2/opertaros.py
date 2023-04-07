# Day 2 of Python in 30 days OPERATORS

age : int = 36
height : float = 1.72
complex_number : complex = 0j


# calculate area whit a UI console

base = input("Enter base: ")
height = input("Enter height: ")
area = 0.5 * float(base) * float(height)
print("The area of the triangle is ", area)

# calculate the perimeter of triangle

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))

perimeter = side_a + side_b + side_c

print("The perimeter of the triangle is ", perimeter)

# calculate the area and perimeter of rectangle

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))

area = side_a * side_b
perimeter = 2 * (side_a + side_b)
print("The area is : " , area)
print("The perimeter is :", perimeter)

# area and circunference of circle

radius = float(input("Enter the radius : "))
pi = 3.1417

area = pi * radius**2
circunference = 2 * pi * radius

print("The area is ", area)
print("The circunference is ", circunference)

# slope calculating
x = float(input("Enter x : "))
slope_interception = 2 * x - 2


x1 = float(input("Enter x1 : "))
x2 = float(input("Enter x2 : "))
y1 = float(input("Enter y1 : "))
y2 = float(input("Enter y2 : "))

slop_distance = y2-y1/x2-x1
print("The slop for the previous values is ", slop_distance)


# comparing slopes

print("is equal ", slop_distance == slope_interception)
print("is greater ", slop_distance > slope_interception)
print("is lower ", slop_distance < slope_interception)

# ecuation

x = float(input("Enter x : "))
ecuation = x**2 + 6*x + 9
print("Ecuation value ", ecuation)

# comparations
print("The comparison of python and dragon is ", len("pithon") == len("dragon"))

print("On is in pithon and dragon ", 'on' in 'python' and 'dragon')
sentence = "I hope this course is no full of jargon."
print(sentence, 'jargon' in sentence, sep=' is jargon in sentence? ')


print("On is on python and dragon ", 'on' in 'python' and 'dragon')

print("the length of python to float and to string ", str(float(len('python'))))

user_number = float(input("introduce a number "))
print("is even number ", user_number % 2 == 0)

print('floor division between 7 and 3', 7//3, '\n','is equal to int cast of 2.7 ', int(2.7) == 7//3)

print('checking types "10" and 10, are equal ', type("10") == type(10))

print(int(9.8) == 10)

hours = int(input("Enter the hours "))
rate = float(input("Enter rate per hour "))
print(f'your weakly earning is {hours*rate}')


transfor_year_to_seconds = 365 * 24 * 60 * 60

years_to_transform = int(input("Enter number of years you have lived "))

print(f'You have live for {years_to_transform * transfor_year_to_seconds} seconds')

numbers = [1,2,3,4,5]
for number in numbers:
    print(number, 1, number * 1, number**2, number**3)












