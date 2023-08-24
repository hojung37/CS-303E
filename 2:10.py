x = 100
if(x%2 == 0):
    print('x is even')
else:
    print('odd')
    
x = 8
if(x%3 == 0):
    print('multiple of 3')
else:
    print('not a multiple of 3') 

i = 0
while(i < 10):
    i+=1
    print(i)
print('Done')

gas_tank = 5
while(gas_tank > 0): 
    gas_tank = gas_tank - 0.5
    print(gas_tank) 
print('Out of gas')

x = input('Is it winter? [yes or no] ')
while (x != 'yes' and x != 'no'):
    print('that is not a valid input. ')
    x = input('Is it winter? [yes or no] ')
print('Your answer was', x) 


x = input('Is it winter? [Yes or No] ')
x = x.lower() 
while (x != 'yes' and x != 'no'):
    print('that is not a valid input. ')
    x = input('Is it winter? [Yes or No] ')
print('Your answer was', x)

for x in range (10):
    print(x) 

    
