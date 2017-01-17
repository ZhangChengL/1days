while True:
    city_list = ['1.四川','2.重庆']
    city_list1 = ['1.成都','2.绵阳']
    city_list2 = ['1.高新区','2.新都区']
    print(city_list[0])
    print(city_list[1])
    ch1 = input("选择地区：")
    if ch1 == 1:
        print(city_list1[0])
        print(city_list1[1])
        ch2 = input("选择城市：")
        if ch2 == 1:
            print(city_list2[0])
            print(city_list2[1])
            ch3 = input("选择区县：")
            if ch3 == 1:
                print(city_list2[0],city_list1[0],city_list[0])
            elif ch3 == "b":
                break
            else:
                print("111")
        elif ch2 == "b":
            break
        else:
            print("222")
    elif ch1 == "b":
        break
    else:
        print("333")


