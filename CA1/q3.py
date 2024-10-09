import ast

matrix = ast.literal_eval(input())
output = []
while True:
    for elem in matrix[0]:
        output.append(elem)
    del matrix[0]
    if len(matrix) == 0:
        break

    for list in matrix:
        output.append(list[-1])
        del list[-1]
    if len(matrix) == 0:
        break

    for i in range(len(matrix[-1]) - 1, -1, -1):
        output.append(matrix[-1][i])
    del matrix[-1]
    if len(matrix) == 0:
        break
    
    for i in range(len(matrix) - 1, -1, -1):
        output.append(matrix[i][0])
        del matrix[i][0]
    if len(matrix) == 0:
        break

print(output)