from math import radians, tan, pi

#exercise 1
user_input = int(input("Input degree: "))
def to_radians(n):
    to = radians(n)
    print("Output radian:",to)

to_radians(user_input)



#exercise 2
height_input = int(input("Height: "))
base1_input = int(input("Base1: "))
base2_input = int(input("Base2: "))

def area_t(h, m, n):
    area = 1/2*(m+n)*h
    print("Expected Output:", area)

area_t(height_input, base1_input, base2_input)



#exercise 3
number_input = int(input("Input number of sides: "))
length_input = int(input("Input the length of a side: "))

def area_p(n, l):
    area = (n * l**2) / (4 * tan(pi/n))
    print("The area of the polygon is:", area)

area_p(number_input, length_input)



#exercise 4
length_input = int(input("Length of base: "))
height_input = int(input("Height of parallelogram: "))

def area_p(l, h):
    area = l * h
    print("Expected Output:", area)

area_p(length_input, height_input)
