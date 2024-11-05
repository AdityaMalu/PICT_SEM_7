import heapq

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    # Define comparison operators for the priority queue
    def __lt__(self, other):
        return self.bound > other.bound

def compare_items(item):
    return item.ratio

def bound(u, n, W, items):
    if u.weight >= W:
        return 0
    profit_bound = u.profit
    j = u.level + 1
    totweight = u.weight

    while j < n and totweight + items[j].weight <= W:
        totweight += items[j].weight
        profit_bound += items[j].value
        j += 1

    if j < n:
        profit_bound += (W - totweight) * items[j].ratio

    return profit_bound

def knapsack(W, items):
    n = len(items)
    items.sort(key=compare_items, reverse=True)

    Q = []
    u = Node(-1, 0, 0, 0)
    heapq.heappush(Q, u)

    max_profit = 0

    while Q:
        u = heapq.heappop(Q)

        if u.level == -1:
            v = Node(0, 0, 0, 0)
        elif u.level == n - 1:
            continue
        else:
            v = Node(u.level + 1, u.profit, u.weight, 0)

        if v.level < n:
            v.weight = u.weight + items[v.level].weight
            v.profit = u.profit + items[v.level].value

            if v.weight <= W and v.profit > max_profit:
                max_profit = v.profit

            v.bound = bound(v, n, W, items)

            if v.bound > max_profit:
                heapq.heappush(Q, v)

            v = Node(u.level + 1, u.profit, u.weight, bound(u, n, W, items))

            if v.bound > max_profit:
                heapq.heappush(Q, v)

    return max_profit

if __name__ == "__main__":
    W = 50  # Knapsack capacity
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]  # {weight, value}

    max_value = knapsack(W, items)
    print(f"Maximum value: {max_value}")