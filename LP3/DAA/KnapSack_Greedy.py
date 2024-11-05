class Item:
    def __init__(self, value, weight):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def frac_knp(items,capacity):
    items.sort(key=lambda item:item.ratio, reverse = True)

    total_value = 0.0

    for item in items:
        if capacity > item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.ratio*capacity
            break
    
    return total_value

items = [Item(60,10),Item(100,20),Item(120,30)]
capacity = 50

ans = frac_knp(items,capacity)
print(ans)