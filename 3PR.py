

def build_array():


    n=int(input("Enter Size Of Array : "))
    array=[ 0*n for i in range(n)]

    for i in  range(n):
        print("Enter",i+1,"Of Array:")
        a=int(input())
        array[i]=a

        
    return array
        
        




def selection_sort(arr):

    n=len(arr)
    for i in range(n-1):
        min=i
        
        for j in range(i+1,n):

            if arr[j] < arr[min]:
                min=j

        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp

array1=build_array()
selection_sort(array1)
print(array1)


