def main():
    print('Welcome to the Code Breaker App')
    phrase = str(input('Enter a word or phrase to count the occurrence of each letter: '))
    letters = countPhrase(phrase)
    calculatePercentage(letters,phrase)
    sortDict(letters)

    #Second Ejectution
    phrase = str(input('Enter a word or phrase to count the occurrence of each letter: '))
    letters = countPhrase(phrase)
    calculatePercentage(letters,phrase)
    sortDict(letters)
    
def sortDict(letters : dict):
    print('Letters ordered from highest occurrence to lowest:')
    letters_ordered = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    for k,v in letters_ordered:
        print(k)

def countPhrase(phrase : str):
    letters = {}
    for i in range(len(phrase)):
        if phrase[i] in letters:
            letters[phrase[i]]+=1
        else:
            letters[phrase[i]] = 1
    return letters

def calculatePercentage(letters : dict, phrase : str):
    print('%s %s %s'%('Letter','Occurrence','Percentage'))
    for k,v in letters.items():
        calc = v/len(phrase)*100
        print('%5s %10s %2.2f'%(k,v,calc))

if __name__ == '__main__':
    main()