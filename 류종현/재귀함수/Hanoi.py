def hanoi(numOfDisk,  orgPillar, purposePillar):
    if numOfDisk == 1:
        print(f"{orgPillar}번 기둥의 {numOfDisk}번 원반을 {purposePillar}번 기둥에 옮긴다.")
    else:
        if orgPillar == 1 and purposePillar == 2:
            hanoi(numOfDisk-1,1,3)
            print(f"{orgPillar}번 기둥의 {numOfDisk}번 원반을 {purposePillar}번 기둥에 옮긴다.")
            hanoi(numOfDisk-1,3,2)
        elif orgPillar == 1 and purposePillar == 3:
            hanoi(numOfDisk-1,1,2)
            print(f"{orgPillar}번 기둥의 {numOfDisk}번 원반을 {purposePillar}번 기둥에 옮긴다.")
            hanoi(numOfDisk-1,2,3)
        elif orgPillar == 2 and purposePillar == 3:
            hanoi(numOfDisk-1,2,1)
            print(f"{orgPillar}번 기둥의 {numOfDisk}번 원반을 {purposePillar}번 기둥에 옮긴다.")
            hanoi(numOfDisk-1,1,3)

hanoi(3,1,3)