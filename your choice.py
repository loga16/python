print('options are [1 2 3 4 q]')
i=1
s=['1','2','3','4','q']
while i<5:
    x=input('enter your option')
    if x=='1':
        print('Go to the college')
        i=i+1
    if x=='2':
        print('Go to the movie')
        i=i+1
    if x=='3':
        print('Take rest')
        i=i+1
    if x=='4':
        print('Play game')
        i=i+1
    if x=='q':
        print('quit')
        break
    if x not in s:
        print('your choice is not in option')
        i=i+1
    
        
