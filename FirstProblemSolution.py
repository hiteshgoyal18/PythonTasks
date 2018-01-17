import json
data=json.load(open('data.json'))

// recursive function
def recFunc(data):
    for key in data.keys():
        if(type(data[key])==dict):
            data[key]=recFunc(data[key])
        elif(type(data[key])==list):
            for index in range(len(data[key])):
                data[key][index]=recFunc(data[key][index])
        else:
            if(str(key)=="quantity"):
                data[key]=str(int(data[key]))+'gm'
    return data
                
fp=open('newD.json','w')
newData=recFunc(data)
json.dump(newData,fp)
