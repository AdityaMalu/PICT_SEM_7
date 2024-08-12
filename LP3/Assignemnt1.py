def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_recursive_memoization(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci_recursive_memoization(n - 1, memo) + fibonacci_recursive_memoization(n - 2, memo)
    return memo[n]

def menu():
    while True:
        print("\nFibonacci Sequence Calculator")
        print("1. Calculate Fibonacci using Iterative Method")
        print("2. Calculate Fibonacci using Recursive Method")
        print("3. Calculate Fibonacci using Recursive Method with Memoization")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice in ['1', '2', '3']:
            n = int(input("Enter the value of n: "))
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            
            if choice == '1':
                result = fibonacci_iterative(n)
            elif choice == '2':
                result = fibonacci_recursive(n)
            elif choice == '3':
                result = fibonacci_recursive_memoization(n)
                
            print(f"Fibonacci({n}) = {result}")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    menu()
