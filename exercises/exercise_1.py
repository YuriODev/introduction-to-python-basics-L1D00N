# Exercise 1
num = int(input("put in a five digit number: "))
a = num // 10
b = num // 100
c = num // 1000
print(f"{num % 10 + num // 10000 + b % 10}{a % 10 + c % 10}")
