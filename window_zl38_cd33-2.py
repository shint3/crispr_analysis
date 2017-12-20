import csv
import sys

dict_reads = {}
list_zeroes = []

#open tab file
with open(sys.argv[1], 'U') as tab_file:
    reader = csv.reader(tab_file, delimiter = '\n')

    for i,row in enumerate(reader):

        #save timepoints
        if i == 0:
            col_titles = row[0]
            #print col_titles

        #save sequence and numbers of reads
        else:
            row = row[0].split('\t')
            seq = row[0][78:96]
            reads = row[1:]
            #print seq + '\t' + '\t'.join(reads)

            #if sequence is already there, add numbers of reads together
            if seq in dict_reads:
                for i,read in enumerate(reads):
                    #print i,read
                    dict_reads[seq][i] = dict_reads[seq][i] + int(read)
                #print "yes",dict_reads[seq]

            #if sequence is new, make new entry
            else:
                for read in reads:
                    list_zeroes.append(0)
                dict_reads[seq] = list_zeroes
                list_zeroes = []

                for i,read in enumerate(reads):
                    #print i,read
                    dict_reads[seq][i] = dict_reads[seq][i] + int(read)
                #print "no",dict_reads[seq]

#print timepoints, then sequences and numbers of reads
print col_titles
for seq in dict_reads:
    print seq + '\t' + '\t'.join(map(str,dict_reads[seq]))
