
#!/usr/bin/env python
import itertools
import sys
# input comes from STDIN (standard input)
result = []


for line in sys.stdin:
    line = line.strip()
    #print(line,"!!!!!!!!!!!!")
    LengRes = len(result)
    result.sort()
    if "##" in line and LengRes > 0:
        if LengRes == 1:
            # print (result)
            result = []
            continue
        reL = itertools.combinations(result, 2)
        for author_pairs in reL:
            # =====res.write('"%s" "%s"\t\n'%(author_pairs[0],author_pairs[1],))
            #print('"%s" "%s"\t%s' % ( author_pairs[0], author_pairs[1] , '1' , ))
            s = str('"' + author_pairs[0] +'" "'+ author_pairs[1] + '"' + '\t1')
            print (s)
        result = []

    else:
        result.append(line.strip('\n'))





# #!/usr/bin/env python
# import itertools
# # input comes from STDIN (standard input)
# result = []

# with open("authorXMLNoQ.txt", 'r') as f:
#     for line in f:
#         LengRes = len(result)
#         result.sort()
#         if "##" in line and LengRes > 0:
#             if LengRes == 1:
#                 # print (result)
#                 result = []
#                 continue
#             reL = itertools.combinations(result, 2)
#             for author_pairs in reL:
#                 # =====res.write('"%s" "%s"\t\n'%(author_pairs[0],author_pairs[1],))
#                 print('"%s" "%s"\t%s\n' % ( author_pairs[0], author_pairs[1] , '1' , ))
#             result = []

#         else:
#             result.append(line.strip('\n'))

