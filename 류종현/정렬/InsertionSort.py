List = [9, 4, 3, 1, 12]

def InsertionSort(lst):
    for i in range(1,len(lst)):
        for j in range(i-1,-1,-1):
            if lst[j] > lst[j+1] : lst[j+1], lst[j] = lst[j], lst[j+1]

InsertionSort(List)