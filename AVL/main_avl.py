from .create_tree import create_tree, pre_order, in_order, post_order
from .Operations.minmax import find_min, find_max
from .Operations.delete import delete
from .Operations.export import export
from .Operations.rebalance import rebalance
from .Operations.remove import remove

def main_func_avl():
    root = create_tree()
    
    while True:
        print("\n| 1 - Print | 2 - Remove | 3 - Delete | 4 - Export | 5 - Rebalance | 6 - Find Min/Max | 7 - Exit |")
        choice = input("action > ")
        
        if choice == '1':
            print("Pre-order sort:", pre_order(root))
            print("In-order sort:", in_order(root))
            print("Post-order sort:", post_order(root))
        
        elif choice == '2':
            root = remove(root)
        
        elif choice == '3':
            root = delete(root)
            print("Deleted tree successfully!")
        
        elif choice == '4':
            export(root)
        
        elif choice == '5':
            root = rebalance(root)
        
        elif choice == '6':
            min_value = find_min(root)
            max_value = find_max(root)
            print("Min value:", min_value)
            print("Max value:", max_value)
        
        elif choice == '7':
            return False
        else:
            print("Select a valid option!")
