class Item:
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value
    
def knp_sack(W,items):
    n = len(items)
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            if items[i-1].weight<= W:
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-items[i-1].weight] + items[i-1].value)
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]

W = 50  
items = [Item(10, 60), Item(20, 100), Item(30, 120)]

max_value = knp_sack(W, items)
print(f"Maximum value: {max_value}")