#!/usr/bin/env python
# coding: utf-8
#on ubuntu

# In[1]:


#family of 8
from Bio import SeqIO
import dendropy
from dendropy.interop import raxml

for j  in range(1,11): 
    globals()["bb"+ str(j)]=dendropy.TreeList()

##for j  in range(1,7):
  ##  globals()["taxa8n"+ str(j)]=[]
    
            
##for j  in range(1,7):
 ##   globals()["bp8nont"+ str(j)]=[]        

for j  in range(1,7):
    output="/mnt/e/sugerc/family of 8 alignment/f8y"+ str(j)+"-aligned.fasta"
    globals()["data8y"+ str(j)]=dendropy.DnaCharacterMatrix.get(path=output, schema="fasta")
    rx = raxml.RaxmlRunner()
    globals()["tree8y"+ str(j)] = rx.estimate_tree(char_matrix= globals()["data8y"+ str(j)], raxml_args=["--no-bfgs"])
    #globals()["tree8ybp"+ str(j)]=dendropy.Tree.encode_bipartitions(globals()["tree8y"+ str(j)])
    #for i in range(len(globals()["tree8ybp"+ str(j)])):        
     #   if(globals()["tree8ybp"+ str(j)][i].is_trivial()== False):
      #       globals()["bp8nont"+ str(j)].append(globals()["tree8ybp"+ str(j)][i])
    cc=0
    with open(output) as read_file:
        records = SeqIO.parse(output, 'fasta')    
        for record in records:
            v = record.description        
            ##globals()["taxa8n"+ str(j)].append(v[len(v)-1])
            cc=v[len(v)-3:len(v)-1]
    if(cc != "10"):
        cc=cc[len(cc)-1]  # cc homeology set 1-10 # change globals()["tree8y"+ str(j)] taxon names one by one
    for w in range(globals()["tree8y"+ str(j)].taxon_namespace.__len__()):
        #print(w)
        globals()["tree8y"+ str(j)].taxon_namespace[w].label=globals()["tree8y"+ str(j)].taxon_namespace[w].__str__()[len(globals()["tree8y"+ str(j)].taxon_namespace[w].__str__())-2:len(globals()["tree8y"+ str(j)].taxon_namespace[w].__str__())-1]
    globals()["bb"+ str(cc)].append(globals()["tree8y"+ str(j)]) # make b TreeList #bk homeology set b1-b10  


# In[2]:


#family of 7
from Bio import SeqIO
import dendropy
from dendropy.interop import raxml

#for j  in range(1,48):
   # globals()["taxa7n"+ str(j)]=[]
    
            
#for j  in range(1,48):
 #   globals()["bp7nont"+ str(j)]=[]        

for j  in range(1,48):
    output="/mnt/e/sugerc/family of 7 alignment/f7y"+ str(j)+"-aligned.fasta"
    globals()["data7y"+ str(j)]=dendropy.DnaCharacterMatrix.get(path=output, schema="fasta")
    rx = raxml.RaxmlRunner()
    globals()["tree7y"+ str(j)] = rx.estimate_tree(char_matrix= globals()["data7y"+ str(j)], raxml_args=["--no-bfgs"])
    #globals()["tree7ybp"+ str(j)]=dendropy.Tree.encode_bipartitions(globals()["tree7y"+ str(j)])
    #for i in range(len(globals()["tree7ybp"+ str(j)])):        
     #   if(globals()["tree7ybp"+ str(j)][i].is_trivial()== False):
      #       globals()["bp7nont"+ str(j)].append(globals()["tree7ybp"+ str(j)][i])
    cc=0
    with open(output) as read_file:
        records = SeqIO.parse(output, 'fasta')    
        for record in records:
            v = record.description        
       #     globals()["taxa7n"+ str(j)].append(v[len(v)-1])
            cc=v[len(v)-3:len(v)-1]
    if(cc != "10"):
        cc=cc[len(cc)-1]
    for w in range(globals()["tree7y"+ str(j)].taxon_namespace.__len__()):
        #print(w)
        globals()["tree7y"+ str(j)].taxon_namespace[w].label=globals()["tree7y"+ str(j)].taxon_namespace[w].__str__()[len(globals()["tree7y"+ str(j)].taxon_namespace[w].__str__())-2:len(globals()["tree7y"+ str(j)].taxon_namespace[w].__str__())-1]
    globals()["bb"+ str(cc)].append(globals()["tree7y"+ str(j)]) # make b TreeList #bk homeology set b1-b10  


# In[3]:


#family of 6
from Bio import SeqIO
import dendropy
from dendropy.interop import raxml

#for j  in range(1,234):
 #   globals()["taxa6n"+ str(j)]=[]
    
            
#for j  in range(1,234):
 #   globals()["bp6nont"+ str(j)]=[]        

for j  in range(1,234):
    output="/mnt/e/sugerc/family of 6 alignment/f6y"+ str(j)+"-aligned.fasta"
    globals()["data6y"+ str(j)]=dendropy.DnaCharacterMatrix.get(path=output, schema="fasta")
    rx = raxml.RaxmlRunner()
    globals()["tree6y"+ str(j)] = rx.estimate_tree(char_matrix= globals()["data6y"+ str(j)], raxml_args=["--no-bfgs"])
    #globals()["tree6ybp"+ str(j)]=dendropy.Tree.encode_bipartitions(globals()["tree6y"+ str(j)])
    #for i in range(len(globals()["tree6ybp"+ str(j)])):        
     #   if(globals()["tree6ybp"+ str(j)][i].is_trivial()== False):
      #       globals()["bp6nont"+ str(j)].append(globals()["tree6ybp"+ str(j)][i])
    cc=0            
    with open(output) as read_file:
        records = SeqIO.parse(output, 'fasta')    
        for record in records:
            v = record.description        
            #globals()["taxa6n"+ str(j)].append(v[len(v)-1])
            cc=v[len(v)-3:len(v)-1]
    if(cc != "10"):
        cc=cc[len(cc)-1]
    for w in range(globals()["tree6y"+ str(j)].taxon_namespace.__len__()):
        #print(w)
        globals()["tree6y"+ str(j)].taxon_namespace[w].label=globals()["tree6y"+ str(j)].taxon_namespace[w].__str__()[len(globals()["tree6y"+ str(j)].taxon_namespace[w].__str__())-2:len(globals()["tree6y"+ str(j)].taxon_namespace[w].__str__())-1]
    globals()["bb"+ str(cc)].append(globals()["tree6y"+ str(j)])   


# In[10]:

# input ready
for a in range(1,11):
    pat="/mnt/c/Users/Asus/Desktop/astral/Astral/Mine-sugarcane/homeologySet"+str(a)+".tre"
    globals()["bb"+str(a)].write(path=pat,schema="newick")


# In[14]:


# outputs of cmd call astral
import dendropy as dn
for i in range(1,11):
    t=dn.Tree.get(path="/mnt/c/Users/Asus/Desktop/astral/Astral/Mine-sugarcane/outputs/OutputHomeologySet"+str(i)+".tre",schema="newick")
    t.print_plot()
    print(t.as_string(schema="newick"))


# In[15]:


import dendropy as dn
for i in range(1,11):
    t=dn.Tree.get(path="/mnt/c/Users/Asus/Desktop/astral/Astral/Mine-sugarcane/outputs/OutputHomeologySet"+str(i)+".tre",schema="newick")
    #t.print_plot()
    print(t.as_string(schema="newick"))


