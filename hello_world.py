import os
import json
import csv


#dit = {'Q1': 'Hello world','Q2': 'sum_number','Q3': '[top10_list]'}

def read():
    with open('/tcdata/num_list.csv') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row[0] for row in reader]
        int_list = [int(x) for x in rows]
        int_list.sort(reverse=True)
        #int_list = rows
        return int_list


def sum(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sum(list, size - 1)


def save_json():
    with open('result.json', 'w', encoding='utf-8') as f:
        dit = {'Q1': 'Hello world', 'Q2': sum_number, 'Q3': top10_list}
        json.dump(dit, f, ensure_ascii=False)
        f.close


if __name__ == "__main__":
    list = read()
    sum_number = sum(list, len(list))
    top10_list = list[:10]
    # print(sum_number,top10_list)
    save_json()
