"""
A program to access the GirlNames.txt file
and the BoyNames.txt file, pull the names into
a list and allow the user to search for names.
"""

def main():

    try:

        # Open the Girl name file
        girls = open('GirlNames.txt', 'r')

        # Open the Boy name file
        boys = open('BoyNames.txt', 'r')

        # Create the lists for the two
        girl_names = girls.readlines()
        boy_names = boys.readlines()

        # Create the loop to fill the lists
        # Need to strip off the \n
        index1 = 0
        while index1 < len(girl_names):
            girl_names[index1] = girl_names[index1].rstrip('\n')
            index1 += 1

        index2 = 0
        while index2 < len(boy_names):
            boy_names[index2] = boy_names[index2].rstrip('\n')
            index2 += 1
           

        # Create the 'another' variable
        another = 'y'
        
        # Capture the user input, set loop to keep
        # capturing names
        while another == 'y' or another == 'Y':
            # Wanted to use capital letters to match the lists
            search = input("Enter a name you would like to search for: ")
            search = search.title()

            # Search for the name entered
            if search in girl_names:
                print(search, "is a popular girl name.")

            elif search in boy_names:
                print(search, "is a popular boy name.")

            else:
                print(search, "was not found in the list.")
        
            another = input("Would you like to check another name? 'Y' = yes ")

        # Close the files
        girls.close()
        boys.close()

    except Exception as err:
        print(err)

# Call the main function
main()
