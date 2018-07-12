#Input List
myList = ['Cat','Manhattan','Oncologist','That','Precipitation' ]

#Function to find the longest word in a given list
def longestWord(lst):
    longest_word = ""
    longest_length = 0

    for word in lst:
        if len(word)>longest_length:
            longest_word = word
            longest_length = len(word)
    return longest_word


print(longestWord(myList))
