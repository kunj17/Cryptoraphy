abcd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k=list(input("Enter your String"))
nor=2
rf=[['']*len(k) for i in range(0,nor)]
print(rf,len(rf))

i,j=1,-1
for ind,t in enumerate(k):
    print("i= ",i," j=",j)
    j+=1
    if ind%2==0:
        i=0
    else:
        i=1
    rf[i][j]=t
    i+=1
ec=[y for t in rf for y in t if y!=""]
#decryption
dc=[]
i,j=1,-1
for ind,t in enumerate(k):
    print("i= ",i," j=",j)
    j+=1
    if ind%2==0:
        i=0
    else:
        i=1
    i+=1
    
    dc.append(t)

print("Encoding=",ec)
print("decoding=",dc)
