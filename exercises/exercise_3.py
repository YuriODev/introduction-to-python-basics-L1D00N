# Exercise 3
# Your solution comes here
num = int(input("how many seconds have passed"))
a = num // 216000
b = (num - (a * 216000)) // 3600
c = (num - (a * 216000) - (b * 3600))
print(f"{a}:{b:02d}:{c:02d}")
