List = [5, 3, 8, 4, 9, 1, 6, 2, 7]
resultList = []

def Quick(lst):
    global resultList, List
    if len(lst)== 1 or len(lst) == 0:
        return
    pivot = lst.pop(0)
    g1, g2 = [], []
    for i in lst:
        if pivot > i :
            g1.append(i)
        else : g2.append(i)

    Quick(g1)
    Quick(g2)
    resultList.append(pivot)
    resultList.append(g2[0])
    if  len(List) + 2 == len(resultList):
        resultList.pop(len(resultList)-1)
        resultList.pop(len(resultList)-1)
        resultList.insert(len(resultList)//2,pivot)
        return resultList


print(Quick(List))