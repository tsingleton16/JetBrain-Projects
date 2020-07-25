import math

def annuity_monthly_payment(principal, periods, credit_interest):
    i = credit_interest / (12 * 100)
    add_one = i +1
    n = periods
    multiple = (i * add_one ** n) / (add_one ** n -1)
    A = principal * multiple
    return math.ceil(A)

def count_months(principal, monthly_payment, credit_interest):
    i = credit_interest / (12 * 100)
    add_one = i + 1
    bottom = monthly_payment - i * principal
    n = math.log(monthly_payment / bottom, add_one )
    return math.ceil(n)
   
def credit_principal(monthly_payment, periods, credit_interest):
    i = credit_interest / (12 * 100)
    n = periods
    add_one = i + 1
    bottom = (i * add_one ** n)  /  (add_one ** n - 1)
    return monthly_payment / bottom



    
    
# write your code here

print("""What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal""")
type_ = input()

if type_ == 'n':
    credit_principal = float(input('Enter credit principal: '))
    payment = float(input('Enter monthly payment: '))
    interest = float(input('Enter credit interest: '))
    num_of_months = count_months(credit_principal, payment, interest) 
    
    if num_of_months % 12 == 0:
        print(f'You need {num_of_months // 12} years to repay this credit!')
    elif num_of_months % 12 != 0 and num_of_months >= 12:
        print(f'You need {num_of_months // 12} years  and {num_of_months % 12} months to repay this credit!')
    else:
        print(f'You need {num_of_months // 12} months to repay this credit!')

    
elif type_ == 'a':
    credit_principal = float(input('Enter credit principal: '))
    num_of_periods = float(input('Enter count of periods: '))
    interest = float(input('Enter credit interest: '))
    print(f'Your annuity payment = {annuity_monthly_payment(credit_principal, num_of_periods, interest)}')
    
else:
    print('Enter monthly payment: ')
    payment = float(input('Enter monthly payment: '))
    num_of_periods = float(input('Enter count of periods: '))
    interest = float(input('Enter credit interest: '))
    print(f'Your credit principal = {credit_principal(payment, num_of_periods, interest)}!')
    


    
