# for i in range(10):
#     for b in range(1,i+1):
#         a=b*i
#         print(b,'*',i,'==',a, end='   ')
#     print()
#
# b=[34,43,15,25,7,3,76,88]
# s=range(len(b))[::-1]
# for i in s:
#     for a in range(i):
#         if b[a]>b[a+1]:
#             b[a+1],b[a]=b[a],b[a+1]
# print(b)


# for i in range(10):
#     for b in range(1,i+1):
#         c=i*b
#         print(b,"*",i,"==",c,end="  ")
#     print()
num=[]
# i=2
# for i in range(2,100):
#    j=2
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#       num.append(i)
# print(num)
# # a=13%12
# # print(a)
a=123455
def gg():
   global a
   a=886
   print(a)
def gg1():
   global a
   a='ffff'
   print(a)
a=123455
gg()
gg1()
print('函数外的a：'+str(a))