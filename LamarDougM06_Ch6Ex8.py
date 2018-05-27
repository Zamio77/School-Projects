# A program to read the randoms.txt file
# count how many numbers are in the file and
# add them together and print the sum of the numbers

def main():

    # Open the file
    file = open('randoms.txt', 'r')

    # Create the total variable
    total = 0

    # Create the count variable
    count = 0
    
    # Start the loop
    for line in file:
        amount = int(line)
        # Add an amount to the counter
        count += 1
        # Add the amounts together for the sum
        total += amount

    # Close the file
    file.close()

    print("The total number of random numbers is ", count, sep='')
    print("The sum of the numbers is ", total, sep='')

# Call the main function
main()

