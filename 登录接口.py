name = "zcl"
password = "123456"
for i in range(3):
    inname = input("input your mame :")
    inpass = input("input your password:")

    if inname == name and inpass == password:
        print("登录成功！")
        break
    #elif num_c < num_a:
     #   print("The num is too small")
    else:
        print("账户密码错误，请重新输入")
        #break
else:
     print("连续输入多次，已锁定！")