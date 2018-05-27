quantity = int(input("How much will you be purchasing?"))

retailPrice = 99


if quantity < 10:
    discount = 0

elif quantity >= 10 and quantity <= 19:
    discount = 0.10

elif quantity >= 20 and quantity <= 49:
    discount = 0.20

elif quantity >= 50 and quantity <= 99:
    discount = 0.30

else:
    discount = 0.40


subTotal = retailPrice * quantity

totalDiscount = subTotal * discount

totalAmount = subTotal - totalDiscount

print("You received a discount of $", format(totalDiscount, '.2f'), ", and \
your total today is $", format(totalAmount, '.2f'), sep='')

print("Doug Lamar")
