principal = float(input("What is the initial amount of investement?"))

interest = float(input("What is the annual interest rate?"))
interest_rate = interest / 100

compound = float(input("How many times during the year is the interest \
compounded?"))

years = float(input("How many years will the money be left in the \
account?"))

amount = principal * ((1 + (interest_rate / compound)) **
                      (compound * years))

print("Your amount at the end of ", years, " years is $", format(amount, ',.2f'),
      sep='')

print("Doug Lamar")
