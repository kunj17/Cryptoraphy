import hashlib
msg=input('enter your message')

#encryption
m=msg.encode('utf-8')
evc=hashlib.md5(m).hexdigest()
print('Sender side.........')
print('Sending message -{} \n with tag-{}'.format(m,evc))

#decryption
dvc=hashlib.md5(m).hexdigest()
if evc==dvc:
    print('Receiver side........')
    print('Message received-',m,' <-Correct as tag obtained here is same')

