purchase = float(input("What is your purhase?"))            # Prefer float() because it will accept all numbers versu int() will only take whole numbers, not -10 or 2.75
state_sales_tax = 0.05 * purchase
county_sales_tax = 0.025 * purchase
total_sales_tax = state_sales_tax + county_sales_tax
total_sale = purchase + total_sales_tax

print("Hi, my name is Doug Lamar.")

print('Your purchase is', purchase)

print('The State tax on your purchase is', state_sales_tax)

print('The county tax on your purchase is', county_sales_tax)

print('Your total tax equals', total_sales_tax)

print('Your total, with tax, equals', total_sale)

