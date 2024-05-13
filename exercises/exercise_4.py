# Exercise 4
# Your solution comes here
num = int(input("enter a four digit number"))
a = num // 10
b = num // 100

if num % 10 == num // 1000 and a % 10 == b % 10:
  print("1")
else:
  print("0")
