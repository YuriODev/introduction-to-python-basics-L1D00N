# Exercise 11
# Your solution comes here
num = int(input("how many dollars do you have? "))
a = num // 500
b = (num - (a * 500)) // 100
c = (num - (a * 500) - (b * 100)) // 10
d = (num - (a * 500) - (b * 100) - (c * 10)) // 5
f = num - (a * 500) - (b * 100) - ( c * 10) - (d * 5)
print(a, "(500)", b, "(100)", c, "(10)", d, "(5)", f, "(1)")
