#Reverse words in a sentence.

def reverse_words(sentence):
    words = sentence.split()  
    reversed_words = words[::-1]  
    return ' '.join(reversed_words)  

# Get input from the user
sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(sentence)
print("Reversed sentence:", reversed_sentence)
