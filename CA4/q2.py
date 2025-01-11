def charge_tree(n, m, edges, charges):
    from collections import defaultdict

    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    values = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    charge_updates = [0] * (n + 1)
    for a, b in charges:
        charge_updates[a] += b
    
    def dfs(node, cumulative_charge):
        visited[node] = True
        cumulative_charge += charge_updates[node]
        values[node] = cumulative_charge
        for neighbor in tree[node]:
            if not visited[neighbor]:
                dfs(neighbor, cumulative_charge)
    
    dfs(1, 0)
    return values[1:]

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    charges = [tuple(map(int, input().split())) for _ in range(m)]
    result = charge_tree(n, m, edges, charges)
    print(" ".join(map(str, result)))