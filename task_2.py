from re import*
from decimal import Decimal
import argparse

magazine = {}
def f(file):
    file = open(file, 'r', encoding='utf-8')
    for line in file:
        zn = match(r'"(\w+ \w+ \w+)" - (\d+): ([-+]\d+)', line)
        name, chet, summa = zn.groups()
        summa = Decimal(summa)
        if name not in magazine:
            magazine[name]={}
        if chet not in magazine[name]:
            magazine[name][chet] = Decimal('0')
        magazine[name][chet] += summa
    
    for i in magazine.items():
        mess = f'{i[0]} - '
        k = True
        for j in i[1].items():
            if k:
                mess += f'{j[0]}: {j[1]}'
                k = False
            else:
                mess += f', {j[0]}: {j[1]}'
        print(mess)

if __name__=='__main__':  
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()
    file_ = args.file
    f(file_)
