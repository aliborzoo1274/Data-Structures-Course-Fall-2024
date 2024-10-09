input = input()
string_output = ''

while input[0] == ' ':
    input = input[1:]

if input[0] == '+' or input[0] == '-':
    string_output += input[0]
    input = input[1:]

for char in input:
    if '0' <= char <= '9':
        string_output += char
    else:
        break
if (string_output == '' or string_output == '+' or string_output == '-'):
    string_output = '0'

output = int(string_output)
if output < -2**31:
    output = -2**31
elif output > 2**31 - 1:
    output = 2**31 - 1
    
print(output)