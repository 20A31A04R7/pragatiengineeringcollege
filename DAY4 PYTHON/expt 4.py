import re
#print(string.ascii_letters)
#ch = 'g'
#print('a' <=ch <='z')
#str= "hello"
#print(dir(str))
str="she sells sea shells at sea shore"
p1="sells"
if re.match(p1,str):
    print("match found")
else:
    print(p1,"not present in string")
p2=" she "
if re.match(p2,str):
    print("match found")
else:
        print(p2,"not present in string")
