# A program that will read the numbers in steps.txt
# then provide the average per the month of the year.

# Start the function.
def main():
    # Open the file
    step_file = open('steps.txt', 'r')

    # Create the monthly total variable
    monthly_total = 0
    # Start the loops. The .readline is the key for these
    # loops to work. The .readline saves the position
    # to the last place it was used. So, even though
    # we're restarting in a new loop, the .readline
    # starts in the position in the file where it was last used.
    # That's why the range can stay at (1, 32) for the
    # most part.
    for days in range(1, 32):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_jan = monthly_total/31

    for days in range(1, 29):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_feb = monthly_total/28

    for days in range(1, 32):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_mar = monthly_total/31

    for days in range(1, 31):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_apr = monthly_total/30

    for days in range(1, 32):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_may = monthly_total/31

    for days in range(1, 31):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_jun = monthly_total/30

    for days in range(1, 32):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_jul = monthly_total/31

    for days in range(1, 32):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_aug = monthly_total/31

    for days in range(1, 31):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_sep = monthly_total/30

    for days in range(1, 32):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_oct = monthly_total/31

    for days in range(1, 31):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_nov = monthly_total/30

    for days in range(1, 32):
        daily_total = step_file.readline()
        monthly_total += int(daily_total)
        month_avg_dec = monthly_total/31

        

    # Close the file
    step_file.close()

    print("The average for January is ", format(month_avg_jan, '.2f'))
    print("The average for February is ", format(month_avg_feb, '.2f'))
    print("The average for March is ", format(month_avg_mar, '.2f'))
    print("The average for April is ", format(month_avg_apr, '.2f'))
    print("The average for May is ", format(month_avg_may, '.2f'))
    print("The average for June is ", format(month_avg_jun, '.2f'))
    print("The average for July is ", format(month_avg_jul, '.2f'))
    print("The average for August is ", format(month_avg_aug, '.2f'))
    print("The average for September is ", format(month_avg_sep, '.2f'))
    print("The average for October is ", format(month_avg_oct, '.2f'))
    print("The average for November is ", format(month_avg_nov, '.2f'))
    print("The average for December is ", format(month_avg_dec, '.2f'))

# Call main function
main()
