import os
import numpy as np
from natsort import natsorted

path = input(r'Directory: ')
YN = input('Start? Y/N: ')
if not YN.lower() == 'j':
    exit

files = os.listdir(path)
Sfiles = []
destarr = []
sourcearr = []
Afiles = []
Ffiles = []

##set base values
a = 0
while a < len(files):
    filename, fileExtension = os.path.splitext(files[a])
    if not filename.isdecimal():
        sourcearr.append(os.path.join(files[a]))
    elif int(filename) > len(files) + 1:
        sourcearr.append(os.path.join(files[a]))
    else:
        Sfiles.append(files[a])
    a += 1

##sortet to two lists
Efiles = [None]*(len(files))

b = 0
while b < len(Sfiles):
    filename, fileExtension = os.path.splitext(Sfiles[b])
    if Efiles[int(filename) - 1] == None:
        Efiles[int(filename) - 1] = Sfiles[b]
    else:
        sourcearr.append(files[b])
    b += 1


##occupied slots into list
c = 0
while c < len(Efiles):
    if Efiles[c] == None:
        Ffiles.append(c)
    c += 1
##print(len(sourcearr))
##print(len(Ffiles))
##free slots into list
d = 0
for Ffile in Ffiles:
    filename, fileExtension = os.path.splitext(sourcearr[d])
    os.rename(os.path.join(path, filename + fileExtension), os.path.join(path, str(Ffile + 1) + fileExtension))
    print(sourcearr[d] + ' --> ' + str(Ffile) + fileExtension)
    d += 1

    
##renamed files

##print("sourcearr:\n")
##print(sourcearr)
##print("Sfiles:\n")
##print(Sfiles)
##print("Efiles:\n")
##print(Efiles)
##print("\nAfiles:\n")
##print(Afiles)
##print("Ffiles:\n")
##print(Ffiles)

os.system('pause')

