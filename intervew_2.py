a = []
size = int(input("enter the size of the list"))
for i in range(size):
    val = int(input("enter the num"))
    a.append(val)
i = 1
j = size - 1
while i < j:
    p = a[i]
    a[i] = a[j]
    a[j] = p
    i += 1 
    j -= 1
print("list after the reverse =")
for i in range(size):
    print(a[i])
