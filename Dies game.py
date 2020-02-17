import random
def yes():
    y=int(input('enter a number'))
    r=random.randint(1,6)
    print(r)
    if y==r:
        print('you win')
    else:
        print('try again')
def no():
    print('game over')
def main():
    s=['yes','YES','Yes','Y','y']
    m=['NO','no','No','N','n']
    i=1
    while i<100:
        x=input('enter yes or no')
        if x in s:
            yes()
            i=i+1
        if x in m:
            no()
            break
            
main()
            
    
