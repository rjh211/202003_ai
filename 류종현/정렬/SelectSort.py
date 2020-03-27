List = [9,4,3,1,12]

minValue = 100
position = 0



def SelectSort(lst):
    global minValue,  position
    resultList = []
    for _ in range(len(lst)):
        for index, value in enumerate(lst):
            if minValue > value :
                minValue= value 
                position= index 
        resultList.append(lst.pop(index-1))
    print(resultList)

SelectSort(List)