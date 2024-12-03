import re

with open('list3.txt', 'r') as file:
    zeilen = file.readlines()

pattern = r"mul\((\d+),(\d+)\)"

total = 0

for zeile in zeilen:
    matches = re.findall(pattern, zeile)
    for x, y in matches:
        produkt = int(x) * int(y)
        total += produkt

print(total)
