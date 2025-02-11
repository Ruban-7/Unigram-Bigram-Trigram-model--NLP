from collections import Counter

def probability(firstWord, secondWord,thirdWord,doublePairedWords, pairedWords, vocalSize):
    c = pairedWords.get((firstWord,secondWord,thirdWord),0) +1 
    d = doublePairedWords.get((firstWord,secondWord),0)+ vocalSize
    return c/d

def trigram(sentence):
    words = sentence.lower().split()
    return list(zip(words,words[1:],words[2:]))
def bigram(sentence):
    words = sentence.lower().split()
    return list(zip(words,words[1:]))

sentence = "The quick brown fox jumps over the lazy dog"
a= "the"
b= "quick"
probMax= 0
nextWord= None
words = sentence.lower().split()
doublePairedWords = Counter(bigram(sentence))
pairedWords= Counter(trigram(sentence))
vocalSize =len(set(words))
if a not in words:
    print(f"'{a}' is not in corpus")
elif b not in words:
    print(f"'{b}' is not in corpus")
else:
    for sen in words:
        probValue= probability(a,b,sen,doublePairedWords,pairedWords, vocalSize)
        if probValue > probMax:
            probMax = probValue
            nextWord = sen
if nextWord:
    print(f"The next word of '{a} && {b}' is '{nextWord}")

