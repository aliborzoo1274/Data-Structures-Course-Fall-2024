input_str = input()

list_str, x_str = input_str.split('], x = ')
list_str += ']'

houses = eval(list_str)
x = int(x_str)

save = []
for house in houses[::-1]:
    if (len(houses) % x == 0):
        break
    save.append(houses.pop())

output = []
for _ in range(int(len(houses) / x)):
    for i in range(x - 1, -1, -1):
        output.append(houses.pop(i))

output.extend(save[::-1])
print("[" + ",".join(map(str, output)) + "]")