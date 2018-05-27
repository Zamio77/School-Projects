# Read a file and sum the numbers in the file

def main():
    try:
        # Open the file
        file = open('numbers.txt', 'r')

        # create the sum variable
        total = 0

        # Read all the lines from the file
        for line in file:
            # Covert to the float
            amount = int(line)
            # Add each amount to the total
            total += amount

        # Close the file
        file.close()

        # Print the total
        print(total)

    except IOError as err:
        print(err)

    except ValueError as er:
        print(er)

    finally:
        # Close the file
        file.close()

# Call the main function
main()
