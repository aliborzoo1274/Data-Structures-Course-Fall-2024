import heapq

left, right = [], []

def rebalance():
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

num_of_cases = int(input())
while num_of_cases:
    price = int(input())
    if price == 0:
        left.clear()
        right.clear()
        num_of_cases -= 1
    elif price == -1:
        print(-left[0])
        heapq.heappop(left)
        rebalance()
    else:
        if not left or price <= -left[0]:
            heapq.heappush(left, -price)
        else:
            heapq.heappush(right, price)
        rebalance()