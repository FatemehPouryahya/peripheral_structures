for j  in range(1,11):
    globals()["b"+ str(j)]=[]
    globals()["tnofb"+ str(j)]=[]

#on ubuntu   
###########################
    
#family of 8
from Bio import SeqIO
import dendropy
from dendropy.interop import raxml

for j  in range(1,7):
    globals()["taxa8n"+ str(j)]=[]
    
            
for j  in range(1,7):
    globals()["bp8nont"+ str(j)]=[]        

for j  in range(1,7):
    output="/mnt/e/sugerc/family of 8 alignment/f8y"+ str(j)+"-aligned.fasta"
    globals()["data8y"+ str(j)]=dendropy.DnaCharacterMatrix.get(path=output, schema="fasta")
    rx = raxml.RaxmlRunner()
    globals()["tree8y"+ str(j)] = rx.estimate_tree(char_matrix= globals()["data8y"+ str(j)], raxml_args=["--no-bfgs"])
    globals()["tree8ybp"+ str(j)]=dendropy.Tree.encode_bipartitions(globals()["tree8y"+ str(j)])
    for i in range(len(globals()["tree8ybp"+ str(j)])):        
        if(globals()["tree8ybp"+ str(j)][i].is_trivial()== False):
             globals()["bp8nont"+ str(j)].append(globals()["tree8ybp"+ str(j)][i])
    cc=0
    with open(output) as read_file:
        records = SeqIO.parse(output, 'fasta')    
        for record in records:
            v = record.description        
            globals()["taxa8n"+ str(j)].append(v[len(v)-1])
            cc=v[len(v)-3:len(v)-1]
    if(cc != "10"):
        cc=cc[len(cc)-1]        
    globals()["b"+ str(cc)].append(globals()["bp8nont"+ str(j)])
    globals()["t8namspc"+ str(j)] = dendropy.TaxonNamespace(globals()["taxa8n"+ str(j)])
    globals()["tnofb"+ str(cc)].append(globals()["t8namspc"+ str(j)])    
    
    
#family of 7
from Bio import SeqIO
import dendropy
from dendropy.interop import raxml

for j  in range(1,48):
    globals()["taxa7n"+ str(j)]=[]
    
            
for j  in range(1,48):
    globals()["bp7nont"+ str(j)]=[]        

for j  in range(1,48):
    output="/mnt/e/sugerc/family of 7 alignment/f7y"+ str(j)+"-aligned.fasta"
    globals()["data7y"+ str(j)]=dendropy.DnaCharacterMatrix.get(path=output, schema="fasta")
    rx = raxml.RaxmlRunner()
    globals()["tree7y"+ str(j)] = rx.estimate_tree(char_matrix= globals()["data7y"+ str(j)], raxml_args=["--no-bfgs"])
    globals()["tree7ybp"+ str(j)]=dendropy.Tree.encode_bipartitions(globals()["tree7y"+ str(j)])
    for i in range(len(globals()["tree7ybp"+ str(j)])):        
        if(globals()["tree7ybp"+ str(j)][i].is_trivial()== False):
             globals()["bp7nont"+ str(j)].append(globals()["tree7ybp"+ str(j)][i])
    cc=0
    with open(output) as read_file:
        records = SeqIO.parse(output, 'fasta')    
        for record in records:
            v = record.description        
            globals()["taxa7n"+ str(j)].append(v[len(v)-1])
            cc=v[len(v)-3:len(v)-1]
    if(cc != "10"):
        cc=cc[len(cc)-1]        
    globals()["b"+ str(cc)].append(globals()["bp7nont"+ str(j)])                     
    globals()["t7namspc"+ str(j)] = dendropy.TaxonNamespace(globals()["taxa7n"+ str(j)])
    globals()["tnofb"+ str(cc)].append(globals()["t7namspc"+ str(j)])    
    
#family of 6
from Bio import SeqIO
import dendropy
from dendropy.interop import raxml

for j  in range(1,234):
    globals()["taxa6n"+ str(j)]=[]
    
            
for j  in range(1,234):
    globals()["bp6nont"+ str(j)]=[]        

for j  in range(1,234):
    output="/mnt/e/sugerc/family of 6 alignment/f6y"+ str(j)+"-aligned.fasta"
    globals()["data6y"+ str(j)]=dendropy.DnaCharacterMatrix.get(path=output, schema="fasta")
    rx = raxml.RaxmlRunner()
    globals()["tree6y"+ str(j)] = rx.estimate_tree(char_matrix= globals()["data6y"+ str(j)], raxml_args=["--no-bfgs"])
    globals()["tree6ybp"+ str(j)]=dendropy.Tree.encode_bipartitions(globals()["tree6y"+ str(j)])
    for i in range(len(globals()["tree6ybp"+ str(j)])):        
        if(globals()["tree6ybp"+ str(j)][i].is_trivial()== False):
             globals()["bp6nont"+ str(j)].append(globals()["tree6ybp"+ str(j)][i])
    cc=0            
    with open(output) as read_file:
        records = SeqIO.parse(output, 'fasta')    
        for record in records:
            v = record.description        
            globals()["taxa6n"+ str(j)].append(v[len(v)-1])
            cc=v[len(v)-3:len(v)-1]
    if(cc != "10"):
        cc=cc[len(cc)-1]        
    globals()["b"+ str(cc)].append(globals()["bp6nont"+ str(j)])              
    globals()["t6namspc"+ str(j)] = dendropy.TaxonNamespace(globals()["taxa6n"+ str(j)])
    globals()["tnofb"+ str(cc)].append(globals()["t6namspc"+ str(j)])    
    
