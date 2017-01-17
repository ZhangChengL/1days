num_x = 6
aaa = 0
while True:
    num_c = int(input("input one num:"))
    if num_c == num_x:
            print("Bingo")
            break
    elif num_c > num_x:
            print("the num is too bigger")
    else:
            print("the num is too small")
    aaa = aaa + 1
    #print(aaa)
    if aaa == 3:
        print("连续猜错",aaa,"次啦！","The right num is ",num_x)
        break



