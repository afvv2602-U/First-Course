def main():
    print('Welcome to the Database Admin Program')
    users = {'admin00':'12345678','admin01':'12345678','admin02':'12345678','admin03':'12345678','admin04':'12345678'}
    user = str(input('Enter your username: '))
    pasw = str(input('Enter your password: '))
    if user == 'admin00' and pasw == users[user]:
        print('Hello '+str(user)+'! You are logged in!\n')
        print('Here is the current user datebase: ')
        for k,v in users.items():
            print('%8s : %8s \t %8s : %8s '%('Username',k,'Password',v))
    elif user in users.keys() and pasw == users[user]:
        print('Hello '+str(user)+'! You are logged in!\n')
        ch = str(input('Would you like your to change your password: y/n')).lower()
        if ch[0] == 'y':
            while True:
                newPass = str(input('What would you like your new password to be: '))
                if len(newPass) > 7:
                    users[user] = newPass
                    print(str(user)+' your new password is '+str(newPass))
                    break
        else:
            print('Goodbye')
    elif user in users.keys() and pasw != users[user]:
        print('Password incorrect!')
    else:
        print('User not in database, goodbye.')

if __name__ == '__main__':
    main()