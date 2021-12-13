word=input("enter your introduction ")
charactercount=0
wordcount=1
for i in word:
    charactercount+=1
    if (i==" "):
        wordcount+=1
print(charactercount)
print(wordcount)