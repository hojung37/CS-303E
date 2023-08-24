#calling a function
def my_function():
    print('Hello World')
my_function()

#calling function example 
x = 10
print(x)
my_function()
print(x*2)
my_function() 

#return values
def is_winter(word):
    if(word.lower() == 'winter'):
        return True
    else:
        return False

season = input('What season is it? ')
if(is_winter(season)):
    print('It is winter')
else:
    print('It is not winter')
    
#main function
def main():
    season = input('What season is it? ')
    if(is_winter(season)):
        print('It is winter')
    else:
        print('It is not winter')
    print('this is the main function')

if __name__ == '__main__':
    main() 

#strings and indexes
def main():
    greeting = 'Hello'
    print(greeting[0])
    print(len(greeting))
    print(greeting[len(greeting) -1])
if __name__ == '__main__':
    main()

#more complex function
def has_cat(word):
    for i in range(0, len(word)):
        if(word[i] == 'c'and len(word)> i+2):
            if(word[i+1] == 'a'):
                if(word[i+2] == 't'):
                    return True
    return False
def main():
    cat_word = input('Enter a word ')
    print('Contains cat?',has_cat(cat_word))   
if __name__ == '__main__':
    main()

#another way
def has_cat(word):
    for i in range(0, len(word)):
        if(word[i] == 'c'and len(word)> i+2):
            if(word[i+1] == 'a'):
                if(word[i+2] == 't'):
                    return True
    return False
def main():
    cat_word = input('Enter a word ')
    if has_cat(cat_word):
        print('contains cat')
    else:
        print('does not contain cat')
if __name__ == '__main__':
  main()

#yet another string function using backwards
def has_cat(word):
    for i in range(0, len(word)):
        if(word[i] == 'c'and len(word)> i+2):
            if(word[i+1] == 'a'):
                if(word[i+2] == 't'):
                    return True
    return False
def reverse_print(word):
    for i in range(len(word)-1, -1, -1): #go backwards!
        print(word[i], end = '')
def main():
    new_word = input('Enter a word to reverse ')
    reverse_print(new_word)    
if __name__ == '__main__':
    main()

#a math function
def has_cat(word):
    for i in range(0, len(word)):
        if(word[i] == 'c'and len(word)> i+2):
            if(word[i+1] == 'a'):
                if(word[i+2] == 't'):
                    return True
    return False
def reverse_print(word):
    for i in range(len(word)-1, -1, -1): #go backwards!
        print(word[i], end = '')
def is_mult_of(num_1,num_2):
    if(num_1 % num_2 == 0):
        print(num_1,'is a multiple of',num_2)
    else:
        print(num_1,'is not a multiple of',num_2)
def main():
    is_mult_of(4,2)
if __name__ == '__main__':
    main()

#questioning if the word has cat & the reverse of it
def has_cat(word):
    for i in range(0, len(word)):
        if(word[i] == 'c'and len(word)> i+2):
            if(word[i+1] == 'a'):
                if(word[i+2] == 't'):
                    return True
    return False
def reverse_print(word):
    for i in range(len(word)-1, -1, -1): #go backwards!
        print(word[i], end = '')
def is_mult_of(num_1,num_2):
    if(num_1 % num_2 == 0):
        print(num_1,'is a multiple of',num_2)
    else:
        print(num_1,'is not a multiple of',num_2)
def main():
    user_word = input('enter a word')
    print(has_cat(user_word))
    reverse_print(user_word) 
if __name__ == '__main__':
    main()



