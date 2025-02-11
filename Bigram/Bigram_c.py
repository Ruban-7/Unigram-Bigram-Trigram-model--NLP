from collections import Counter

def probability(a, b,pairedWords, wordsCount, vocalSize):
    c = pairedWords.get((a,b),0) +1 
    d = wordsCount.get(a,0)+ vocalSize
    return c/d

def bigram(sentence):
    words = sentence.lower().split()
    return list(zip(words,words[1:]))

sentence = "The quick brown fox jumps over the lazy dog"
a= "the"
probMax= 0
nextWord= None
words = sentence.lower().split()
wordsCount = Counter(words)
pairedWords= Counter(bigram(sentence))
vocalSize =len(wordsCount)
if a not in wordsCount:
    print("Given words is not in corpus")
else:
    for sen in words:
        probValue= probability(a,sen,pairedWords,wordsCount, vocalSize)
        if probValue > probMax:
            probMax = probValue
            nextWord = sen 
if nextWord:
    print(f"The next word of '{a}' is '{nextWord}")






