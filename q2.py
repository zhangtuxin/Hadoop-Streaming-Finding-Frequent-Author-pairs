import itertools
bucket=[]
item = []
count = 0
frqitem = []
threshold = 20
for i in range(1,1002):
    item.append(0)
for i in range(1,1002):
    bucket.append([])

print("Bucket",bucket)
print("item",item)
print("=================")
for i in range(1,1001):
    for k in range(1,1001):
        if k%i ==0:
            bucket[k].append(i)
            item[i] += 1
print("Bucket",bucket)
print("item",item)
print("=================")

for i in range(1,1001):
    if item[i]>=threshold:
        frqitem.append(i)
        item[i] = 0
print ("Freq",frqitem)



c1 = itertools.combinations(frqitem,2)
c1dict = {}

for i in c1:
    c1dict[i] = 0
print ('c1dict :',c1dict)
print("=================")
c1 = itertools.combinations(frqitem,2)
count = 1
for i in c1:
    ite = 0
    for k in range(1,1001):
        if set(i).issubset(set(bucket[k])):
            ite += 1
    c1dict[i] = ite
    count += 1


print ('c1dict :',c1dict)
resultDict = {key: value for key, value in c1dict.items() if value >= 20}
frqitem = []
for key,value in resultDict.items():
    if value >= 20 :
        for n in key:
            if n not in frqitem:
                frqitem.append(n)

print ("Freq: ",frqitem)

print ('resultDict :',resultDict)
print ('Length resultDict :',len(resultDict))
#resultDict = {}
count = 0
num = 3
tmp = None
while len(frqitem) > 0 :
    print("Start processing First P algorithm")
    tmp = None
    c1 = itertools.combinations(frqitem,num)
    num += 1
    c1dict = {}
    for i in c1:
        ite = 0
        for k in range(1, 1001):
            if set(i).issubset(set(bucket[k])):
                ite += 1
        c1dict[i] = ite
    print("for",num-1,"itemset c1dict :",c1dict)
    resultDict = {key: value for key, value in c1dict.items() if value >= 20}
    print("resultDic: ",resultDict)
    print('Length resultDict :', len(resultDict))
    frqitem = []
    for key, value in resultDict.items():
        for n in key:
            if n not in frqitem:
                frqitem.append(n)
    print("Frqitem :",frqitem)
    tmp = resultDict
    resultDict = {}

print("TMP:", tmp)