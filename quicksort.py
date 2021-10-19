#Quick sort 
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        i+=1
        while arr[i]<=pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quickSort(arr,low,high):
    if low==high:
        return arr
    else:
        if low<high:
            j=partition(arr,low,high)
            quickSort(arr,low,j)
            quickSort(arr,j+1,high)

arr = list(map(int,input("Enter the elements(seperated by spaces): ").split(' ')))
arr.append(99999)
quickSort(arr,0,len(arr)-1)
arr.pop()
print(f"The elements in sorted order: {arr}")
