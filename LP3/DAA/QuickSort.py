import random

def deterministic_quic_sort(arr,low,high):
    pivot = arr[low]
    left = low+1
    right = high

    while True:
        while left <= right and arr[left] <=pivot:
            left+=1
        while left <= right and arr[right] >= pivot:
            right-=1
        if left > right:
            break

        arr[left],arr[right] = arr[right],arr[left]
    arr[low],arr[right] = arr[right],arr[low]
    return right

def do_determinsitc_quicksort(arr,low,high,compare,swap):
    if low < high:
        pivot = deterministic_quic_sort(arr,low,high)
        compare[0] += (high - low)
        swap[0] += 2

        do_determinsitc_quicksort(arr,low,pivot-1,compare,swap)
        do_determinsitc_quicksort(arr,pivot+1,high,compare,swap)


def random_quicksort(arr,low,high):
    pivot_index = low + random.randint(0,high-low)
    arr[low],arr[pivot_index] = arr[pivot_index],arr[low]
    pivot= arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left+=1
        while left <= right and arr[right]>=pivot:
            right-=1
        if left >right:
            break
        arr[left],arr[right] = arr[right],arr[left]
    arr[low],arr[right] = arr[right],arr[low]
    return right

def do_random_quicksort(arr,low,high,comapare,swaps):
    if low < high:
        pivot_ind = random_quicksort(arr,low,high)
        comapare[0] += (high - low)
        swaps[0] +=2

        do_random_quicksort(arr,low,pivot_ind-1,comapare,swaps)
        do_random_quicksort(arr,pivot_ind+1,high,comapare,swaps)


compare_det = [0]
swap_det =[0]
arr = [random.randint(0,100) for _ in range(10)]
arr1 = arr.copy()
print(*arr)
do_determinsitc_quicksort(arr,0,len(arr)-1,compare_det,swap_det)
print(*arr)
print(f"NO of Comparisioins : {compare_det[0]}")
print(f"NO of Swaps : {swap_det[0]}")


print()
compare_rand = [0]
swap_rand =[0]
arr = [random.randint(0,100) for _ in range(10)]
print(*arr1)
do_random_quicksort(arr1,0,len(arr1)-1,compare_rand,swap_rand)
print(*arr1)
print(f"NO of Comparisioins : {compare_rand[0]}")
print(f"NO of Swaps : {swap_rand[0]}")