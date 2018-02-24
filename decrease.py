
#!/usr/bin/env python
import itertools
import sys
# input comes from STDIN (standard input)
result = []
print ('"Starting Reading"')
with open("author.txt", 'w') as f:
    with open("authorXMLNoQ.txt",'r') as f2:
        s="###\n"
        for line in f2:
            line = line.strip()
            print(line,"still doing ")
            LengRes = len(result)
            result.sort()
            if "##" in line and LengRes > 0:
                if LengRes == 1:
                    # print (result)
                    result = []
                    continue
                f.write(s)
                for i in result:
                    f.write(i)

                result = []

            else:
                result.append(line)