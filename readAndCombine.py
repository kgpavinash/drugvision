import nltk.data
from sentence_splitter import SentenceSplitter, split_text_into_sentences
from nltk.tokenize import sent_tokenize, word_tokenize
f = open(r"C:\Users\aprabhakar\Desktop\snakes\testDAT\notext\sometext.txt","r")
firstprocess = []
# for x in f:
#     print(x)

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
data = f.read()
result = ('\n------\n'.join(tokenizer.tokenize(data)))
# print(result)
# data = f.read()


# for e in firstprocess:
#     # print(e)
#     # print(e.index('\n'))
#     s = e.split()
#     print(s)
#     break
allSentences = []
data2 = data.split()
newWord = False
upperCaseWord = False
lowerCaseWord = False
currentSentence = ""
for e in data2:
    if e.isupper():
        upperCaseWord = True
        if lowerCaseWord is True:
            newWord = True
            allSentences.append(currentSentence)

        currentSentence = currentSentence + ' ' + e
    if e.islower():
        if upperCaseWord is True:
            newWord = True
            allSentences.append(currentSentence)
            currentSentence = ""
            currentSentence = currentSentence + ' ' + e
        elif '.' in e:
            currentSentence = currentSentence + ' ' + e
            allSentences.append(currentSentence)
            currentSentence = ""



print(currentSentence)


# if "\n" in result:
#     print("true")

# print(sent_tokenize(data))

# data = data.replace('\n', '')
# print(data)

# splitter = SentenceSplitter(language='en')
# print(splitter.split(text=data))
f.close()


