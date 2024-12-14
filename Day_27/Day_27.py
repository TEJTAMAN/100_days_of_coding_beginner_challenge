#Find the longest word in a sentence.

def find_longest_word(sentence):
    
    words = sentence.split()
    
    longest_word = max(words, key=len)
    
    return longest_word

sentence = input("Enter a sentence: ")
longest_word = find_longest_word(sentence)

print(f"The longest word is: {longest_word}")
