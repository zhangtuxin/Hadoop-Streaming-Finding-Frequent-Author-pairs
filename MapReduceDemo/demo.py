import mincemeat
import stopwords
import glob

text_files = glob.glob('./data/*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

# The data source can be any dictionary-like object
datasource = dict((file_name, file_contents(file_name))
                  for file_name in text_files)

def mapfn(k, v):
    for line in v.splitlines():
        info = line.split(':::')
        title = info[2]
        author = info[1].split('::')
        words = title.split()
        for w in words:
            w = w.replace('.','')
            w = w.replace(',','')
            w = w.replace('?','')
            w = w.replace('!','')
            w = w.replace(':','')
            w = w.replace(';','')
            w = w.replace('+','')
            w = w.replace('-',' ')
            w = w.replace('*','')
            w = w.replace('/','')
            w = w.replace('(','')
            w = w.replace(')','')
            w = w.replace('<','')
            w = w.replace('>','')
            w = w.replace('{','')
            w = w.replace('}','')
            w = w.lower()
            if len(w) > 1 and not stopwords.allStopWords.has_key(w):
                for a in author:
                    yield a, w

def reducefn(k, vs):
    result = {}
    for v in vs:
        if result.has_key(v):
            result[v] = result[v] + 1
        else:
            result[v] = 1
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
#print results['Philip S. Yu']
#print results['Donald F. Towsley']
print 'Top 10 terms in Philip S. Yu\'s title'
results = sorted(results['Philip S. Yu'].items(), key = lambda x: x[1], reverse=True)
for i in range(10):
    w, c = results[i]
    print '%s\t%d' % (w, c)
