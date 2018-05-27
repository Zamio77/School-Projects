STATE_TAX = 0.05
COUNTY_TAX = 0.025


def main():
    purchase = float(input("What is your purhase?"))

    print("Hi, my name is Doug Lamar.")

    print('Your purchase is', purchase)

    state_sales = state_sales_tax(purchase)

    county_sales = county_sales_tax(purchase)

    total_tax = total_sales_tax(state_sales, county_sales)

    total = total_sale(purchase, total_tax)

    

def state_sales_tax(purch):
    s_tax = STATE_TAX * purch
    print('The State tax on your purchase is', s_tax)
    return s_tax

def county_sales_tax(purchs):
    c_tax = COUNTY_TAX * purchs
    print('The county tax on your purchase is', c_tax)
    return c_tax

def total_sales_tax(tax1, tax2):
    t_tax = tax1 + tax2
    print('Your total tax equals', t_tax)
    return t_tax

def total_sale(sale, tax):
    t_sale = sale + tax
    print('Your total, with tax, equals', t_sale)
    return t_sale

main()



