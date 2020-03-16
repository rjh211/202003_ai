"""19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
 """
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
result = []

for i in range(0,len(a)):
    if len(a[i]) == 7:
        result.append(a[i])
print(result)