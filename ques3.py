

def binarySearch(list, left, right, e):
    if right >= left:
        mid = (left + right) // 2
        if list[mid] == e:
            return mid
        elif list[mid] > e:
            return binarySearch(list, left, mid - 1, e)
        else:
            return binarySearch(list, mid + 1, right, e)
    else:
        return -1

def selectionSort(list):
    list = list.copy()
    for i in range(len(list)):
        minimum = i
        for j in range(i + 1, len(list)):
            if list[minimum] > list[j]:
                minimum = j
        list[i], list[minimum] = list[minimum], list[i]
    return list


def main(): 
    print('''
         MENU
========================
  (1) Binary Search
  (2) Selection Sort
  (0) Exit
        ''')
    
    students = []
    r = int(input('Enter Number of Students: '))
    for i in range(1, r + 1, 1):
        name = input(f'Enter Name of Student {i}: ')
        students.append(name)
    while True:
        choice = int(input('Enter Choice: '))
        if choice == 1:
            name = input("Enter Name to Search: ")
            if (binarySearch((students), 0, r - 1, name) >= 0):
                print("Student Found in List")
            else:
                print("Student Not Found in List")
        elif choice == 2:
            print('Original List:', students)
            print('Sorted List:', selectionSort(students))
        elif choice == 0:
            break
        input('Press any key to continue...')


if __name__ == "__main__":
    main()
