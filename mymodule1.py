# mymodule1.py
def insert_value(sorted_list, value):
    index = 0
    while index < len(sorted_list) and sorted_list[index] < value:
        index += 1
    sorted_list.insert(index, value)
    return sorted_list



