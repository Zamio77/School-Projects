# A program that will read the numbers in steps.txt
# then provide the average per the month of the year.

def main():
    # Open the file
    step_file = open('steps.txt', 'r')

    for days in range(1, 32):
        daily_total = step_file.readline()
        monthly_total = 0
        monthly_total += int(daily_total)
        month_avg_jan = monthly_total/31

    for days in range(1, 29):
        daily_total = step_file.readline()
        monthly_total = 0
        monthly_total += int(daily_total)
        month_avg_feb = monthly_total/31

    # Close the file
    step_file.close()

    print("The average for January is ", format(month_avg_jan, '.2f'))
    print("The average for February is ", format(month_avg_feb, '.2f'))

# Call main function
main()
