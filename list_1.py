a = [23,5117,22]
# b = (a[i]//10)
li = []
i=0
while i<len(a):
    b = (a[i]//10)
    c = b%10
    if c==2:
        li.append(a[i])  
    i+=1         
print(li) 

        

