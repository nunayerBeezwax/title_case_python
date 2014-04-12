skipWords = set('a an the for and nor but or yet so at around by after along for from of on to with without in'.split())

def titleCase(string):
    strArray = string.split(' ')
    titleCaseArray = []

    for word in strArray:
        if titleCaseArray == []:
            titleCaseArray.append(word[0].upper() + word[1:])
        elif word not in skipWords:
            titleCaseArray.append(word[0].upper() + word[1:])
        else:
            titleCaseArray.append(word)

    lastWord = titleCaseArray.pop(-1)

    return ' '.join(titleCaseArray) + ' ' + lastWord[0].upper() + lastWord[1:]


while True:
    string = raw_input('Give me a sentence, I will show it to you in Title Case: ')
    print titleCase(string)

