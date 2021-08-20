file="E:/sugerc/ranked bipartition each chromosome/bipartition referance.txt"
with open(file, 'r') as f:
    ref = f.read().splitlines()

#convert combination(x) in list
for i in range(len(ref)):
    s=[i for i in ref[i] if i.isalpha()]
    ref[i]=s 
    
    
#xj is the read file 
for k  in range(1,11):
    globals()["file"+ str(k)]="E:/sugerc/ranked bipartition each chromosome/chromosome "+str(k)+".txt" 
    with open(globals()["file"+ str(k)], "r") as globals()["f"+ str(k)]:
        globals()["x"+str(k)]=globals()["f"+ str(k)].read().splitlines()


#have bipartitions as list of list
for k in range(1,11):  
    for i in range(len(globals()["x"+str(k)])):
        if(globals()["x"+str(k)][i][0:2]== '(('):
            s=globals()["x"+str(k)][i]
            A1 = [i for i in s[0:s.find("), (")] if i.isalpha()]
            A2 = [i for i in s[s.find("), (")+4:] if i.isalpha()]
            A3 = s[s.find(";")+2:]
            globals()["x"+str(k)][i]=[A1,A2,A3]

for k in range(1,11):    
    for i in range(len(globals()["x"+str(k)])):
        if(len(globals()["x"+str(k)][i])==3):
            globals()["x"+str(k)][i][0].sort()
            globals()["x"+str(k)][i][1].sort()

#remove the complement of first 35 element in x so that we have only one side (35 element not 70)
woow=[[] for i in range(len(ref))]                   
arra = ["A","B","C","D","E","F","G","H"]           
for i in range(84,len(ref)):
    for j in arra:
        if(j not in ref[i]):
            woow[i].append(j)
            
for i in range(len(woow)):
    woow[i].sort()

w=[]
for i in range(84,119):
    for j in range(84,len(ref)):
        if(woow[i]==ref[j]):
            w.append(j)
    
for i in w:
    del ref[i]        
#############

for k in range(1,11):
    globals()["weight"+str(k)]=[0]*len(ref)
    

for k in range(1,11):
    s=o1=o2=o3=a1=a2=a3=e1=e2=e3=0
    for i in range(len(globals()["x"+str(k)])):
        if(globals()["x"+str(k)][i]=='A family with 7 genes '):
            s=globals()["x"+str(k)][i+17]
            a1=float(s[6:s.find("a2")-1])
            a2=float(s[s.find("a2")+6:s.find("a3")-1])
            a3=float(s[s.find("a3")+6:])
            
        if(globals()["x"+str(k)][i]=='A family with 6 genes '):
            s=globals()["x"+str(k)][i+32]
            o1=float(s[6:s.find("o2")-1])
            o2=float(s[s.find("o2")+6:s.find("o3")-1])
            o3=float(s[s.find("o3")+6:])
            
        if(globals()["x"+str(k)][i]=='A family with 8 genes '):
            s=globals()["x"+str(k)][i+7]
            e1=float(s[6:s.find("e2")-1])
            e2=float(s[s.find("e2")+6:s.find("e3")-1])
            e3=float(s[s.find("e3")+6:]) 
            
        else:
           if(len(globals()["x"+str(k)][i])==3):
               for j in range(len(ref)):    
                   if((globals()["x"+str(k)][i][0]==ref[j]) or (globals()["x"+str(k)][i][1]==ref[j])):
                       if(globals()["x"+str(k)][i][2]=='105'):
                           globals()["weight"+str(k)][j] +=a1
                       if(globals()["x"+str(k)][i][2]=='45'):
                           globals()["weight"+str(k)][j] +=a2
                       if(globals()["x"+str(k)][i][2]=='945'):
                           globals()["weight"+str(k)][j] +=a3
                       if(globals()["x"+str(k)][i][2]=='15'):
                           globals()["weight"+str(k)][j] +=o1
                       if(globals()["x"+str(k)][i][2]=='9'):
                           globals()["weight"+str(k)][j] +=o2
                       if(globals()["x"+str(k)][i][2]=='105'):
                           globals()["weight"+str(k)][j] +=o3
                       if(globals()["x"+str(k)][i][2]=='945'):
                           globals()["weight"+str(k)][j] +=e1
                       if(globals()["x"+str(k)][i][2]=='315'):
                           globals()["weight"+str(k)][j] +=e2
                       if(globals()["x"+str(k)][i][2]=='225'):
                           globals()["weight"+str(k)][j] +=e3                          
   
#########################

