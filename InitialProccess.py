import pandas as pd
import numpy as np

#extract genes from all the genes

d = pd.read_csv("Desktop/genes of gene families .csv")
x = d.values
#X=X[:,1:20532]
for i in range(len(x)):
    s=x[i][0]
    s=s[0:20]
    x[i][0]=s


#a=[]
from Bio import SeqIO

readfile="C:/Users/Asus/Downloads/56253-gene(1).fasta"
file="Desktop/assump.fasta"

with open(readfile) as read_file, open(file, 'a') as fill:
    recordss=SeqIO.parse(readfile, 'fasta')
    for re in recordss:
        for i in range(len(x)):
            if(x[i][0] in re.description):
                SeqIO.write(re, fill, "fasta")

            
# it must contain 1775 genes
            
fh = open("Desktop/assump.fasta")
n = 0
for line in fh:
    if line.startswith(">"):
        n += 1
fh.close()
#######################
a=[]
from Bio import SeqIO

#"C:/Users/Asus/Saccharum_officinarum_LA_Purple.faa"
readfile="Desktop/assump.fasta"


with open(readfile) as read_file:
    recordss=SeqIO.parse(readfile, 'fasta')
    for re in recordss:
        for i in range(len(x)):
            if(x[i][0] in re.description):
                a.append(x[[i]])
                
p=pd.DataFrame(a)
p.to_csv('Desktop/gen.csv', sep=",", index= False)
pp = pd.read_csv('Desktop/gen.csv')
# Make it numpy array essential for the libraries
xx = pp.values

for i in range(len(xx)):
    s=str(xx[i])
    s=s[5:25]
    xx[i]=s

ss=pd.DataFrame(xx)
ss.to_csv('Desktop/g.csv', sep=",", index= False)

####

p1=pd.DataFrame(x)
p1.to_csv('Desktop/genf.csv', sep=",", index= False)

import pandas as pd
import numpy as np
from Bio import SeqIO
import re

#put all genes of a gene family in one fasta file
import os

DIR = 'E:\sugarcane\missed genes'

oh = open('E:\missonefile.fasta', 'w')
for f in os.listdir(DIR):
    fh = open(os.path.join(DIR, f))
    for line in fh:
        oh.write(line)
    fh.close()
oh.close()

    
        
readfile="E:\missonefile.fasta"
file="E:\missonefilechanged.fasta"

with open(readfile) as read_file, open(file, 'w') as fill:
    records = SeqIO.parse(readfile, 'fasta')    
    for record in records:
        s = record.description
        m =re.search("Name: (.+?), Type:",s)
        record.id = m.group(1)
        m1 =re.search("Chr: (.+?),",s)
        record.description = m1.group(1)        
        SeqIO.write(record, fill, 'fasta')

#######################


readfiles="E:\highnumberg.fasta"
files="E:\highnumbergchanged.fasta"

with open(readfiles) as read_file, open(files, 'w') as fill:
    records = SeqIO.parse(readfiles, 'fasta')    
    for record in records:
        v = record.description
        start = v.find("Soffic")
        m = v[start:start+20]
        record.id = m
        st = v.find("Purple") +len("Purple")+2
        m1 = v[st:st+3]
        if(m1[2]== '|' ):
            m1=m1[0:2]
        record.description = m1       
        SeqIO.write(record, fill, 'fasta')

####################
#Whole gene file

readfile="E:\highnumbergchanged.fasta"
file="E:\merged.fasta"   #copy of missones

with open(readfile) as read_file, open(file, 'a') as fill:
    recordss=SeqIO.parse(readfile, 'fasta')
    for re in recordss:
        SeqIO.write(re, fill, "fasta")


            
# it must contain 1775 genes
            
fh = open("E:\merged.fasta")
n = 0
for line in fh:
    if line.startswith(">"):
        n += 1
fh.close()

            
################
# genes on each homo chromosomes ci(1,..10)
for j  in range(1,11):
    globals()["c"+ str(j)]=[]
    
for i in range(len(x)):
    for j in range(1,12):
        if(((int(x[i][1]/8)) == (j-1)) & ((x[i][1]%8) != 0)): 
            globals()["c" + str(j)].append(x[[i]])
        if(((x[i][1]/8) == (j-1)) & ((x[i][1]%8) == 0)): 
             globals()["c" + str(j-1)].append(x[[i]])
#############

#genes on each family 
# 286 gene family 
                            
#family of 8                
d8=pd.read_csv("Desktop/gfam8.csv")                
x8=d8.values
for i in range(len(x8)):
    s8=x8[i][0]
    s8=s8[0:20]
    x8[i][0]=s8

for j  in range(1,7):
    globals()["f8y"+ str(j)]=[]

count=0
for i in range(len(x8)):
    if(x8[i,0]=='a family'):
        count=count+1
        for j in range(1,9):
            globals()["f8y"+ str(count)].append(x8[[i+j]])

readf="E:/sugerc/merged.fasta"
for j  in range(1,7):
    fil="E:/sugerc/family of 8/f8y"+ str(j) +".fasta"    
    with open(readf) as read_file, open(fil, 'a') as fll:
        recordss=SeqIO.parse(readf, 'fasta')
        for re in recordss:
            for i in range(8):
                if( globals()["f8y"+ str(j)][i][0][0] in re.id):
                    SeqIO.write(re, fll, "fasta")
       
#family of 7         
d7=pd.read_csv("Desktop/gfam7.csv")                
x7=d7.values

for i in range(len(x7)):
    s7=x7[i][0]
    s7=s7[0:20]
    x7[i][0]=s7

for j  in range(1,48):
    globals()["f7y"+ str(j)]=[]

c=0
for i in range(len(x7)):
    if(x7[i,0]=='a family'):
        c=c+1
        for j in range(1,8):
            globals()["f7y"+ str(c)].append(x7[[i+j]])
            

for j  in range(1,48):
    fil7="E:/sugerc/family of 7/f7y"+ str(j) +".fasta"    
    with open(readf) as read_file, open(fil7, 'a') as fll7:
        recordss=SeqIO.parse(readf, 'fasta')
        for re in recordss:
            for i in range(7):
                if( globals()["f7y"+ str(j)][i][0][0] in re.id):
                    SeqIO.write(re, fll7, "fasta")
       
#family of 6         
d6=pd.read_csv("Desktop/gfam6.csv")                
x6=d6.values
for i in range(len(x6)):
    s6=x6[i][0]
    s6=s6[0:20]
    x6[i][0]=s6


for j  in range(1,234):
    globals()["f6y"+ str(j)]=[]

coo=0
for i in range(len(x6)):
    if(x6[i,0]=='a family'):
        coo=coo+1
        for j in range(1,7):
            globals()["f6y"+ str(coo)].append(x6[[i+j]])
            

for j  in range(1,234):
    fil6="E:/sugerc/family of 6/f6y"+ str(j) +".fasta"    
    with open(readf) as read_file, open(fil6, 'a') as fll6:
        recordss=SeqIO.parse(readf, 'fasta')
        for re in recordss:
            for i in range(6):
                if( globals()["f6y"+ str(j)][i][0][0] in re.id):
                    SeqIO.write(re, fll6, "fasta")
       
 