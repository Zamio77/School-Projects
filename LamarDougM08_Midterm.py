"""
A program to take a users input
as a sentence. The program should
split the input into a list, capitalize
the first letter, and print out the
completed string with a period on the end.
"""

# Start the main function
def main():

    try:
        # Get the users input
        words = input("Please write out a sentence. ")

        # Create list variable for punctuation
        is_punct = False

        # Create the punctuation list
        punctuation = ['.', ',', ';', '!', '?']
        
        # Create variable for seperated punctuation
        separated_punctuation = ''
        
        # Seperate out the punctuation, if there is any
        for character in words:
            if character in punctuation:
                output_character = " %s" % character
            else:
                output_character = character
            separated_punctuation += output_character

        # Create a new list
        separated_words = separated_punctuation.split()
        
        # Capitalize the first element, but first test it's not a digit
        if separated_words[0].isalpha():
            separated_words[0] = separated_words[0].title()

        # Test for the punctuation
        if separated_words[-1] in punctuation:
            separated_words[-2:] = [''.join(separated_words[-2:])]
            is_punct = True
        
        # Rejoin the words back into a sentence.
        out_words = ' '.join(separated_words)

        # Get the number of words
        num_words = len(separated_words)
        
        # Print out the output
        if is_punct:
            print(out_words)
            print("There are", num_words, "words in the sentence")
        else:
            print(out_words + '.')
            print("There are", num_words, "words in the sentence")

    except Exception as err:
        print(err)

# Call the main function
main()
        

        
            
