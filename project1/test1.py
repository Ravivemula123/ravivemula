import json
file='/home/agile/Desktop/project1/accounting.json'

# with open(file ,'r') as f:
#     obj =json.loads(f)
#     print(obj)


with open(file, 'r') as f:
    file1 = json.load(f)

for question ,answer in file1.items():
    print(answer)
  
 




