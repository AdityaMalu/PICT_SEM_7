def fibo(n):
    if n<=1:
        return n
    
    return fibo(n-1) + fibo(n-2)


def fibo_recc(n):
    for i in range(n):
        print(fibo(i),end=" ")

def fibo_iter(n):
    fibo_list = [0,1]
    for i in range(n-2):
        curr = fibo_list[-1] + fibo_list[-2]
        fibo_list.append(curr)
    print(*fibo_list)

(fibo_recc(10))
print()
(fibo_iter(10))