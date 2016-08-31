MENU = "R - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()

# if choice == R:
#     R()
# elif choice == C:
#     C()
# elif choice == A:
#     A()
# elif choice == M:
#     M()
# else
#     Q()

def A ():
    item_name = input("Item name: ")
    while item_name == "":
        print("Item cannot be blank")
        item_name = input("Item name: ")
    invalid_price = True
    while invalid_price:
        try:
            item_price = int(input("Price: $"))
        except ValueError:
            print("Invalid input; enter a valid number")
            item_price = int(input("Price: $"))
        except item_price == "":
            print("Price cannot be blank")
            item_price = int(input("Price: $"))
        except item_price < 0:
            print("Price must be >= $0")
            item_price = int(input("Price: $"))
        else:
            invalid_price = False
    invalid_priority = True
    while invalid_priority:
        try:
            item_priority = int(input("Priority: "))
        except ValueError:
            print("Invalid input; enter a valid number")
            item_priority = int(input("Priority: "))
        except item_priority < 1 or item_priority >3:
            print("Priority must be 1, 2 or 3")
            item_priority = int(input("Priority: "))
        except item_priority == "":
            print("Priority cannot be blank")
        else:
            invalid_priority = False
    new_item = ("{}, ${} ({}) added to shopping").format(item_name, item_price, item_priority)
    print(new_item)
    return new_item

A()