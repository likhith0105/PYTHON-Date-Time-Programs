import math
lst=[]
even=[]
odd=[]
n = int(input(""))


for i in range(n):
    a = int(input(""))
    lst.append(a)
    if(a % 2 == 0):
      even.append(a)
    else:
      odd.append(a)

print(even,odd)
print("sum of even numbers:",sum(even))
print("sum of odd:",sum(odd))

