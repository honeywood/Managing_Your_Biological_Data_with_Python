'''
===================================
searching protein by keywords
===================================
'''
from Bio import Entrez
from Bio import SeqIO
import time
keyword = 'bacteriorhodopsin'
#search proteins in Entrez
Entrez.email = 'zhaojiadong@sygene.cn'
handle = Entrez.esearch(db = 'protein', term = keyword)


record = Entrez.read(handle)
#protein_ids = record['IdList']
id_list = record['IdList'][:20]
id_list1 = ','.join(id_list)
#print(id_list)
#retrive sequence from Entrez
outf = open('protein_searching.gb', 'w')
for id in id_list:
	time.sleep(1)
	handle = Entrez.efetch(db = 'protein', id = id, \
		rettype = 'gb', retmode = 'text').read()
	outf.write(handle)###这样报错()
'''
i = 0
for record in records:
	i += 1
	outf.write('%s\n' % i)
	#print(record)
	for a in record.keys()
		outf.write('%s:%s' % (a, record[a]) + '\n')'''
outf.close()

