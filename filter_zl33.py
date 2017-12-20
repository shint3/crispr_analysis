import csv
import sys

nucs=['A','T','C','G']

d={'cd33_1':"CCTAGCCCTTCTCCTCCACTCCTTTCCTGCTCTCTGCTCACACAGGGAGCCCAGGAAACCTCAGCCTCAGACATGCCGCTGCTGYTGCTGCCCCTGCTGTGGGCAGGTGAGTGACTGCTGGGAGGGGGGTTGTCGGGCTGGGCCAAGCTGACCCTCATTTCCCCACAGGGGCCCTGGCTATGGATCCAAGAGTCAGGCTGGAAGTGCAGGAGTCAGTGACAGTACAGGAGGGTTTGTGCGTCCTTGTGCCCTGCACTTTCTTCCATCCCGTACCCTACCACACCAGGAATTCCCCAGTTCATGGTTACTGGTTCCGGGAAGGAGCCATTGTATCCTTGGACTCTCCAGTGGCCACAAAC"}

genes = ["cd33_1"]
dic={}
cnt={}
num={}
dlst=[]
clst=[]
n=0
p=0
foo=''
poo=2
moo=0
l=[]


if sys.argv[1] in genes:


    ref = d[sys.argv[1]]
    for i,item in enumerate(ref):
        if item not in nucs:
            num[i]=item
    #print num
    

    for item in sys.argv:
        if sys.argv.index(item) > 1:
        
            with open(sys.argv[poo],"U") as f:
                reader=csv.reader(f, delimiter='\t')
                for i,line in enumerate(reader):
                    if i==0:
                        continue
                    else:
                        foo = list(line[0])
                        #iupac= line[0] # remove when removing triple quote
                        
                        for i,item in enumerate(foo):
                            if i in num:
                                #print "before",i, item
                                foo[i]=num[i]
                                #print "after",i, item
                            iupac = ''.join(foo)
                            #print iupac
                            
                    
                    if iupac in dic:
                        n=n+1
                        dic[iupac][moo]= dic[iupac][moo] + int(line[7])
                        cnt[iupac][moo]= cnt[iupac][moo] + float(line[8])
                        #print int(line[7])

                    else:
                        p=p+1
                        for i in range(2,len(sys.argv)):
                            dlst.append(0)
  
                        dic[iupac]=dlst
                        dic[iupac][moo]=int(line[7])

                        for i in range(2,len(sys.argv)):
                            clst.append(0)
                            
                        cnt[iupac]=clst
                        cnt[iupac][moo]=float(line[8])
                        #print "dic ",dic[iupac][moo]
                        #print "cnt ", cnt[iupac][moo]
                        clst=[]
                        dlst=[]
                        
                        
                    #print dic[iupac]
                    #print cnt[iupac]
                                          
                poo = poo+1
                moo = moo + 1
    
else:
    print "unknown gene, please type one of the following: aavs, asxl1, asxl2, tet1, tet2, dnmt3, dnmt19, asxl1"


head = []
for item in sys.argv:
    if ".csv" in item:
        head.append(item.strip('.csv'))
        
print '\t'.join(head)

#print dic
chen=0
for item in cnt:
    for i,num in enumerate(cnt[item]):
        #print i
        if i==0:
            chk=num
        #print "calcs= ", num,'\t', chk, '\t',abs(float(num-chk))
        #print "before= ", dic[item][i]
        if i != 0:
            if abs(float(num-chk)) < 0.10:
                chen=chen+1
                #print chen
                #print dic
        #print "chen before", chen        
    
    
        #print "after= ", dic[item][i]
    if sum(dic[item])>1:
        if len(sys.argv) - chen -3 != 0:
            print item,'\t', '\t'.join(map(str,dic[item]))
    #print "*************************"
    chen=0
    #print "chen after zeroing", chen
    #print len(sys.argv)
        
    



for item in dic:    
    
    if sum(dic[item])> 1:
        continue
        #print item,'\t', '\t'.join(map(str,dic[item]))


#print "number of duplicates =\t", n
#print "number of uniques =\t", p
#print "number of arguments=\t",poo
#print "number of files=\t", moo
