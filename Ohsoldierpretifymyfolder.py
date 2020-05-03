import os

def removeFiles(filen):
    DNotDis = open(filen)
    l = (DNotDis.read())
    var = (l.split('\n'))
    DNotDis.close()
    return var

def army(pathn, filen, ext):
    os.chdir(pathn)
    count = 0
    var = removeFiles(filen)
    for f in os.listdir():
         f_name, f_ext = os.path.splitext(f)
         if f_ext == f'.{ext}':
             newName = f'{str(count)}{f_ext}'
             count += 1
             os.rename(f,newName)
             pass
         if f_name not in var:
             tn = f_name.title()
             new_name = f'{tn}{f_ext}'
         else:
             new_name = f'{f_name}{f_ext}'
         os.rename(f,new_name)

if __name__ == '__main__':

    pathn= "C:/Users/BHARAT/PycharmProjects/first"
    filen= "abstract12.py"
    ext= ".mp3"
    army(pathn,filen,ext)

