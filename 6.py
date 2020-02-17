def username():
    
    x=input('enter the username:')
    m='@'
    s='.'
    val=True
    for i in range(len(x)):
        if(x[i]==m):
            n=i
            for j in range(len(x)):
                if(x[j]==s):
                    o=j
                    if(o>n):
                        return val
                    
def password():
    y=input('enter the password')
    s=['$','@','#','%','*','!']
    val=True
    if (len(y)<6 and len(y)>15):
        print('length should be 5-15 characters')
        val=False
    if not any(char.isdigit() for char in y):
        print('password should have at least one numerical')
        val=False
    if not any(char.islower() for char in y):
        print('password should have at least one lowercase')
        val=False
    if not any(char.isupper() for char in y):
        print('password should have at least one uppercase')
        val=False
    if not any(char in s for char in y):
        print('password should have at least one special character')
        val=False
    if val:
        return val
def main():
    
    
    if(username()):
        
        if(password()):
            print('valid username and password')
        else:
            print('invalid password')

    else:
        print('invalid username')
main()
    
                       
                        
