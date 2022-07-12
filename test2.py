import json
file='/home/agile/Desktop/project1/accounting.json'

# with open(file ,'r') as f:
#     obj =json.loads(f)
#     print(obj)
x=[]
quzz1={}

with open(file, 'r') as f:
    file1 = json.load(f)

    for question ,answer in file1.items():
        #print(question)
        x1=question.replace("####","").replace("Q","")
        #print(x)
        res = [sub.replace('- [ ]', '').replace('- [x]','') for sub in answer]

        # print(res)
        
        for a in answer:
            
            if a.startswith("- [x]"):
                # print(a)
                y=a.replace("- [x]","")
                print(y)
                #pass
               
                quzz={"Question":x1,"Option":res,"Answer":y}   
        x.append(quzz) 
        quzz1["accounting"]=x
    print(quzz1)                         
   
with open('accounting2.json', 'w') as f:
    data = json.dump(quzz1,f)
print("it is sucessfull")