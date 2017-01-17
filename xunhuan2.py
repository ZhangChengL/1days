num_a = 6
num_b = 0
while num_b < 3:
    num_c =int(input("input your num :"))
    if num_c > num_a:
        print("The num is too bigger")
    elif num_c < num_a:
        print("The num is too small")
    else:
        print("Bingo")
        break
    num_b = num_b +1
else:
     print("too many retrys! the right num is ",num_a)