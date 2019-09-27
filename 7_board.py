import sys 
n=int(input("enter the order of board : "))
n1=int(input("enter the width : "))
h=int(input("enter the height : "))
if n>10 or n1>10 or h>10:
  print("input too large to handle")
  sys.exit()
a='-'*n1*2
b='|'
s1=(' '+a)*n
s2=(b+'  '*n1)*n

for i in range(n) :
  print(s1)
  for i in range(h) :
    print(s2+b)
print(s1)
