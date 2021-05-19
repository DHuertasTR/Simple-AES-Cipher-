from Crypto import Cipher
from Encrypt import Cipher as cp


def desciph(pathFile, password):
    print("file recover")

def ciph(pathFile, password):
    print("response ciphered")
    
def main():
    
    cpp=cp()
    
    cpp.cipher('come','image.jpg')
    
    response= int(input("Ingrese 1 si desea cifrar un archivo, ingrese 2 si desea descifrar un archivo o CTR+c si desea salir"))
    if response==1:
        pathFile=input("ingrese la ruta del archivo")
        password=input("ingrese una contrasena")
        
        ciph(pathFile, password)
    
    elif response==2:
        pathFile=input("ingrese la ruta del archivo")
        password=input("ingrese una contrasena")
        
        desciph(pathFile, password)
    
    else:
        print("ingrese un numero valido")

if __name__ == "__main__":
    main()
    
