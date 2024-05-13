# Exercise 7
# Your solution comes here
num = int(input("enter a 4 digit number. "))
a = num // 10
b = num // 100

print((a % 10) + (b % 10) + (num % 10) + (num // 1000))
