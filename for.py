num_a = 6
for i in range(3):
    num_c =int(input("input your num :"))
    if num_c > num_a:
        print("The num is too bigger")
    elif num_c < num_a:
        print("The num is too small")
    else:
        print("Bingo")
        break
else:
     print("too many retrys! the right num is ",num_a)