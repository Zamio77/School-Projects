"""
Create a funtion "max" that takes two
integers and returns the value that is
greater of the two

example max(7, 12)

Should return 12 is greater
"""

a = int(input("Please enter a number."))

b = int(input("Please enter a second number."))

while a == b:
    print("The numbers are equal. Please re-enter")
    a = int(input("Please enter a number."))
    b = int(input("Please enter a second number."))     

def max(a, b):
    if a > b:
        print(a, "is greater than", b)

    else:
        print(b, "is greater than", a)

    
max(a,b)

        
print("Doug Lamar")
