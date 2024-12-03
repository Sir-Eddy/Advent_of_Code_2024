import re

input_file = 'list3.txt'
output_file = 'formatted_list3.txt'

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

with open(input_file, 'r') as file:
    gesamte_zeile = ''.join(line.strip() for line in file)

reformatted_lines = re.sub(f"({do_pattern}|{dont_pattern})", r"\n\1", gesamte_zeile).splitlines()

with open(output_file, 'w') as file:
    for line in reformatted_lines:
        if line.strip():
            file.write(line.strip() + '\n')