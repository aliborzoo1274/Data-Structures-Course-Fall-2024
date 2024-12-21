def main():
    import sys
    n = int(sys.stdin.readline())
    if n == 0:
        print()
        return

    segments = []
    points = set()
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().split())
        segments.append((l, r))
        points.add(l)
        points.add(r + 1)

    sorted_points = sorted(points)
    point_map = {x: i for i, x in enumerate(sorted_points)}
    freq = [0] * (len(sorted_points) + 1)

    for l, r in segments:
        freq[point_map[l]] += 1
        freq[point_map[r + 1]] -= 1

    current = 0
    counts = [0] * (n + 1)
    for i in range(len(sorted_points)):
        current += freq[i]
        if 1 <= current <= n:
            next_point = sorted_points[i + 1] if i + 1 < len(sorted_points) else sorted_points[i]
            counts[current] += sorted_points[i + 1] - sorted_points[i] if i + 1 < len(sorted_points) else 0

    print(' '.join(map(str, counts[1:n+1])))

if __name__ == "__main__":
    main()