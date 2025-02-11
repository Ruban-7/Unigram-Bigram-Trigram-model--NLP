from collections import Counter

def probability(a, b,c,doublePairedWords, words, vocalSize):
    c = pairedWords.get((a,b,c),0) +1 
    d = doublePairedWords.get((a,b),0)+ vocalSize
    return c/d

def trigram(sentence):
    words = sentence.lower().split()
    return list(zip(words,words[1:],words[2:]))
def bigram(sentence):
    words = sentence.lower().split()
    return list(zip(words,words[1:]))

sentence = "The quick brown fox jumps over the lazy dog"
a= "fox"
b= "jumps"
c= "over"
words = sentence.lower().split()
doublePairedWords = Counter(bigram(sentence))
pairedWords= Counter(trigram(sentence))
vocalSize =len(set(words))

print(probability(a,b,c,doublePairedWords,pairedWords, vocalSize))