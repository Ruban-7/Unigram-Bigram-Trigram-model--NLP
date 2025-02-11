from collections import Counter

def probability(a, b,pairedWords, wordsCount, vocalSize):
    c = pairedWords.get((a,b),0) +1 
    d = wordsCount.get(a,0)+ vocalSize
    return c/d

def bigram(sentence):
    words = sentence.lower().split()
    return list(zip(words,words[1:]))

sentence = "The quick brown fox jumps over the lazy dog"
a= "fox"
b= "jumps"
words = sentence.lower().split()
wordsCount = Counter(words)
pairedWords= Counter(bigram(sentence))
vocalSize =len(wordsCount)

print(probability(a,b,pairedWords,wordsCount, vocalSize))




