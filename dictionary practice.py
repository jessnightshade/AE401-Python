dic={}
dic={'apple':50,'banana':30}

dic['guava']=40
dic['apple']=55

print(dic['apple'])

dic.pop('apple')

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)
    
for k, v in dic.items():
    print(k,'=>', v)