string = input("Enter a string")
a = ""
for i,char in enumerate(string):
    if(ord(char)>=65 and ord(char)<=90):
        a+=string[i:]
        break
    elif(ord(char)>=97 and ord(char)<=122):
        a+=char.upper()
        a+=string[i+1:]
        break
    a+=char
print(a)



# txt = "Welcome to my world"

# x = txt.title()

# print(x)
