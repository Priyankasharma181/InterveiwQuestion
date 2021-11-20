num = float(input("enter the num"))
a = num*10
if a % 5 == 0:
    print(num)
elif a %10 > 5:
    print(int(num)+1)
else:
    print(int(num) - 1)       
