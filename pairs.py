# m is the number of (2,n-2) bipartitions
# n is the number of leaves

def prob(n, m):
    if((n<=2) or (m<=1) or (m>= int(n/2)+1)):
        print("Wrong input, n or m is not in the boundary")
    else:
        if(m==2):
            if(n>=6):
                return((n/(2*n-5))*prob(n-1, m))
            elif((n>=3) and (n<=5)):
                return(1)
        elif((m>=3) and (m<=(int(n/2)-1))):
            return(((((2*n-5)-(n-1-2*m))/(2*n-5))*prob(n-1, m))+ ((((n-1)-2*(m-1))/(2*n-5))*prob(n-1, m-1)))                    
        elif(m==(int(n/2))):
            if((n%2)==0):
                return((1/(2*n-5))*prob(n-1,m-1))
            else:
                return(((2/(2*n-5))*prob(n-1,m-1))+(1*prob(n-1,m)))
z=50
# dont use this
for i in range(3,z):
    for j in range(2, int(i/2)+1):
        print("\\newline for n is "+str(i) +" and m is "+ str(j) +" the probability is "+ str(prob(i,j)))

z=50
b=[]
# dont use this
for i in range(6,z):
    a=[]
    for j in range(2, int(i/2)+1):
        a.append(prob(i,j))
        print("for n is "+str(i) +" and m is "+ str(j) +" the probability is "+ str(prob(i,j)))       
    b.append(dict(leaves=i, prob=a))      


# use this, start from here, below less time consuming

z=101  
b=[{'leaves': 0, 'prob': [0]},\
 {'leaves': 1, 'prob': [0]},\
 {'leaves': 2, 'prob': [0]},\
 {'leaves': 3, 'prob': [1]},\
 {'leaves': 4, 'prob': [1]},\
 {'leaves': 5, 'prob': [1]},\
 {'leaves': 6, 'prob': [0.8571428571428571, 0.14285714285714285]},\
 {'leaves': 7, 'prob': [0.6666666666666666, 0.3333333333333333]},\
 {'leaves': 8,\
  'prob': [0.48484848484848486, 0.48484848484848475, 0.030303030303030304]},\
 {'leaves': 9,\
  'prob': [0.3356643356643357, 0.5594405594405594, 0.10489510489510488]},\
 {'leaves': 10,\
  'prob': [0.22377622377622378,\
   0.5594405594405594,\
   0.20979020979020976,\
   0.006993006993006992]}]     
    
for i in range(11,z):
    a=[]
    prob=0
    for j in range(2, int(i/2)+1):
        if(j==2):
            prob=((i/(2*i-5))*b[i-1]["prob"][j-2])
        elif((j>=3) and (j<=(int(i/2)-1))):
            prob=(((((2*i-5)-(i-1-2*j))/(2*i-5))*b[i-1]["prob"][j-2])+ ((((i-1)-2*(j-1))/(2*i-5))*b[i-1]["prob"][j-3]))                    
        elif(j==(int(i/2))):
            if((i%2)==0):
                prob=((1/(2*i-5))*b[i-1]["prob"][j-3])
            else:
                prob=(((2/(2*i-5))*b[i-1]["prob"][j-3])+(1*b[i-1]["prob"][j-2]))               
        a.append(prob)
        print("for n is "+str(i) +" and m is "+ str(j) +" the probability is "+ str(prob))       
    b.append(dict(leaves=i, prob=a))            
        
import matplotlib.pyplot as plt 

for i in range(len(b)):
    globals()["x"+str(i)]=[]
    globals()["y"+str(i)]=[]


for p in range(6,len(b)):     
    globals()["x"+ str(p)]=list(range(2, int(p/2)+1))
    globals()["y"+ str(p)]=b[p]["prob"]
    plt.plot(globals()["x"+ str(p)], globals()["y"+ str(p)], label = str(p)+" leaves")

plt.xlabel('number of (2,n-2) bipartitions') 
plt.ylabel('probability distribution') 
#plt.title('') 
#plt.legend()   
plt.show()        

file="E:/sugerc/probdis6t100.txt"
with open(file,"w") as f:
    for s in b:
        f.write(str(s))
        f.write("\n")

for i in range(len(b)):
    globals()["z"+str(i)]=0      # mean
    globals()["frac"+str(i)]=0  # for mean/n
    
for p in range(6,len(b)):
    for j in range(int(p/2)-1):
        globals()["z"+str(p)] +=globals()["x"+ str(p)][j]*globals()["y"+ str(p)][j]

# mean/n :
for p in range(6,len(b)):
    globals()["frac"+str(p)]= (globals()["z"+str(p)])/p
    
# st :
        
import math  
for i in range(len(b)):
    globals()["bigv"+str(i)]=0
    globals()["var"+str(i)]=0
    globals()["st"+str(i)]=0

for i in range(len(b)):
    globals()["stfrac"+str(i)]=0    #st/m
    
for p in range(6,len(b)):
    for j in range(int(p/2)-1):
        globals()["bigv"+str(p)] +=(math.pow(globals()["x"+ str(p)][j],2))*globals()["y"+ str(p)][j]


for p in range(6,len(b)):
     globals()["var"+str(p)]= globals()["bigv"+str(p)]-(math.pow(globals()["z"+str(p)],2))
     
for p in range(6,len(b)):     
     globals()["st"+str(p)]=math.sqrt(globals()["var"+str(p)])  
        
for p in range(6,len(b)):     
     globals()["stfrac"+str(p)]=(globals()["st"+str(p)])/p

import pandas as pd
mean=[]
st=[]
fracmean=[]  
fracst=[]
   
for i in range(6,len(b)): 
    mean.append(globals()["z"+str(i)])
    st.append(globals()["st"+str(i)])
    fracmean.append(globals()["frac"+str(i)])
    fracst.append(globals()["stfrac"+str(i)])
       
d = {"leaves":list(range(6,101)),'Mean': mean, 'St': st,"Mean/n":fracmean,"St/n":fracst}
df = pd.DataFrame(data=d)     

df.to_csv('E:/sugerc/meanst.csv')

