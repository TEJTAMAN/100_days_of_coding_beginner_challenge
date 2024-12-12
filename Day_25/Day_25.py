#Write a function to count the frequency of words in a sentence.

def count_word_frequency(sentence):
   
    import string
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator).lower()
    
    
    words = sentence.split()
    
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    return word_frequency

# EXAMPLE
sentence = "This is a test. This test is only a test."
print(count_word_frequency(sentence))
