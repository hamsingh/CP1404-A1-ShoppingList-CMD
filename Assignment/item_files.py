item_name = "Phone"
item_price = "400"
item_priority = "2"
item_status = "r"

# def file_write():
#     import csv
#     fields = [item_name,item_price,item_priority,item_status]
#     with open('items.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(fields)
#     file.close()
#
# file_write()

def load_items():
    lines = []
    file = open('items.csv', 'r', newline='')
    for line in file.readlines():
        l = line.strip().split(',')
        l[2] = int(l[2])
        l[1] = float(l[1])
        lines.append(l)
    lines.sort()
    print(lines)
    return lines

#items = load_items()
#number_items = (len(items))

def required (lines):
    load_items()
    print(lines)

required(lines)
