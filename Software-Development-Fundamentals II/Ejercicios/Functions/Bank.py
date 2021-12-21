def main():
    wallet = {}
    wallet = get_info()
    while True:
        display_info(wallet)
        accType = str(input('What would you like to access (Savings or Checking): ')).capitalize()
        op = str(input('What type of transaction would you like to make (Deposit or Withdrawal): '))
        money = float(input('How much money: '))
        if op.capitalize() == 'Deposit':
            make_deposit(wallet,accType,money)
        elif op.capitalize() == 'Withdrawal':
            make_withdrawal(wallet,accType,money)
        op = str(input('Would you like to make another transaction (y/n): '))
        if op.capitalize() == 'N':
            print('Thank you. Have a great day!')
            break
        else:
            pass
            

def get_info():
    print('Welcome')
    name = str(input('Hello, what is your name: '))
    savingAccount = float(input('How much money would you like to set up your saving account with: '))
    checkigAccount = float(input('How much money would you like to set up your checking account with: '))
    wallet = {'name':name,'Savings':savingAccount,'Checking':checkigAccount}
    return wallet

def make_deposit(wallet,accType,deposit):
    wallet.update({accType:deposit})
    print('Deposited '+str(deposit)+' into '+str(wallet.get('name'))+' '+str(accType)+' account\n')

def make_withdrawal(wallet,accType,withDraw):
    saves = wallet.get(accType)
    if (saves - withDraw) < 0:
        print('The update can not be done\n')
    else:
        wallet.update({accType:(saves-withDraw)})
        print('Withdrew '+str(withDraw)+' into '+str(wallet.get('name'))+' '+str(accType)+ ' account\n')

def display_info(wallet):
    print('Current Account Information: ')
    for x in wallet:
        print(str(x)+' : '+str(wallet.get(x)))

if __name__ == "__main__":
    main()