###############################
    
file="/mnt/e/sugerc/Non-trivial bipartitions"
with open(file, "a") as fl:
    for k in range(1,11):
        fl.write("All non-trivial bipartitions on homologous chromosomes of chromosome "+ str(k)+"\n")
        fl.write("\n")
        for i in range(len(globals()["b"+ str(k)])):
            for j in range(len(globals()["b"+ str(k)][i])):
                fl.write(globals()["b"+ str(k)][i][j].leafset_as_newick_string(taxon_namespace= globals()["tnofb"+ str(k)][i], preserve_spaces=False, quote_underscores=True)+"\n")
            fl.write("\n")
        fl.write("\n")    
    fl.write("\n")    
    
########################
# print everything extensions, ratio, and wights

file="/mnt/e/sugerc/Non-trivial bipartitions-expanded- with weigh"
labels=["A","B","C","D","E","F","G","H"]

with open(file, "a") as fl:
    for k in range(1,11):
        fl.write("All non-trivial bipartitions on homologous chromosomes of chromosome "+ str(k)+"\n")
        fl.write("\n")
        for i in range(len(globals()["b"+ str(k)])):
            if(len(globals()["b"+ str(k)][i])==5):
                fl.write("A family with 8 genes \n")
            if(len(globals()["b"+ str(k)][i])==4):
                fl.write("A family with 7 genes \n")
            if(len(globals()["b"+ str(k)][i])==3):
                fl.write("A family with 6 genes \n")
            A1= A2= a1= a2= a3 =0
            O1= O2= o1= o2= o3 =0
            E1= E2= E3= e1= e2= e3 =0
            for j in range(len(globals()["b"+ str(k)][i])):
                t=globals()["b"+ str(k)][i][j].leafset_as_newick_string(taxon_namespace= globals()["tnofb"+ str(k)][i], preserve_spaces=False, quote_underscores=True)
                d=t.find("), (")
                if(len(globals()["b"+ str(k)][i])==5):
                    if(d==6 or d==18):
                        fl.write(t+" 945"+"\n")
                        E1 +=1
                    if(d==9 or d==15):
                        fl.write(t+" 315"+"\n")
                        E2 +=1
                    if(d==12 ):
                        fl.write(t+" 225"+"\n")
                        E3 +=1
                a=[]
                u=[]
                for p in labels:
                    if(p not in t):
                        a.append(p)                
                if(len(a)==1):
                    if(d==6 or d==15):
                        fl.write(t[:d] +", " +a[0] + t[d:]+" 105"+"\n")
                        fl.write(t[:d+4]+ a[0] +", "+ t[d+4:]+" 105"+"\n")
                        A1 +=2                        
                    if(d==9 or d==12):
                        fl.write(t[:d] +", " +a[0] + t[d:]+" 45"+"\n")
                        fl.write(t[:d+4]+ a[0] +", "+ t[d+4:]+" 45"+"\n")                        
                        A2 +=2
                if(len(a)==2):
                    if(d==6 or d==12):
                        fl.write(t[:d] +", " +a[0]+", " +a[1] + t[d:]+" 15"+"\n")
                        fl.write(t[:d+4]  +a[0]+", " +a[1]  +", "+ t[d+4:]+" 15"+"\n")
                        fl.write(t[:d] +", " +a[0] +"), (" +a[1]+", " + t[d+4:]+" 15"+"\n")
                        fl.write(t[:d] +", " +a[1] +"), (" +a[0]+", " + t[d+4:]+" 15"+"\n") 
                        O1 +=4
                    if(d==9):
                        fl.write(t[:d] +", " +a[0]+", " +a[1] + t[d:]+" 9"+"\n")
                        fl.write(t[:d+4]  +a[0]+", " +a[1]  +", "+ t[d+4:]+" 9"+"\n")
                        fl.write(t[:d] +", " +a[0] +"), (" +a[1]+", " + t[d+4:]+" 9"+"\n")
                        fl.write(t[:d] +", " +a[1] +"), (" +a[0]+", " + t[d+4:]+" 9"+"\n")
                        O2 +=4
                if(j==len(globals()["b"+ str(k)][i])-1):
                    for g in t:
                        if((g !="(") & (g!=")") & (g!=" ") & (g!=";") & (g!=",")):
                           u.append(g)
                    if(len(globals()["b"+ str(k)][i])==4):    
                        fl.write("(("+u[0]+", "+a[0]+"), ("+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+", "+ u[6]+"));"+" 945"+"\n")
                        fl.write("(("+u[1]+", "+a[0]+"), ("+ u[0]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+", "+ u[6]+"));"+" 945"+"\n")
                        fl.write("(("+u[2]+", "+a[0]+"), ("+ u[0]+", "+ u[1]+", "+ u[3]+", "+ u[4]+", "+ u[5]+", "+ u[6]+"));"+" 945"+"\n")
                        fl.write("(("+u[3]+", "+a[0]+"), ("+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[4]+", "+ u[5]+", "+ u[6]+"));"+" 945"+"\n")
                        fl.write("(("+u[4]+", "+a[0]+"), ("+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[5]+", "+ u[6]+"));"+" 945"+"\n")
                        fl.write("(("+u[5]+", "+a[0]+"), ("+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[6]+"));"+" 945"+"\n")
                        fl.write("(("+u[6]+", "+a[0]+"), ("+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 945"+"\n")
                        a1=1/(A1+(A2*(105/45))+(7*(105/945))) #weight for bip with 720 tree
                        a2=1/(A2+(A1*(45/105))+(7*(45/945))) #weight for bip with 288 tree
                        a3=(1/7)*(1-((A1*a1)+(A2*a2)))  #weight for bip with 4320 tree
                        #fl.write(str(A1)+" "+str(A2)+"\n")
                        fl.write("here: \n")
                        fl.write("a1 is "+ str(a1)+" a2 is "+str(a2)+" a3 is "+str(a3)+ "\n")
                    if(len(globals()["b"+ str(k)][i])==3):
                        fl.write("(("+u[0]+", "+a[0]+", "+a[1]+"), ("+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[0]+", "+a[0]+"), ("+a[1]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[0]+", "+a[1]+"), ("+a[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[1]+", "+a[0]+", "+a[1]+"), ("+ u[0]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[1]+", "+a[0]+"), ("+a[1]+", "+ u[0]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[1]+", "+a[1]+"), ("+a[0]+", "+ u[0]+", "+ u[2]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[2]+", "+a[0]+", "+a[1]+"), ("+ u[0]+", "+ u[1]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[2]+", "+a[0]+"), ("+a[1]+", "+ u[0]+", "+ u[1]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[2]+", "+a[1]+"), ("+a[0]+", "+ u[0]+", "+ u[1]+", "+ u[3]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[3]+", "+a[0]+", "+a[1]+"), ("+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[3]+", "+a[0]+"), ("+a[1]+", "+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[3]+", "+a[1]+"), ("+a[0]+", "+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[4]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[4]+", "+a[0]+", "+a[1]+"), ("+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[4]+", "+a[0]+"), ("+a[1]+", "+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[4]+", "+a[1]+"), ("+a[0]+", "+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[5]+"));"+" 105"+"\n")
                        fl.write("(("+u[5]+", "+a[0]+", "+a[1]+"), ("+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+"));"+" 105"+"\n")
                        fl.write("(("+u[5]+", "+a[0]+"), ("+a[1]+", "+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+"));"+" 105"+"\n")
                        fl.write("(("+u[5]+", "+a[1]+"), ("+a[0]+", "+ u[0]+", "+ u[1]+", "+ u[2]+", "+ u[3]+", "+ u[4]+"));"+" 105"+"\n")
                        o1=1/(O1+(O2*(15/9))+(18*(15/105))) #weight for bip with 96 tree
                        o2=1/(O2+(O1*(9/15))+(18*(9/105))) #weight for bip with 36 tree
                        o3=(1/18)*(1-((O1*o1)+(O2*o2)))  #weight for bip with 360 tree
                        #fl.write(str(O1)+" "+str(O2)+"\n")
                        fl.write("here: \n")
                        fl.write("o1 is "+ str(o1)+" o2 is "+str(o2)+" o3 is "+str(o3)+ "\n")
                    if(len(globals()["b"+ str(k)][i])==5):
                        e1=1/(E1+(E2*(945/315))+(E3*(945/225))) #weight for bip with 10080 tree
                        e2=1/(E2+(E1*(315/945))+(E3*(315/225))) #weight for bip with 2160 tree
                        if(E3 !=0):
                            e3=(1/E3)*(1-((E1*e1)+(E2*e2)))  #weight for bip with 2304 tree
                        else:
                            e3=0
                        #fl.write(str(O1)+" "+str(O2)+"\n")
                        fl.write("here: \n")
                        fl.write("e1 is "+ str(e1)+" e2 is "+str(e2)+" e3 is "+str(e3)+ "\n")                        

            #fl.write("\n")    
            fl.write("\n")
        fl.write("\n")    
    fl.write("\n")    
  