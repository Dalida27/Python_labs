import math

#exercise 1
class someClass():
  def getString(param):
    param.variable = input()

  def printString(param):
    print(param.variable.upper())

object = someClass()
object.getString()
object.printString()

#exercise 2
class Shape:
  def __init__(self):
    pass

  def area(self):
    return 0
    
class Square(Shape):
  def __init__(self, length):
    super().__init__()
    self.length=length

  def area(self):
    return self.length**2

user_input = int(input())
square = Square(user_input)
print(square.area())

shape=Shape()
print(shape.area())


#exercise 3
class Shape:
  def __init__(self):
    pass    

class Rectangle(Shape):
  def __init__(self, length, width):
    super().__init__()
    self.length=length
    self.width=width

  def area(self):
    return self.length*self.width

length_input=int(input())
width_input=int(input())
rect=Rectangle(length_input, width_input)

print(rect.area())


#exercise 4
class Point:
  def __init__(self, x, y):
    self.x=x
    self.y=y

  def show(self):
    return f"({self.x}, {self.y})"
  def move(self, newx, newy):
    self.x=newx
    self.y=newy
    
  def dist(self, x1, x2, y1, y2):
    self.d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return self.d
    

x1=int(input("enter x:"))
y1=int(input("enter y:"))
p1=Point(x1, y1)

print(p1.show())

x2=int(input("enter x2: "))
y2=int(input("enter y2: "))

p1.move(x2, y2)

print(p1.show())

x3=int(input("enter x of the 1 point: "))
y3=int(input("enter y of the 1 point: "))

x4=int(input("enter x of the 2 point: "))
y4=int(input("enter y of the 2 point: "))

print(p1.dist(x3, x4, y3, y4))


#exercise 5
class BankAccount:
  def __init__(self, owner, balance):
    self.owner=owner
    self.balance=balance
    
  def deposit(self, deposit_value):
    self.balance=self.balance+deposit_value
    return str(self.owner)+str(self.balance)

  def withdraw(self, withdraw_value):
    self.balance=self.balance-withdraw_value

    if self.balance<0:
      self.balance=self.balance+withdraw_value

    return str(self.owner)+str(self.balance)

ba1_owner=input("enter owner 1 account: ")
ba1_balance=float(input("enter balance 1 account: "))

ba1=BankAccount(ba1_owner, ba1_balance)

ba2_owner=input("enter owner 2 account: ")
ba2_balance=float(input("enter balance 2 account: "))

ba2=BankAccount(ba2_owner, ba2_balance)

ba3_owner=input("enter the owner 3 account: ")
ba3_balance=float(input("enter balance 3 account: "))

ba3=BankAccount(ba3_owner, ba3_balance)

print(ba1.deposit(200))
print(ba1.withdraw(1000))

print(ba2.deposit(3000))
print(ba2.withdraw(500))

print(ba3.deposit(10))
print(ba3.withdraw(0))          


#exercise 6
nums=input().split()
some_list=[int(x) for x in nums]
def isPrime(x):
  if x<2:
    return False
  for i in range(2, x):
    if x%i==0:
      return False
  return True

primes=filter(lambda n:isPrime(n), some_list)
print(list(primes))