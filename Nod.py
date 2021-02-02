a,b = map(int,input("Enter two numbre's: ").split())
print(a,'and',b,'Nod = ',end='')
while b > 0:
   a,b = b,a % b
print(a)