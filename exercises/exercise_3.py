# Exercise 3
# Your solution comes here
num = int(input("how many seconds have passed"))
a = (num // 3600) % 24
b = (num - (a * 3600)) // 60
c = (num - (a * 3600) - (b * 60))
print(f"{a}:{b:02d}:{c:02d}")
