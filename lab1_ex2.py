#  Exercise 2

print("Please enter one string:")

string = input()
length = len(string)

if length >= 2:
    output = string[0:2] + string[(length - 2):]
    """
    where can be replaced by:
    result = string[:2] + string[-2:]
    So if we don't have the start number, it will default as from the very beginning
    If we start from a minus number (e.g -2) it will output start from the tail of 
    the string 
    """
else:
    output = ""

print("The string made by the first two and last to chars is:", output)
