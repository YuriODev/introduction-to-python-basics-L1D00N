# Exercise 3
# Your solution comes here
num = int(input("how many seconds have passed"))
a = num // 216000
b = (num - (a * 216000)) // 60
c = (num - (a * 216000) - (b * 60))
print(f"{a}{':'}{b}{':'}{c}")
