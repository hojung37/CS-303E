#bubble sort
def bubble_sort(sorting_list):
    n = len(sorting_list)

    for i in range(n):
        for j in range(n-i-1): #since we're not including the top number
            if sorting_list[j] > sorting_list[j+1]: #compare the item to its right
                temp = sorting_list[j]
                sorting_list[j] = sorting_list[j+1]
                sorting_list[j+1] = temp 

    return sorting_list

def main():
    my_list = [4,3,6,7,2,3]
    print(bubble_sort(my_list)) 

if __name__ == "__main__":
    main() 

#easier way to swap 
def bubble_sort(sorting_list):
    n = len(sorting_list)

    for i in range(n):
        for j in range(n-i-1): 
            if sorting_list[j] > sorting_list[j+1]:
                sorting_list[j],sorting_list[j+1] = sorting_list[j+1],sorting_list[j]

    return sorting_list

def main():
    my_list = [4,3,6,7,2,3]
    print(bubble_sort(my_list)) 

if __name__ == "__main__":
    main() 

#adding boolean value
def bubble_sort(sorting_list):
    n = len(sorting_list)
    already_sorted = True

    for i in range(n):
        for j in range(n-i-1): 
            if sorting_list[j] > sorting_list[j+1]:
                sorting_list[j],sorting_list[j+1] = sorting_list[j+1],sorting_list[j]
                already_sorted = False
        if already_sorted:
            break

    return sorting_list

def main():
    my_list = [4,3,6,7,2,3]
    print(bubble_sort(my_list)) 

if __name__ == "__main__":
    main()

#binary search implementation
def bubble_sort(sorting_list):
    n = len(sorting_list)
    already_sorted = True

    for i in range(n):
        for j in range(n-i-1): 
            if sorting_list[j] > sorting_list[j+1]:
                sorting_list[j],sorting_list[j+1] = sorting_list[j+1],sorting_list[j]
                already_sorted = False
        if already_sorted:
            break

    return sorting_list

def binary_search(searching_list,x):
    low = 0
    high = len(searching_list)-1
    mid = 0

    while low <= high:
        mid  = (high+low) // 2 #// is quick round down to a whole number

        if searching_list[mid] < x: #if my value is bigger than the middle value
            low = mid + 1 # cut in half
        elif searching_list[mid] > x:
            high = mid - 1 #cut other half
        else:
            return mid #if not bigger or smaller, it's the middle value so return mid
        
    return -1 #if the value was never found in the list 

                  
def main():
    my_list = [4,3,6,7,2,3]
    print(bubble_sort(my_list))
    print('Index:',binary_search(my_list,6)) 

if __name__ == "__main__":
    main()

