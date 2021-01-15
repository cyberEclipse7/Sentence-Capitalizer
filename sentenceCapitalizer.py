# Problem 3: Sentence Capitalizer

# sentenceCapitalizer(string) returns a copy of the string with the first character of each sentence capitalized.
def sentenceCapitalizer(string):

    # Seperate each word in the sentence, and store them in the list as an separate element.
    list = string.split()

    capitalizedSentence = ""
    capitalizeTheWord = False
    isFirstWord = True

    # Loop through the list.
    for word in list:

        # Example: hello. my name is Ameen. how are you?

        # Capitalizing the first word.
        if isFirstWord == True:
            temp = word
            temp = temp.capitalize()
            capitalizedSentence = capitalizedSentence + temp + " "
            isFirstWord == False
            continue

        # Capitalize the word if there has been a full stop before.
        if capitalizeTheWord == True:
            temp = word
            temp = temp.capitalize()
            capitalizeTheWord = False
            capitalizedSentence = capitalizedSentence + temp + " "
            continue

        capitalizedSentence = capitalizedSentence + word + " "

        for character in word:
            if character == '.':
                capitalizeTheWord = True

    # Print the capitalized string.
    print(capitalizedSentence)

    # Returns a copy of the string with the first character of each sentence capitalized.
    return capitalizedSentence


def main():

    new_sentence = input("\nEnter a string for the program to capitalize sentences: ")
    sentenceCapitalizer(new_sentence)

# Call the main function.
main()
