__author__ = 'Harmon Singh'
COMPLETED = "c"
REQUIRED = "r"

import csv


def load_items():
    item_list = []
    with open('items.csv', 'r', newline='') as f:
        for line in f.readlines():
            line = line.strip().split(',')
            line[2] = int(line[2])
            line[1] = float(line[1])
            item_list.append(line)
        item_list.sort()
    return item_list


def write_items(item_list):
    write_changes = csv.writer(open("items.csv", 'w', newline=''))
    for line in item_list:
        write_changes.writerow(line)


def add_item(item_list):
    item_name = get_item_name()
    item_price = get_item_price()
    item_priority = get_item_priority()
    item_list.append([item_name, item_price, item_priority, 'r'])
    print("{}, ${} ({}) added to shopping".format(item_name, item_price, item_priority))


def get_item_name():
    item_name = input("Item name: ")
    while item_name == "":
        print("Item cannot be blank")
        item_name = input("Item name: ")
    return item_name


def get_item_price():
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
    return item_price


def get_item_priority():
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
    return item_priority


def required_items(items):
    print("Required items:")
    total_price = 0
    i = 0
    for row in items:
        if REQUIRED in row[3]:
            total_price += row[1]
            print("{}. {:22} $  {:.2f} ({})".format(i, row[0], row[1], row[2]))
            i += 1
    if i == 0:
        print("No required items")
    else:
        print("Total expected price for {} items: ${}".format(i, total_price))


def completed_items(items):
    print("Completed items:")
    total_price = 0
    i = 0
    for row in items:
        if COMPLETED in row[3]:
            total_price += row[1]
            print("{}. {:22} $  {:.2f} ({})".format(i, row[0], row[1], row[2]))
            i += 1
    if i == 0:
        print("No completed items")
    else:
        print("Total expected price for {} items purchased: ${}".format(i, total_price))


def mark_item(items):
    print("Required items:")
    total_price = 0
    i = 0
    for row in items:
        if REQUIRED in row[3]:
            total_price += row[1]
            print("{}. {:22} $  {:.2f} ({})".format(i, row[0], row[1], row[2]))
            i += 1
    if i == 0:
        print("No required items")

    invalid_choice = True
    while invalid_choice:
        try:
            change_item = int(input("Enter the number of an item to mark as completed"))
        except ValueError:
            print("Invalid input; enter a valid number")
        except change_item < 0:
            print("Invalid input; enter a valid number")
        except change_item == "":
            print("Invalid input; enter a valid number")
        except change_item > len(items):
            print("Item does not exist")
        else:
            invalid_choice = False
    items[change_item][3] = COMPLETED


def main():
    items = load_items()
    number_of_items = len(items)
    MENU = "R - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            required_items(items)
        elif choice == "C":
            completed_items(items)
        elif choice == "A":
            add_item(items)
        elif choice == "M":
            mark_item(items)
        else:
            print("Invalid Option")
        print(MENU)
        choice = input(">>> ").upper()
    write_items(items)
    print("{} items saved to items.csv".format(number_of_items))
    print("Have a nice day :)")


main()




# def file_write(item_name,item_price,item_priority,item_status):
#     import csv
#     fields = [item_name,item_price,item_priority,item_status]
#     with open(('items.csv', 'a'), lineterminator=('\n')) as file:
#         writer = csv.writer(file)
#         writer.writerow(fields)
#     file.close()
