#function
def first_function():
    print('First function')

def second_function():
    print('Second function')

def main():
    print('This is main')
    second_function()
    x = 5
    print('x is', x)
    first_function()

if __name__ == '__main__':
    main()

#other function
def first_function():
    print('First function')

def second_function(num):
    print('Second function prints the num parameter', num)

def third_function():
    return 3

def main():
    print('This is main')
    second_function(500)
    first_function()
    x = third_function()
    print('The third function returns',x)

if __name__ == '__main__':
    main()

#list example
days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
print(days)
print(len(days))
print(days[3])

day = input('What day is it? ')
while day not in days:
    day = input('Try again. What day is it? ')

print('Great! It is',day)

#sets
my_set = {'red','green','blue'}
second_set = {'blue','red','green'}
print(my_set == second_set)
my_set.add('yellow')
print(my_set == second_set)
print(my_set) 

#tuples
my_tuple = ('apple','banana','apple')
print(my_tuple[0])
print(my_tuple)

#dictionaries
my_dictionary = {
    'name': 'Sally',
    'age': 30,
    'car_owner': True
    }
print(my_dictionary['age'])
print(my_dictionary['name'])
print()
print(my_dictionary)
print()

car_1 = {
    'color':'red',
    'year':2010,
    'make':'Ford',
    'pre-owned':True
    }
car_2 = {
    'color':'blue',
    'year':2019,
    'make':'Toyota',
    'pre-owned':False
    }
cars = [car_1,car_2]
for car in cars:
    print(car['color']) 
