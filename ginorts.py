word= input('')

capsList=[]
nonCapsList=[]
oddNumList=[]
evenNumList=[]

for digit in word:
    if digit.isupper():
        capsList.append(digit)
    elif digit.islower():
        nonCapsList.append(digit)
    elif digit.isdigit():
        if int(digit)%2==0:
            evenNumList.append(digit)
        else:
            oddNumList.append(digit)

allList=[nonCapsList,capsList,oddNumList, evenNumList]
wordList=[]

for digList in allList:
    digWord=''.join(sorted(digList))
    wordList.append(digWord)

sortedWord=''.join(wordList)
print(sortedWord)
