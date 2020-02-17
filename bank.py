a=0
w=0
d=0
def deposit(amt):
    print('deposited')
    global d
    if (w==0):
        d=amt+a
        print(d)
    elif (w!=0):
        
        d=amt+w
        print(d)
    
    
def withdraw(amt):
    print('withdrawed')
    global w
    w=d-amt
    print(w)
    
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
