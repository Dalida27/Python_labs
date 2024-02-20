#exercise 1
nums = input().split()
some_list = [int(num) for num in nums]

def my_square(n):
    for i in n:
        yield(i*i)
list = list(my_square(some_list))
print(*list)



#exercise 2
user_input = int(input())
def is_even(n):
    for i in range (0, n):
        if(i % 2 == 0):
            yield(i)

for num in is_even(user_input):
    print(num)


#exercise 3
nums = input().split()
some_list = [int(n) for n in nums]

def is_divisible(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield(i)

for num in is_divisible(max(some_list)):
    print(num)



#exercise 4
user_input1 = int(input())
user_input2 = int(input())
def squares(n, m):
    for i in range(n, m):
        yield(i*i)

for num in squares(user_input1, user_input2):
    print(num)


#exercise 5
user_input = int(input())
def is_down(n):
    i = n
    while i != 0:
       i-=1
       yield i

for num in is_down(user_input):
    print(num)