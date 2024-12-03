import re

with open('formatted_list3.txt', 'r') as file:
    zeilen = file.readlines()

pattern = r"mul\((\d+),(\d+)\)"
exclude_pattern = r"^don't\(\)"

total = 0

for zeile in zeilen:
    if re.match(exclude_pattern, zeile):
        continue
    matches = re.findall(pattern, zeile)
    for x, y in matches:
        produkt = int(x) * int(y)
        total += produkt

print(total)