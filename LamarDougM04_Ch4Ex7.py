#Start the program with the starting point
start = 0.01


# Capture the number of days, and build the table
days = int(input('Enter the number of days: '))

while days < 0:
    print("ERROR: you cannot enter a negative number.")
    days = int(input('Enter the number of days: '))
    
print('Day\t\t', 'Salary')
print('-' * 25)

#begin the calculation
total = 0
for i in range(1, days + 1):
    salary = start * 2 ** (i -1)
    print(format(i, '3.0f'), '\t\t$', format(salary, '8.2f'), sep='')
    total += salary
print('The total pay at the end of the period is $', format(total, '.2f'),
      sep='')

    
print("Doug Lamar")
