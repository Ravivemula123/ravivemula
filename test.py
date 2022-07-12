import re
import json
import csv





file= '/home/agile/Desktop/project/autodesk_fusion.txt'

acrobat= {}
y=[]
key=[]
w=[]
with open(file,'r') as f:
    a=f.readlines()
    cnt=0
    z=[]
    for x in a:
        #key = re.findall("[Q]{1}\w[A-Za-z0-9 .'" ",$()-]*[?]{1}",x)
        if x.startswith("####") :
            key.append(x)
        if x.startswith("- ["):
            y.append(x)
            #cnt=cnt+1
        for i in y:
            #print(i)
            pass
            my_list2 = [y[i:i+4] for i in range(0, len(y), 4)]
        #print(my_list2)
            for k in key:
            #print(k)
                pass
            for d in my_list2:
            #print(d)
                #print(k)
                pass

              
            acrobat[k]=d

print(acrobat)

with open('autodesk_fusion.json', 'w') as f:
    data = json.dump(acrobat,f)

print("it is sucessfull")