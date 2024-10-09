list = []
input_lines = []
lines = []
columns = []
blocks = []
result = 'true'

for i in range(9):
    input_lines.append(input())

for input_line in input_lines:
    for char in input_line:
        if '0' < char <= '9':
            list.append(char)
    lines.append(list)
    list = []

for i in range(9):
    for input_line in input_lines:
        if '0' < input_line[i * 4 + 3] <= '9':
            list.append(input_line[i * 4 + 3])
    columns.append(list)
    list = []

for i in range(9):
    for j in range(3):
        for z in range(3):
            if '0' < input_lines[(i % 3) * 3 + j][int(i / 3) * 12 + z * 4 + 3] <= '9':
                list.append(input_lines[(i % 3) * 3 + j][int(i / 3) * 12 + z * 4 + 3])
    blocks.append(list)
    list = []

for line in lines:
    if len(line) != len(set(line)):
        result = 'false'

for column in columns:
    if len(column) != len(set(column)):
        result = 'false'

for block in blocks:
    if len(block) != len(set(block)):
        result = 'false'

print(result)