name = input("name:").strip()
age = input("age:")
job = input("job:")
print("Information of %s:\nname:%s\nage:%s\njob:%s"  %(name,name,age,job)  )

msg = '''
    Information of %s:
        name:%s
        age:%s
        job:%s

'''%(name,name,age,job)
print(msg)