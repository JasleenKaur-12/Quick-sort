def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<pivot]
    right=[x for x in arr[:-1] if x>=pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
arr_input=input("enter item by comma")
arr=[int(x) for x in arr_input.split(",")]
sorted_array=quick_sort(arr)
print("sorted array is",sorted_array)