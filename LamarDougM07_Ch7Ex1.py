"""
A program to take the sales for a week
and return the total.
"""
import math

def main():

    try:

        # Set days of week variable
        days_of_week = 7

        # Create the list
        sales = []



        # Create the loop.
        for day in range(days_of_week):
            print("Enter the sales for day ", day + 1,
                  ':', sep='', end='')
            sale = float(input())
            sales.append(sale)
            
        total = sum(sales)

        print("The sales for the week are", sales)
        print("The total sales for the week are", total)

    except ValueError:
        print("Please enter a number for the sales for the day")

main()
