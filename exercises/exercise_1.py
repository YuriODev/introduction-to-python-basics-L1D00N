# Exercise 1
num = int(input("put in a five digit number"))
a = num // 10
b = num // 100
c = num // 1000
print("the total is ", a % 10 + b % 10 + c % 10 + num // 10000 + num % 10)
