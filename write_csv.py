import csv


def write_csv(filename,*args):
    args_list = []
    for arg in args:
        args_list.append(arg)

    with open(filename, 'a', encoding='utf-8', newline="") as f:
        data_handler = csv.writer(f, delimiter=",")
        data_handler.writerow(args_list)



write_csv('عصمت','چغتائی','کمال')


