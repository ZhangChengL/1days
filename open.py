f = open("test.txt","w")

f.write("this is 1 line\n")
f.write("this is 2 line\n")
f.write("this is 3 line\n")
f.close()

f = open("test.txt","r")
f.read()