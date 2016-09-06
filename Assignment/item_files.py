item_name = "Phone"
item_price = "400"
item_priority = "2"
item_status = "r"

def file_write():
    import csv
    fields = [item_name,item_price,item_priority,item_status]
    with open('items.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
    file.close()

file_write()