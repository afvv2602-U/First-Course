
def main():
    users = ['afvv2602','randy','notorious','goofy','spray']
    name = str(input('Welcome to the Shipping Accounts Program\nHello, what is your username: ')).lower()
    #Check if name is in users
    if name in users:
        print('Shipping orders 0 to 100:\t\t$5.10 each')
        print('Shipping orders 100 to 500:\t\t$5.00 each')
        print('Shipping orders 500 to 1000:\t\t$4.95 each')
        print('Shipping orders over 1000:\t\t$4.80 each')
        items = int(input('How many items would you like to ship: '))
        shipping(items)
        if str(input('Would you like to place this order (y/n): ')).lower() == 'y':
            print('Okay. Shipping your '+str(items)+' items.')
        else:
            print('Okay, no order is being placed at this time.')
    else:
        print('Sorry, you do not have an account with us. Goodbye.')

#Simulate the shipping
def shipping(num):
    if num < 101:
        total = num*5.10
        print('To ship '+str(num)+' items it will cost you $'+str(total)+' at $5.10')
    elif num < 501:
        total = num*5.00
        print('To ship '+str(num)+' items it will cost you $'+str(total)+' at $5.00')
    elif num < 1001:
        total = num*4.95
        print('To ship '+str(num)+' items it will cost you $'+str(total)+' at $4.95')
    else:
        total = num*4.80
        print('To ship '+str(num)+' items it will cost you $'+str(total)+' at $4.80')

if __name__ == "__main__":
    main()