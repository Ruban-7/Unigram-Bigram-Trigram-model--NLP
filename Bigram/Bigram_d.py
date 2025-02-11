from collections import Counter
import nltk
from nltk.corpus import brown  # Correct import for brown corpus
nltk.download("brown")

def probability(a, b, pairedWords, wordsCount, vocalSize):
    c = pairedWords.get((a, b), 0) + 1
    d = wordsCount.get(a, 0) + vocalSize
    return c / d

def bigram(sentence):
    words = sentence.lower().split()
    return list(zip(words, words[1:]))

def predictSentence(start_word, pairedWords, wordsCount, vocalSize, length=5):
    sentence = [start_word]
    
    for _ in range(length):
        current_word = sentence[-1]
        max_prob = 0
        next_word = None
        for (w1, w2) in pairedWords.keys():
            if w1 == current_word:
                prob = probability(w1, w2, pairedWords, wordsCount, vocalSize)
                if prob > max_prob:
                    max_prob = prob
                    next_word = w2
        sentence.append(next_word)
    return " ".join(sentence)

# Use the first few sentences from the brown corpus
sentences = brown.sents()[:5]
words = [word.lower() for sentence in sentences for word in sentence]
wordsCount = Counter(words)
pairedWords = Counter(bigram(' '.join([word for sentence in sentences for word in sentence])))
vocalSize = len(wordsCount)

# Example output for a sentence starting with "the"
print(predictSentence("the", pairedWords, wordsCount, vocalSize, length=8))
