List = [7, 4, 5, 1, 3]

def BubbleSort(lst):
    count = len(lst)
    while count != 0:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1] : lst[i] , lst[i+1] = lst[i+1],  lst[i]
        count-=1
    return lst

print(BubbleSort(List))