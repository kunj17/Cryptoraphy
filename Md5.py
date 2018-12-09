import hashlib
import sys
def main():
    print ("MD5 ENCRYTION")
    print( '1 - ENCRYTION WITH MD5')
    print( '2 - MD5 DECRYTION')
    select = int(input("SELECT OPTION:"))
    if select == 1:
        encrytion()
    elif select == 2:
        decrytion()
t=''
def encrytion():
        print("MD5 ENCRYTION");
        MD5encrytion()
def MD5encrytion():
        
        string=input("string you want to convert to SHA1 > ")
        algorithim=hashlib.md5()
        algorithim.update(string.encode('utf-8'))
        encrypted=algorithim.hexdigest()
        print('%s to MD5 hash %s' %(string,encrypted))
        mainmenu=input("Press [ENTER] to go to main menu.")
        main()
def decrytion():
        print("MD5 DECRYPTION")
        MD5decrytion()
 
def MD5decrytion():
        
        counter = 0
        lines = 0
        string=input("paste MD5 Hash > ")
        wordList ='temporary.txt'
        try:
                wordlistfile = open(wordList,'a')
                wordlistfile.write(t)
                wordlistfile.close()
                wordlistfile = open(wordList,'r')
                for line in open(wordList):
                        lines += 1
        except IoError:
                print('Dictionary is not valid')
                input("Press [ENTER] to try Again")        
                main()
        else:
            
                pass
        for line in wordlistfile:
            algorithim = hashlib.md5()
            line = line.replace("\n","")
            algorithim.update(line.encode('utf-8'))
            wordlistdecrypted = algorithim.hexdigest()
            counter += 1
            percentage_raw = float(counter) / float(lines) * 100
            percentage_raw ="%.0f" % percentage_raw; percentage = str(percentage_raw) + " " + "%"
                
            print(percentage)
            if wordlistdecrypted == string:
                print('Hash Crackrd - %s' % line)
                mainmenu =input("Press [ENTER] to go to main menu")
                main()
main()

