from collections import Counter
import nltk
from nltk.corpus import brown  # Correct import for brown corpus
nltk.download("brown")

def probability(firstWord, secondWord, thirdWord, doublePairedWords, pairedWords, vocalSize):
    c = pairedWords.get((firstWord, secondWord, thirdWord), 0) + 1  # Corrected access for trigram
    d = doublePairedWords.get((firstWord, secondWord), 0) + vocalSize  # Corrected access for bigram
    return c / d

def trigram(sentence):
    words = sentence.lower().split()
    return list(zip(words, words[1:], words[2:]))

def bigram(sentence):
    words = sentence.lower().split()
    return list(zip(words, words[1:]))

def predictSentence(start_word, doublePairedWords, pairedWords, vocalSize, length=5):
    sentence = [start_word]  
    
    for _ in range(length): 
        current_word = sentence[-1]  
        max_prob = 0
        next_word = None
        for (w1, w2, w3) in pairedWords.keys():
            if w1 == current_word:  
                prob = probability(w1, w2, w3, doublePairedWords, pairedWords, vocalSize)
                if prob > max_prob:  
                    max_prob = prob
                    next_word = w2
                   
        if next_word is None:
            break
        sentence.append(next_word)
 
    return " ".join(sentence)

# Correctly access sentences from the Brown corpus
sentence = ' '.join(brown.sents()[0])  # Example sentence from the Brown corpus
words = sentence.lower().split()
doublePairedWords = Counter(bigram(sentence))
pairedWords = Counter(trigram(sentence))
vocalSize = len(set(words))
print(predictSentence("the", doublePairedWords, pairedWords, vocalSize, length=8))
