#Write a function to convert a list of words into a sentence.

def list_to_sentence(words):
    
    if not words:
        return ""
    
   
    sentence = " ".join(words).capitalize()
    
   
    if not sentence.endswith("."):
        sentence += "."
    
    return sentence

#EXAMPLE
words = ["this", "is", "a", "list", "of", "words"]
sentence = list_to_sentence(words)
print(sentence)  