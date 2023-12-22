def heapify(arr,n,i):  # this function identifies the largest element
        largest=i       # among the root , left and right cild
        left=2*i+1      # if largest is not root , it swaps with root and recursively call heapify
        right=2*i+2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right]> arr[largest]:
            largest=right
        
        if largest !=i:
            arr[i], arr[largest]=arr[largest], arr[i]
            heapify(arr,n,largest)   
        
        return arr    
       
def heap_sort(arr):    #builds a max heap by calling heapify on nonleaf nodes in reverse order 
    n=len(arr)         # extracts each element one by one from heap swaps the root with last element 
  
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    print(arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
   
        
arr=[12,11,13,5,6,7]        
heap_sort(arr)
print(arr)

# print(heapify(arr,len(arr),0))








            