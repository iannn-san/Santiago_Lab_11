numberof_words=0
words=[]
matchedwords=[]
while numberof_words<10:
    word=input("enter any word:")
    words.append(word)
    numberof_words+=1
num=int(input("to display the words under the same number of letters, enter any number of letters you want: "))
for i in words:
    if len(i)>=num:
        matchedwords.append(i)
print(matchedwords)