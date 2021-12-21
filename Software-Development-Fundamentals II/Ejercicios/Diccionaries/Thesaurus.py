from os import sep
from random import randint

def main():
    thesaurus = {"hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']}
    print('Welcome to the Thesaurus App!')
    print('Here are the words in thesaurus: ')
    #Display keys in the dict
    for k,v in thesaurus.items():
        print('-'+str(k))
    word = str(input('What word would you like to synonym for: ')).lower()
    if word in thesaurus.keys():
        #Get a random word in synonyms
        print('A synonym for '+str(word)+' is : '+str(thesaurus[word][randint(0,len(thesaurus[word])-1)]))
    ch = str(input('Would you like to see the whole Thesaurus: y/n ')).lower()
    if ch[0] == 'y':
        for k,v in thesaurus.items():
            print('\n')
            print(str(k)+' Synonyms are: ')
            print(*v,sep='\n')
    else:
        print('I hope you enjoyed the program. Thank you!')    


if __name__ =='__main__':
    main()