def is_compatible(bipA, bipB):
    #numset=0
    status="compatible"
    def _A():
        global status
        status="compatible"
        for i in range(len(bipA["bipartition"])):
            for j in range(len(bipB["bipartition"])):
                if(bipA["bipartition"][i]==bipB["bipartition"][j]):
                    #global status
                    status="not-compatible"
                    #print("x"+ str(i)+ str(j))
                    #print(status)
                    return status
                else:
                    continue
        #print(status)
        return status
    
    status=_A()
    #print(status)
    if(status=="not-compatible"):
        #print("yes")
        #numset +=1
        def _B():
            global status
            status="compatible"
            for i in range(len(bipA["bipartition"])):
                for j in range(len(bipB["complement"])):
                    if(bipA["bipartition"][i]==bipB["complement"][j]): 
                        status="not-compatible"
                        #print("y")
                        return status
                    else:
                        continue
            #print(status)
            return status
        
        status=_B()
    #print(status)    
    if(status=="not-compatible"):
        #status="compatible"
        #numset +=1
        #print(status)
        def _C():
            global status
            status="compatible"
            for i in range(len(bipA["complement"])):
                for j in range(len(bipB["bipartition"])):
                    if(bipA["complement"][i]==bipB["bipartition"][j]):
                        #global status
                        status="not-compatible"
                        #print("z")
                        return status
                    else:
                        continue
            #print(status)
            return status
        status=_C()
     
    #print(status)     
    if(status=="not-compatible"):
        #status="compatible"
        #numset +=1
        def _D():
            global status
            status="compatible"
            for i in range(len(bipA["complement"])):
                for j in range(len(bipB["complement"])):
                    if(bipA["complement"][i]==bipB["complement"][j]):
                        #global status
                        status="not-compatible"
                        #print("t")
                        return status
                    else:
                        continue
            #print(status)
            return status
        status=_D()            

    #print(status)    
    if(status=="compatible"):
        return(True)
    else:
        #print(numset +1)
        return(False)
############## 
   
comp=[[] for i in range(len(ref))]                   
arra = ["A","B","C","D","E","F","G","H"]           
for i in range(len(ref)):
    for j in arra:
        if(j not in ref[i]):
            comp[i].append(j)                 



for k in range(1,11):
    globals()["u"+str(k)]=[]
    

for k in range(1,11):
    for i in range(len(ref)):
        globals()["u"+str(k)].append(dict(bipartition=ref[i], complement=comp[i], weight=globals()["weight"+str(k)][i]))


for k in range(1,11):
    globals()["bipweight"+str(k)] = sorted(globals()["u"+str(k)], key=lambda item: item["weight"], reverse=True) 

######################## 
def _setof5compatibleGreedy(newu):
    #compc1=[]
    jja=[]
    for j in range(len(newu)):
        if(is_compatible(newu[0],newu[j])):
            jja.append(j)
            #compc1.append(newu[j])
            
    #first and second:
    setofcompc1=[newu[jja[0]],newu[jja[1]]]
    del newu[jja[0]]
    del newu[jja[1]-1]
    #print(len(newu))
    #original len of ref=28+56+35=119
    # third
    if(len(newu)==117):
        for j in range(len(newu)):
            if((is_compatible(setofcompc1[0],newu[j])) & (is_compatible(setofcompc1[1],newu[j]))):
                setofcompc1.append(newu[j])
                del newu[j]
                break
    
    #fourth
    if(len(newu)==116):
        for j in range(len(newu)):
            if((is_compatible(setofcompc1[0],newu[j])) & (is_compatible(setofcompc1[1],newu[j])) & (is_compatible(setofcompc1[2],newu[j]))):
                setofcompc1.append(newu[j])
                del newu[j]
                break
    
    #fifth 
    if(len(newu)==115):   
        for j in range(len(newu)):
            if((is_compatible(setofcompc1[0],newu[j])) & (is_compatible(setofcompc1[1],newu[j])) & (is_compatible(setofcompc1[2],newu[j])) & (is_compatible(setofcompc1[3],newu[j]))):
                setofcompc1.append(newu[j])
                del newu[j]
                break
    
    if(len(newu)==114):
        print(setofcompc1)
        return(setofcompc1)
    else:
        print("error")
        
########

#_setof5compatibleGreedy(bipweight2)  

for k in range(1,11):
    globals()["bipweight"+str(k)] = sorted(globals()["u"+str(k)], key=lambda item: item["weight"], reverse=True) 

for k in range(1,11):
    globals()["bset"+str(k)]=[]
    
for k in range(1,11):
    globals()["bset"+str(k)]=_setof5compatibleGreedy(globals()["bipweight"+str(k)]) 

for k in range(1,11):
    print("\n")
    print("chromosome"+str(k))
    for i in range(5):
        print( globals()["bset"+str(k)][i]["bipartition"],globals()["bset"+str(k)][i]["complement"])
    we=0
    for i in range(5):
        we += globals()["bset"+str(k)][i]["weight"]
    print("with sum of weight of "+str(we))














            