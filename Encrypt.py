from Crypto.Cipher import AES
import os
import hashlib as hl
import sys

class Cipher:
    def __init__(self):
        pass
    
    def padToAES(self, entry):
       # entry=entry.encode('utf-8')
        while len(entry) % AES.block_size!=0:
            entry=entry + b'0'
        return entry
    
    def cipher(self, password, file):
        salt=os.urandom(8) 
        
        key= hl.pbkdf2_hmac('sha1',password.encode('utf-8'), salt, 400, dklen=16)
        mode= AES.MODE_CBC
        IV= os.urandom(16)
        
        print(len(key))
        print(len(IV))
        
        cc= AES.new(key,mode,IV)
        with open(file,'rb') as r:
            oldFile=r.read()
        
        oldFile=self.padToAES(oldFile)
        encryptedFile=cc.encrypt(oldFile)
        
        with open(file+'.enc','wb') as w:
            w.write(encryptedFile)
        
    
    