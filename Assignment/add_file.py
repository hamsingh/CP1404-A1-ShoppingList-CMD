


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

def requireditem(number_items, items):
    print("Required items:")
    total_price = 0
    item_number = -1
    for row in items:
        total_price += row[1]
        item_number += 1
        if "r" in row[3]:
            print("{}. {:22} $  {:.2f} ({})".format(item_number, row[0], row[1], row[2]))
    print("Total expected price for {} items: ${}".format(number_items, total_price))

requireditem(number_items,items)