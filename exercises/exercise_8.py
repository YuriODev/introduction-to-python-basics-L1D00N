# Exercise 8
# Your solution comes here

a = int(input("enter your first number. "))
b = int(input("enter your second number. "))
c = int(input("enter your third number. "))

small = (a * (a < b and a < c)) + (b * (b < a or b < c)) + (c * (c < a and c < b))

big = (a * (a > b and a > c)) + (b * (b > a or b > c)) + (c * (c > a and c > b))

mid = a + b + c - small - big

print(small)
print(mid)
print(big)
