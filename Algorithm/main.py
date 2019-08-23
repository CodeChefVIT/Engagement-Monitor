import re
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://number1:1234@engagement-montor-9t1qi.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["engagement-montor"]
collection = db["Admin"]

file = open("chat1.txt",encoding="utf8")
c=0
mem = []
dicti={}
while True:
    line = file.readline()
    x = re.search(r"(\d.*?\,.*?-.*?\:)", line)
    if x:
        r = re.search(r"(-.*?:)",x.group()).group()[2:-1]
        c+=1

        if (r in mem): 
            #print ("Member Exists") 
            for i in dicti:
                if(i==r):
                    a = dicti[i]
                    up = {r:a+1}
                    dicti.update(up)
                    #print(up)
        else:
            mem.append(r)
            up = {r:1}
            dicti.update(up)



    if not line:
        z=0
        
        break
for i in dicti :  
    z+=dicti[i]
print(dicti)
print(z,c)
print(collection.insert_one(dicti))
file.close()