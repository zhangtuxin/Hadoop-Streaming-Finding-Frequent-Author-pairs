import itertools
import heapq

# pre processing xml
result = []
with open("author.txt",'w') as res:
    with open('dblp.xml', 'r') as f:
        s = "###\n"
        for line in f:
            if "<au" in line:
                newLine = line[:-10]
                newLine = newLine.split('>', 1)[-1]
                result.append(newLine)
                #res.write(newLine + '\n')
            else:
                if len(result) > 1:
                    result.sort()
                    res.write(s)
                    for a in result:
                        res.write(a+'\n')
                    result = []
                else:
                    result = []

print ("Starting pre-processing")