class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):

    items.sort(key=lambda item: item.ratio, reverse=True)
    
    total_value = 0.0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.ratio * capacity
            break
            
    return total_value

def menu():
    items = []
    
    while True:
        print("\nFractional Knapsack Problem")
        print("1. Add Item")
        print("2. Solve Knapsack Problem")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            value = float(input("Enter the value of the item: "))
            weight = float(input("Enter the weight of the item: "))
            items.append(Item(value, weight))
            print(f"Item added: Value = {value}, Weight = {weight}")
        
        elif choice == '2':
            if not items:
                print("No items available. Please add items first.")
                continue
            
            capacity = float(input("Enter the capacity of the knapsack: "))
            max_value = fractional_knapsack(capacity, items)
            print(f"Maximum value in the knapsack: {max_value}")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    menu()
