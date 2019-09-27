with open("prime.txt",'r') as f :
    prime=f.readlines()
pri=prime[0].rstrip("\n").split(" ")
pri.pop()
pri=list(map(int,pri))



with open("happy.txt",'r') as f1 :
    prime=f1.readlines()
hap=prime[0].rstrip("\n").split(" ")
hap.pop()
hap=list(map(int,pri))
#print(hap)
p=len(pri)
while p:
    p-=1
    if pri[p] in hap :
        print(pri[p],end=" ")
    
