import itertools


print ("Starting pre-processing")
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
# with open("authorPair.txt",'w') as res:

# list(itertools.combinations(a,2))
# def pro():
#     result = []
#     with open("authorPair.txt", 'w') as res:
#         with open("authorXMLNoQ.txt", 'r') as f:
#             for line in f:
#                 LengRes = len(result)
#                 result.sort()
#                 if "##" in line and LengRes > 0:
#                     if LengRes == 1:
#                         # print (result)
#                         result = []
#                         continue
#                     reL = itertools.combinations(result, 2)
#                     for author_pairs in reL:
#                         #=====res.write('"%s" "%s"\t\n'%(author_pairs[0],author_pairs[1],))
#                         print('"%s" "%s"\t\n'%(author_pairs[0],author_pairs[1],))
#                     result = []
#
#                 else:
#                     result.append(line.strip('\n'))
#
#
# def main():
#     pro()
# if __name__ == "__main__":
#     main()

        # print ("Starting Reading")
    # with open("authorXML.txt",'w') as res:
    #     with open('dblp.xml', 'r') as f:
    #         for _,line in enumerate(f, 1):
    #             if "<au" in line:
    #                 res.write(line.strip('<author>')[:-10]+'\n')


    # print ("Starting Reading")
    # with open("authorXML.txt",'w') as res:
    #     with open('dblp.xml', 'r') as f:
    #         for _,line in enumerate(f, 1):
    #             if '<ar' in line:
    #                 res.write("------\n")
    #             if "<au" in line:
    #                 res.write(line.strip('<author>')[:-10]+'\n')

# print ("Starting pre-processing")
# result = []
# with open("author.txt",'w') as res:
#     with open('dblp.xml', 'r') as f:
#         for line in f:
#             if '<au' not in line:
#                 res.write("###\n")
#             if "<au" in line:
#                 #newLine = line.strip('<author>')[:-10]
#                 newLine = line[:-10]
#                 newLine = newLine.split('>', 1)[-1]
#                 res.write(newLine + '\n')
