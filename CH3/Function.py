def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return 'It is decidedly so'
    else:
        return 'Very doubtful'


fortune = getAnswer(2)
print(fortune)