# A program to generate a random number to
# a file

# Will need the random module to generate numbers

import random


def main():

    # Create the file
    file = open('randoms.txt', 'w')

    # See how many times the loop should run
    howMany = int(input('Enter the number of numbers you would' +
                       'like to generate: '))

    # Run the loop
    for i in range(howMany):
        number = random.randint(1, 501)
        file.write(str(number) + '\n')

    # Close the file
    file.close()

# Call the main function
main()
