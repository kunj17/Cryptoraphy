import numpy as np
from fractions import Fraction
abcd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=np.array([(3,3),(2,5)])
print(a)
ste=input("Enter the string to encode:")
if len(ste)%2!=0:
    ste=ste+ste[0]
print(ste)
i=0
cipher=""
while i<len(ste):
    st=abcd.index(ste[i])
    sd=abcd.index(ste[i+1])
    b=np.array([(st),(sd)])
    num=(np.matmul(a,b))%52
    cipher=cipher+abcd[num[0]]+abcd[num[1]]
    i=i+2
print("cipher text is:",cipher)

#decryption
deta=int(np.linalg.det(a))
adj=np.array([(5,-3), (-2,3)])
def inv(k1):
    c=1
    diff=0
    i=1
    j=2
    if k1%52==1:
        return 1
    elif (k1*2)%52==1:
        return 2
    else:
        diff=((k1*3)%52)-((k1*2)%52)
        while True:
            c+=1
            diff=diff+k1
            diff=diff%52
            if diff==1:
                break
        return c
inv=(inv(deta))%52
new=np.dot(inv,adj)
i=0
plain=""
while i<len(cipher):
    st=abcd.index(cipher[i])
    sd=abcd.index(cipher[i+1])
    b=np.array([(st),(sd)])
    num=(np.matmul(new,b))%52
    plain=plain+abcd[num[0]]
    plain=plain+abcd[num[1]]
    i=i+2
print("plain text is:",plain)
