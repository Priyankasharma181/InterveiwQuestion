list_1=[4,3,2,9,8,1,5,7]
i=0 
list_2=[] 
for i in range(len(list_1)):
    if list_1[i]%2==0:
        # print(s[i])
        pass
    else:
        list_2.append(list_1[i])
i=0
for i in range(len(list_2)):
    j=1
    temp=0
    for j in range(len(list_2)):
        if list_2[j]>list_2[i]:
           temp=list_2[i]
           list_2[i]=list_2[j]
           list_2[j]=temp
i=0
for i in range(len(list_1)):   
    if list_1[i]%2==0:
        a=list_1.index(list_1[i])
        # print(a)
        list_2.insert(a,list_1[i])
print(list_2)