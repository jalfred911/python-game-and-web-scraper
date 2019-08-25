staff = open("intern.txt" , "r")
for name in staff.readlines():
    print(name)


'''print(staff.readable())
print(staff.readlines()[1])
'''

staff.close()


