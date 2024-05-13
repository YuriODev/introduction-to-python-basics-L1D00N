# Exercise 10
# Your solution comes here
num = float(input("how much degrees has the hour hand passed today"))
a = num // 30
num = num - (30 * a)
num = num * 12
print(num)
