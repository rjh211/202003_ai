'''
3.
앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을
경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다.
주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.
list=[4,3,2,1,8,7,5,10,11,16,21,6]

<입력>
print(bubble_sort(list))

<출력>
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 16, 21]'''

lst=[4,3,2,1,8,7,5,10,11,16,21,6]
count = len(lst)

def compare(a,b):
    return a if a<=b else b

def bubble_sort(sortList):
    global count
    while count != 1:
        for i in range(1, count):
            if sortList[i-1] > sortList[i]: 
                sortList[i-1], sortList[i] = sortList[i], sortList[i-1]
        count-=1
        bubble_sort(sortList)
    return sortList


print(bubble_sort(lst))