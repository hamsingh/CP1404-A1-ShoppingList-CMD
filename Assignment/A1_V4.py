__author__ = 'Harmon Singh'

MENU = "R - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()

import csv


def load_items():
    lines = []
    with open('items.csv', 'r', newline='') as f:
        for line in f.readlines():
            l = line.strip().split(',')
            l[2] = int(l[2])
            l[1] = float(l[1])
            lines.append(l)
        lines.sort()
    return lines

items = load_items()
number_items = (len(items))

def file_write(item_name,item_price,item_priority,item_status):
    import csv
    fields = [item_name,item_price,item_priority,item_status]
    with open(('items.csv', 'a'), lineterminator=('\n')) as file:
        writer = csv.writer(file)
        writer.writerow(fields)
    file.close()

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
        except item_price == "":
            print("Price cannot be blank")
        except item_price < 0:
            print("Price must be >= $0")
        else:
            invalid_price = False
    invalid_priority = True
    while invalid_priority:
        try:
            item_priority = int(input("Priority: "))
        except ValueError:
            print("Invalid input; enter a valid number")
        except item_priority < 1 or item_priority > 3:
            print("Priority must be 1, 2 or 3")
        except item_priority == "":
            print("Priority cannot be blank")
        else:
            invalid_priority = False
    item_status = "r"
    new_item = "{}, ${} ({}) added to shopping".format(item_name, item_price, item_priority)
    print(new_item)
    return item_name
    return item_price
    return item_priority
    return item_status
    file_write(item_name,item_price,item_priority,item_status)

def R (number_items, items):
    print("Required items:")
    total_price = 0
    item_number = -1
    for row in items:
        total_price += row[1]
        item_number += 1
        if "r" in row[3]:
            print("{}. {:22} $  {:.2f} ({})".format(item_number, row[0], row[1], row[2]))
    print("Total expected price for {} items: ${}".format(number_items, total_price))

def C (items):
    print("Completed items:")
    total_price = 0
    item_number = -1
    for row in items:
        total_price += row[1]
        item_number += 1
        if "c" in row[3]:
            print("{}. {:22} $  {:.2f} ({})".format(item_number, row[0], row[1], row[2]))
    print("Total spend for {} items purchasd: ${}".format(number_items, total_price))

def M ():
    print("Required items:")
    total_price = 0
    item_number = -1
    for row in items:
        total_price += row[1]
        item_number += 1
        if "r" in row[3]:
            print("{}. {:22} $  {:.2f} ({})".format(item_number, row[0], row[1], row[2]))
    print("Total spend for {} items purchasd: ${}".format(number_items, total_price))
    invalid_choice = True
    while invalid_choice:
        try:
            change_item = input("Enter the number of an item to mark as completed")
        except ValueError:
            print("Invalid input; enter a valid number")
        except change_item < 0:
            print("Invalid input; enter a valid number")
        except change_item == "":
            print("Invalid input; enter a valid number")
        else:
            invalid_choice = False

while choice != "Q":
    if choice == "R":
        R(number_items, items)
    elif choice == "C":
        C()
    elif choice == "A":
        A()
    elif choice == "M":
        M()
    else:
        print("Invalid Option")
    print(MENU)
    choice = input(">>> ").upper()