# list=[['g','f','g'],['i','s'],['b','e','s','t']]
# i=0
# b=[]
# while i<len(list):
#     if type(list[i])==type([]):
#         j=0
#         while j<len(list[i]):
#             b.append(list[i][j])
#             j+=1
#     else:
#         b.append(list[i])
#     i+=1
# print(b)

# list=[['g','f','g'],['i','s'],['b','e','s','t']]
# i=0
# while i<len(list):
#     list1="".join(list[i])
#     i+=1
#     print(list1)


list=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
a=[]
while i<len(list):
    a.extend(list[i])
    i+=1
    list1="".join(a)
print(list1)