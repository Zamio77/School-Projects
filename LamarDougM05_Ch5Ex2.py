STATE_TAX = 0.05
COUNTY_TAX = 0.025


def main():
    purchase = float(input("What is your purhase?"))

    state_sales = state_sales_tax(purchase)

    county_sales = county_sales_tax(purchase)

    total_tax = total_sales_tax(state_sales, county_sales)

    total = total_sale(purchase, total_tax)

    print("Hi, my name is Doug Lamar.")

    print('Your purchase is', purchase)

    print('The State tax on your purchase is', state_sales)

    print('The county tax on your purchase is', county_sales)

    print('Your total tax equals', total_tax)

    print('Your total, with tax, equals', total)

def state_sales_tax(purch):
    s_tax = STATE_TAX * purch
    return s_tax

def county_sales_tax(purchs):
    c_tax = COUNTY_TAX * purchs
    return c_tax

def total_sales_tax(tax1, tax2):
    t_tax = tax1 + tax2
    return t_tax

def total_sale(sale, tax):
    t_sale = sale + tax
    return t_sale

main()



