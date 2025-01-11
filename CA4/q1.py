from collections import deque

def min_steps_to_reach(n, m):
    if n >= m:
        return n - m
    
    queue = deque([(n, 0)])
    visited = set([n])
    
    while queue:
        current, steps = queue.popleft()
        
        if current == m:
            return steps
        
        if current * 2 <= m * 2:
            if current * 2 not in visited:
                queue.append((current * 2, steps + 1))
                visited.add(current * 2)
        
        if current - 1 > 0:
            if current - 1 not in visited:
                queue.append((current - 1, steps + 1))
                visited.add(current - 1)
    
n, m = map(int, input().split())
print(min_steps_to_reach(n, m))