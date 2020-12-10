name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
dct = dict()

for line in handle:
    if(line.startswith("From:")):
        lst = line.split()
        dct[lst[1]] = dct.get(lst[1],0)+1
tmpLst = list()
for k,v in dct.items():
    tmpLst.append((v,k))
tmpLst = sorted(tmpLst, reverse=True)
for v,k in tmpLst[:1]:
    print(k,v)
