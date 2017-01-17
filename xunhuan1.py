num_x = 6
num_c = -1
while num_x != num_c :  #/死循环
    num_c = int(input("input one num:"))
    #if num_c == num_x:
            #print("Bingo")
            #break
    if num_c > num_x:
            print("the num is too bigger")
    elif num_c < num_x:
            print("the num is too small")
print("Bingo!")