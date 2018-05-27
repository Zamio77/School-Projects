"""
A program to read the test.txt file
and find the number uppercase letters,
lowercase letters, digits, and whitespace
characters. Then, print out the numbers.
"""

def main():
    try:

        # Open the file
        test = open('test.txt', 'r')

        # Read the file
        tests = test.read()

        # Set count variables
        count_upp = 0
        count_low = 0
        count_dig = 0
        count_spa = 0

        # Start the loop
        for i in tests:
            if i.isupper():
                count_upp += 1
            elif i.islower():
                count_low += 1
            elif i.isdigit():
                count_dig += 1
            elif i.isspace():
                count_spa += 1

        # Print the output
        print("There are", count_upp, "uppercase letters.")
        print("There are", count_low, "lowercase letters.")
        print("There are", count_dig, "digits")
        print("There are", count_spa, "spaces.")

        # Close the file
        test.close()

    except Exception as err:
        print(err)

# Call the main function
main()
