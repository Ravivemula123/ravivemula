import json
file='/home/agile/Desktop/project1/accounting.json'
# with open(file ,'r') as f:
#     obj =json.loads(f)
#     print(obj)
output=[]
quzz={}
quzz1={}
r=[]
y=[]
with open(file, 'r') as f:
    file1 = json.load(f)

    for question ,answer in file1.items():
        # print(question)
        x1=question.replace("####","").replace("Q","")
        # print(x1)
        res = [sub.replace('- [ ]', '') if '- [ ]' in sub  else sub for sub in answer]
        #print(res)
        quzz={"question":x1,"options":res}
        for data in res:
            if data.startswith('- [x]'):
                quzz['answer'] = data
                #print(quzz) 
            if data.startswith("[source]") or data.startswith("[reference]"):
                quzz['reference'] = data
            else:
                print("")
        y.append(quzz)
        quzz1["accounting"]=y
    
    # print(quzz1)
with open('accounting3.json', 'w') as f:
    data = json.dump(quzz1,f)
print("it is sucessfull")
                
                 

        

        # # print(res) 
        # if len(answer)==4:
        # if len(answer)==4:
        #     r.append(answer[4])
        #     pr 


#         for a in answer:         
#             if a.startswith("- [x]"):
#                 # print(a)
#                 y=a.replace("- [x]","")
#                 #print(y)
#                 #pass             
#                 quzz={"Question":x1,"Option":res,"Answer":y,"reference":answer}   
#         x.append(quzz) 
#         quzz1["accounting"]=x
#     #print(quzz1)                           
# with open('accounting1.json', 'w') as f:
#     data = json.dump(quzz1,f)
# print("it is sucessfull")