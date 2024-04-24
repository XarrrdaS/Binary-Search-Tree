from BST.build_bst import build_bst

choice = input("Enter nr. of your choice: (1. Print, 2. Remove, 3. Delte, 4. Export, 5. Rebalance, 6. Exit)")

if choice == "1" or choice == "1.":
    print("Option Print selected")

elif choice == "2" or choice == "2.":
    print("Option Remove selected")

elif choice == "3" or choice == "3.":
    print("Option Delete selected")

elif choice == "4" or choice == "4.":
    print("Option Export selected")

elif choice == "5" or choice == "5.":
    print("Option Rebalance selected")

elif choice == "6" or choice == "6.":
    print("Option Exit selected")

else:
    print("Invalid choice")