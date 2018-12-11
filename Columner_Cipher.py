########import random
abcd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k=list(input("Enter your String"))
key="HACK"
scn=[['']*4 for i in range(0,4)]
p=sorted(list(key))
ci=[key.index(i) for i in p]
print(ci,p)

i,j=0,0
for m in k:
    if j>3:
        i+=1
        j=0
    scn[i][j]=m
    j+=1
#enc
ec=[]
i=0
for i in range(0,4):
    for j in range(0,4):
        ec.append(scn[j][ci[i]])
    
print(ec)

#dcd

dc=[]
dcdm=[['']*4 for i in range(0,4)]
i,j=0,0
c=-1
for i in range(0,4):
    for j in range(0,4):
        c+=1
        dcdm[ci[i]][j]=ec[c]
for m in range(0,4):
    for f in range(0,4):
        dc.append(dcdm[f][m])
dc=dc[:len(k)]       
        
print("Key used=",key),print("ec",ec),print("dc",dc)


"""
while a<len(k):
    a+=1;
    a=a*a;
scn=[['']*a for i in range(0,a)]
key=[random.randint(0,26) for x in range(0,a)]
skey=[abcd[a] for a in key]
order=sorted(skey)
ci=[key.index(i) for i in order]
i,j=0,0
for m in k:
    scn[i][j]=m
    i+=1
    j+=1

"""

"""
if len(k)>16:
    print("length should be less than 16")
    quit()

#enc
ec=[]
i=0
for i in range(0,a):
    for j in range(0,len(ci)):
    ec.append([ci[j]][i])
print(ec)

#dec
dc=[]
i=0
for i in range(0,a):
    ci[i]
    for j in range(0,a):
        dc.append([ci[j]][i])
    
    
    
print("Key used=",[abcd.index()])
print(rf,len(rf))
"""
