arr =[4,5,7,3,262,2,23,4,23,532,53,32,67,57,45,12,123]
steps = []

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while(i<j):

        while arr[i] <= pivot and i <= high-1:
            i+=1
            
        while arr[j] > pivot and j >= low+1:
            j-=1
            
        if i<j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j


def quick_sort(arr,low,high):
    if low >= high:
        return 
    partition_index = partition(arr,low,high)
    quick_sort(arr,low,partition_index-1)
    quick_sort(arr,partition_index+1, high)
    steps.append(arr.copy())
    return arr

arr = quick_sort(arr,0,len(arr)-1)
print(arr)
print()
print(steps)