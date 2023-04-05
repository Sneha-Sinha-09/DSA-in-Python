#Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.
#Rules: The word should have the largest frequency. In case multiple words have the same frequency, then choose the word that has the maximum length.
#Assumptions: The text has no special characters other than space. The text would beign with a word and there will be only a single space between the words. Perform case insensitivity string comparisions wherever necessary.

def find_most_frequent_word(text):
    
    words = text.lower().split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    max_frequency = 0
    max_word = ''
    for word, freq in frequency.items():
        if freq > max_frequency:
            max_frequency = freq
            max_word = word
        elif freq == max_frequency:
            if len(word) > len(max_word):
                max_word = word

    return max_word + ' ' + str(max_frequency)

text = ('Betty bought a bit of butter but the bit of butter was a little bitter so Betty bought a bit of better butter to make the bitter butter better.')
print(find_most_frequent_word(text))  
