str1=input("enter the string1:")
str2=input("enter the string2:")
if (len(str1)==len(str2)):
    if sorted(str1)==sorted(str2):
        print("it is an aligram")
    else:
            print("it is not an aligram")
else:
                print("length problem,not an aligram")
                  
