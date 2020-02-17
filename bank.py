a=0
w=0
def deposit(amt):
    print('deposited')
    global d
    d=amt+a
    print('now your balance is:',d)
    
def withdraw(amt):
    print('withdrawed')
    w=d-amt
    print('now your balance is:',w)
    
def main():
    print(' To Deposit enter 1')
    print(' To withdraw enter 2')
    i=1
    while i<100:
        x=int(input('enter the your option'))
        amt=int(input('enter the amount'))
        if x==1:
            deposit(amt)
            i=i+1
        if x==2:
            withdraw(amt)
            i=i+1
        

main()
