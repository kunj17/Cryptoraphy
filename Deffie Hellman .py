abcd=[chr(i) for i in range(97,97+26)]
g=11
p=7
a=int(input('Enter a:'))
b=int(input('Enter b:'))

print('ON a side..')
print('performing (g^a mod p) \n g=',g,' a=',a,' p=',p)
aans=g**a%p
print('-->',aans)


print('ON b side..')
print('performing (g^b mod p) \n g=',g,' b=',b,' p=',p)
bans=g**b%p
print('-->',bans)

print('A sending number to B..')
baans=aans**b%p
print('B calculates- a**b mod p =',baans)

print('B sending number to A..')
abans=bans**a%p
print('A calculates- b**a mod p =',abans)
print('Calculated results are same.')
print('Key Successfully exchanged.')
