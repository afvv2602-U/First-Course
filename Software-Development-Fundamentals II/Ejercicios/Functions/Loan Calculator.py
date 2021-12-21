def main():
    loan = get_loan_info()
    print('\n----Loan information after 0 months----\n')
    show_loan_info(loan)

def get_loan_info():
    loan = {}
    print('Welcome to the Loan Calculator App')
    loan['principal'] = float(input('Enter the loan amount: '))
    rate = float(input('Enter the interest rate: '))
    loan['rate'] = rate / 100
    loan['monthly payment'] = float(input('Enter the desired monthly payment amount: '))
    loan['money paid'] = 0
    return loan

def show_loan_info(loan):
    for k,v in loan.items():
        print(str(k)+' : '+str(v))
    collect_info(loan)

def collect_info(loan):
    print('\n----Loan information after 0 months----\n')
    loan['principal'] = loan.get('principal') * (loan.get('rate')/12)
    for k,v in loan.items():
        print(str(k)+' : '+str(v))

def make_monthly_payment(loan):
    if loan.get('principal') > 0 and loan.get('principal') - loan.get('monthly payment') > 0:
        loan['principal'] = loan.get('principal') - (loan.get('monthly payment'))
        loan['money paid'] +=  loan.get('monthly payment')
    elif loan.get('principal') == 0:
        print('Congratulations you have paid all the debt')
    else:
        loan['money paid'] +=  loan.get('principal')
        loan['principal'] = 0
            
if __name__ == "__main__":
    main()