List = [6,8,3,9,10,1,2,4,7,5]
resList = []
switch = False

def Devide(lst):
    global resList

    if len(lst) == 1:
        resList.append(lst)
        return lst
    else:
        foreList = lst[:int(len(lst)/2)]
        backList = lst[int(len(lst)/2):]

        Devide(foreList)
        Devide(backList)

    return resList

def Merge(lst):
    newList = []
    for i in range(0, len(lst)//2):
        newList.append(Combine(lst[i*2],lst[i*2+1]))
    if len(lst) %2 == 1:
        newList.append(lst[-1])
    if len(newList) != 1:
        newList = Merge(newList)
    return newList
        

def Combine(firstList, lastList):
    global switch
    retList = []
    while switch == False:
        if len(firstList) !=0 and len(lastList) != 0:
            retList.append(firstList.pop(0) if firstList[0] < lastList[0] else lastList.pop(0) )
        elif len(firstList) !=0 and len(lastList) == 0:
            retList += firstList
            del firstList, lastList
            switch = True

        elif len(firstList) ==0 and len(lastList) != 0:
            retList += lastList
            del firstList, lastList
            switch = True

    switch = False            
    return retList
    
print(Merge(Devide(List)))