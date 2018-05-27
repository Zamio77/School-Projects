#prompt user for factorial

number = int(input("Please enter a number."))

while number < 0:
    print("ERROR: You cannot enter a negative number.")
    number = int(input("Please enter a number."))

start = 1

for num in range(start, number + 1):
    start *= num


print("The factorial of your number is", start)

print("Doug Lamar")


    
    
