#  Exercise 2

print("Please enter one string:")

string = input()
length = len(string)

if length >= 2:
    output = string[0:2] + string[(length - 2):]
else:
    output = ""

print("The string made by the first two and last to chars is:", output)
