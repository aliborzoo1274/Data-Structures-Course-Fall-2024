import ast

matrix = ast.literal_eval(input())
output = []

while matrix and any(matrix):
    
    output.extend(matrix.pop(0))
    if not matrix or not any(matrix):
        break
    
    for row in matrix:
        output.append(row.pop())
    if not matrix or not any(matrix):
        break
    
    output.extend(matrix.pop()[::-1])
    if not matrix or not any(matrix):
        break
    
    for row in reversed(matrix):
        output.append(row.pop(0))

print(output)