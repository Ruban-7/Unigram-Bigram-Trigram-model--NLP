import nltk
nltk.download('brown')
from nltk.corpus import brown 
from collections import Counter
words= [word.lower() for word in brown.words()]
words_count = Counter(words)
Total_count = sum(words_count.values())
def unigram(word, words_count,Total_count):
    return words_count[word.lower()]/ Total_count
    
word = "for"
print(f"Probability of '{word}':",unigram(word, words_count,Total_count))



