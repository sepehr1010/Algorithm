#%%%%%%%%%%%%%%%%5


a = [1, 2, 4, 6]
b = [2, 3, 5]


def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    size = len(arr) // 2
    a, b = mergesort(arr[:size]), mergesort(arr[size:])
    arr = sort(a, b)
    return arr    


def sort(a, b):
    
    sort = [None] * len(a+b)

    i, j, k = 0, 0, 0

    while k < len(sort):
        if i == len(a):
            sort[k:] = b[j:]
            break
        if j == len(b):
            sort[k:] = a[i:]
            break
        if a[i] <= b[j]:
            sort[k] = a[i]
            i += 1
            k += 1
        elif b[j] <= a[i]:
            sort[k] = b[j]
            j += 1
            k += 1
    return sort

def sort(a, b):
    
    sort = [None] * len(a+b)

    i, j, k = 0, 0, 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sort[k] = a[i]
            i += 1
        else:
            sort[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        sort[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        sort[k] = b[j]
        j += 1
        k += 1
    return sort


mergesort([4,3,3, 23,10,5, 1, 100])

#%%%%%%%%%%%%%%%%%%%%

def search(arr, ele):
    i = 0
    while i < len(arr):
        if arr[i] == ele:
            return True
        else:
            i += 1
    return False

####

def rec_binsearch(arr, ele):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == ele:
            return True
        elif arr[mid] < ele:
            return rec_binsearch(arr[mid+1:], ele)
        else:
            return rec_binsearch(arr[:mid], ele)


#%%%%%%%%5

def bobsort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k] >= arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr

def selsort(arr):
    k = len(arr)
    while k > 0:
        temp = max(arr[:k])
        arr.remove(temp)
        arr.append(temp)
        k -= 1
    return arr

def selsort(arr):
    for n in range(len(arr), 0, -1):
        max_idx = 0
        for k in range(n):
            if arr[k] >= arr[max_idx]:
                max_idx = k
        arr[n-1], arr[max_idx] = arr[max_idx], arr[n-1]
    return arr

selsort([4,3,3, 23,10,5])


def insort(arr):
    for i in range(1, len(arr)):
        arr1 = arr[:i]
        arr2 = arr[i]
        j, k = 0, 0
        arr3 = [None] * (len(arr1)+1)
        while k < len(arr3):
            if arr2 <= arr1[j]:
                arr3[k] = arr2
                arr3[k+1:] = arr1[j:]
                break
            else:
                arr3[k] = arr1[j]
                if j == len(arr1) - 1:
                    arr3[k+1] = arr2
                    break
                else:
                    j += 1
            k += 1
        arr = arr3 + arr[i+1:]
    return arr

def insort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        pos = i
        while pos > 0 and val<arr[pos-1]:
            arr[pos] =arr[pos-1]
            pos -= 1
        arr[pos] = val
    return arr
    
    
insort([4,3,3, 23,10,5])






    
    
    
    

