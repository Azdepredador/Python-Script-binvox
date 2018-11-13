import glob
from subprocess import check_output


def runShell(obj):
    check_output("cd C:\Users\Prestador\Documents\Zernike & binvox.exe c:\Users\Prestador\Desktop\Objetos3D\\"+obj, shell=True)
    

def readBinvox(binvox):
    with open(binvox, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(binvox, 'w') as fout:
        fout.writelines(data[1:])

if __name__ == "__main__":
    for f in glob.glob("*.binvox"):  
        readBinvox(f)  
    pass
