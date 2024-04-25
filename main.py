from BST.main_bst import main_func_bst
from AVL.main_avl import main_func_avl

if __name__ == "__main__":
    while True:
        print('\n\n| 1 - BST | 2 - AVL | 3 - Exit |\n')
        choice = input('Select an option you would like to take action with: ')
        if choice == '1':
            main_func_bst()
        elif choice == '2':
            main_func_avl()
        elif choice == '3':
            break
        else:
            print("Select a valid option!\n")
