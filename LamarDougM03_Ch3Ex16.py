year = int(input("What is the year?"))

# Testing against the year 2100 as this year is not a leap year
# but it is divisble by both 100 and 4, but not 400.

if (year % 100 == 0):
    if (year % 400 == 0):
        print("In ", year, ", February had 29 days.", sep='')
    else:
        print("In ", year, ", February had 28 days.", sep='')

elif (year % 4 == 0):
    print("In ", year, ", February had 29 days.", sep='')

else:
    print("In ", year, ", February had 28 days.", sep='')


print("Doug Lamar")
