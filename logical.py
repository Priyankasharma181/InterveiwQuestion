# assending for odd
a = [4,32,2,8,13,7,6,0,3,64]
for i in range(len(a)):
    if a[i]%2 != 0:
        for s in range(len(a)):
            for k in range((len(a)) - s):
                if a[k]%2 != 0:
                    if a[i] < a[k]: 
                        temp = a[i]
                        a[i] = a[k]
                        a[k] = temp
print(a)                        
                        
# # desending for even
# a = [4,3,2,8,1,7,6,9]
# for i in range(len(a)):
#     if a[i]%2 != 0:
#         for s in range(len(a)):
#             for k in range((len(a)) - s):
#                 if a[k]%2 != 0:
#                     if a[i] > a[k]: 
#                         temp = a[i]
#                         a[i] = a[k]
#                         a[k] = temp
# print(a)                        


