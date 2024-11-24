import ast

def surviving_rats(rats):
    stack = []
    for rat in rats:
        while stack and stack[-1] > 0 and rat < 0:
            if stack[-1] + rat == 0:
                stack.pop()
                break
            elif stack[-1] + rat < 0:
                stack.pop()
            else:
                break
        else:
            stack.append(rat)
    return stack

rats = ast.literal_eval(input())
stack = surviving_rats(rats)
print("[" + ",".join(map(str, stack)) + "]")