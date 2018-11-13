import glob
from subprocess import check_output


def runShell(obj):
    check_output("cd C:\Users\Prestador\Documents\Zernike & binvox.exe c:\Users\Prestador\Desktop\Objetos3D\\"+obj, shell=True)
    

if __name__ == "__main__":
    for f in glob.glob("*.binvox"):  
        print(f)
    
    pass
