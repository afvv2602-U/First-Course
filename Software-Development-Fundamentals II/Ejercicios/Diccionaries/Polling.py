def main():
    print('Welcome to the Yes or No Issue Polling App')
    question = str(input('What is the yes or no issue you will be voting on today: '))
    voters = int(input('What is the number of voters will you allow on the issue: '))
    pasw = str(input('Enter the password for polling results: '))
    results = createPoll(question,voters)
    checkResults(question,results)
    if pasw == str(input('To see the voting results enter the admin password: ')):
        for k,v in results.items():
            print('%5s : %1s %4s : %1s'%('Voter',k,'Vote',v))
    else:
        print('Sorry, that is not the correct password. Goodbye...')
    print('Thank you for using the Yes or No issue Polling App')


def createPoll(question : str, voters : int):
    results = {}    
    for i in range(voters):
        name = str(input('Enter your full name: '))
        vote = str(input('Here is our issue: '+str(question)+'?\n What do you think... yes or no: ')).lower()
        if vote[0] == 'n':
            vote = 'No'
        else:
            vote = 'Yes'
        results[name] = vote
        print('Thank you '+str(name)+'! your vote of '+str(vote)+' has been recorded')
    return results

def checkResults(question,results : dict):
    conts = {'contY':0,'contN':0}
    print('The following '+str(len(results))+' people voted: ')
    for k,v in results.items():
        print(k)
    for k,v in results.items():
        if v == 'Yes':
            conts['contN']=1
        else:
            conts['contY']+=1
    if conts['contN'] > conts['contY']:
        print('On the following issue: '+str(question)+' No wins! '+str(conts['contN'])+' to '+str(conts['contY']))
    elif conts['contN'] < conts['contY']:
        print('On the following issue: '+str(question)+' Yes wins! '+str(conts['contY'])+' to '+str(conts['contN']))
    else:
        print('Tie both votes are equals')


if __name__ == '__main__':
    main()