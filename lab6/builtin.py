import time
import math

#exercise 1
nums=input().split()
some_list=[int(num) for num in nums]
def pr(l):
    p=1
    for i in l:
        p=eval("p*i")
    return p
print("product is:", pr(some_list))



#exercise 2
mystr=input()
def c(s): 
    up=sum(1 for i in s if i.isupper())
    lo=sum(1 for k in s if k.islower())
    return up, lo
u, l=c(mystr)
print("Uc num:", u, "\nLC num:", l)



#exercise 3
somestr=input()
def p(s1):
    s2=s1[::-1]
    if s1==s2:
        print("palindrome")
    else:
        print("not palindrome")
p(somestr)



#exercise 4
num=int(input("enter num: "))
ms=int(input("enter ms: "))
s=ms/1000
time.sleep(s)

print(math.sqrt(num))


#exercise 5
mytup=tuple(input())
def my_func(t):
    return all(t)
print(my_func(mytup))