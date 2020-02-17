import random
def yes():
    print(random.randint(1,6))
def no():
    print('game over')
def main():
    s=['yes','YES','Yes','Y','y']
    m=['NO','no','No','N','n']
    i=1
    while i<5:
        x=input('enter yes or no')
        if x in s:
            yes()
            i=i+1
        if x in m:
            no()
            break
            
main()
            
    
