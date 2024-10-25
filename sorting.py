
class SortingModule():
    def __init__(self):
        self.steps = []

    def bubble_sort(self,arr):
        for i in range(0,len(arr)-1):
            for j in range(0,len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
            self.steps.append(arr.copy())
        

    def selection_sort(self,arr):
        for i in range(len(arr)-1):
            min_element  = arr[i]
            for j in range(i+1,len(arr)):
                if arr[j] < min_element:
                    min_element = arr[j]
                    min_index = j
            if min_element != arr[i]:
                temp = arr[i]
                arr[i] = min_element
                arr[min_index] = temp
            self.steps.append(arr.copy())
        
    
    def insertion_sort(self,arr):
        for i in range(0,len(arr)):
            j = i
            while j>0 and arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j]  = arr[j-1]
                arr[j-1] = temp
                j-=1
            self.steps.append(arr.copy())
        

    def merge(self,arr,low,mid,high):
        temp = []
        left = low
        right = mid+1

        while left<=mid and right<=high:

            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        while left<=mid:
            temp.append(arr[left])
            left+=1

        while right<=high:
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i] = temp[i-low]
        self.steps.append(arr.copy())

    def merge_sort(self,arr,low,high):
        if low >= high :
            return
        mid = (low+high)//2
        self.merge_sort(arr, low, mid)
        self.merge_sort(arr, mid+1, high)
        self.merge(arr, low, mid, high)
            