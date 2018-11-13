import glob
from subprocess import check_output


def runShell(obj):
    #cmd=check_output("cd", shell=True) #return the path, where there are the objects
    #print()
    check_output("cd C:\Users\Prestador\Documents\Zernike & binvox.exe c:\Users\Prestador\Desktop\Objetos3D\\"+obj, shell=True)
    

if __name__ == "__main__":
    for f in glob.glob("*obj"):
        print(f)  
   # runShell("lab ")
    
    pass
