            
def Probtriple(m,k,n):
    if((m>k) or (m>int(n/3)) or (m<0) or (k>=int(n/2)+1) or (k<2) or (n<6)):
        return(0)
    if( (k==3) and (m==0) and (n==6)):
        return(1/7)
    if((m==1) and (n==6)):
        return(0)
    if( (k==2) and (m==2) and (n==6)):
        return(6/7)        
    else:
        #print(Probtriple(m,k,n-1),Probtriple(m-1,k,n-1),Probtriple(m,k-1,n-1),Probtriple(m+1,k-1,n-1))
        return(((n-4+3*m-k)/(2*n-5))*Probtriple(m,k,n-1)+((3*k-3*m+3)/(2*n-5))*Probtriple(m-1,k,n-1)
               +((n-2*k-m+1)/(2*n-5))*Probtriple(m,k-1,n-1)+((m+1)/(2*n-5))*Probtriple(m+1,k-1,n-1))

def probtrip(m,n):
    a=0
    for i in range(m, int(n/2)+1):
        a= a+Probtriple(m,i,n)
    return(a)    

z=101
t=[{'leaves': 0, 'prob': [0]},\
 {'leaves': 1, 'prob': [0]},\
 {'leaves': 2, 'prob': [0]},\
 {'leaves': 3, 'prob': [0]},\
 {'leaves': 4, 'prob': [0]},\
 {'leaves': 5, 'prob': [0]},\
 {'leaves': 6,
  'prob': [[0.0, 0, 0.8571428571428571], [0.14285714285714285, 0, 0.0]]},
 {'leaves': 7,
  'prob': [[0.0, 0.0, 0.6666666666666666], [0.0, 0.3333333333333333, 0.0]]},
 {'leaves': 8,
  'prob': [[0.0, 0.0, 0.48484848484848486],
   [0.0, 0.24242424242424243, 0.2424242424242424],
   [0.030303030303030304, 0.0, 0.0]]},
 {'leaves': 9,
  'prob': [[0.0, 0.0, 0.3356643356643357, 0],
   [0.0, 0.16783216783216784, 0.33566433566433573, 0.055944055944055944],
   [0.02097902097902098, 0.08391608391608392, 0.0, 0.0]]},
 {'leaves': 10,
  'prob': [[0.0, 0.0, 0.22377622377622378, 0],
   [0.0, 0.11188811188811189, 0.33566433566433573, 0.1118881118881119],
   [0.013986013986013986, 0.1118881118881119, 0.08391608391608393, 0.0],
   [0.006993006993006993, 0.0, 0.0, 0.0]]}]
    
for n in range(11,z):
    a1=[]
    for k in range(2, int(n/2)+1):
        a2=[]
        for m in range(0, int(n/3)+1):                
                if(m>k):
                    a2.append(0)     
                else:
                    if(k==2):
                        if(m==0):
                             a2.append(((n-4+3*m-k)/(2*n-5))*t[n-1]["prob"][k-2][m])
                        elif(m >= (int((n-1)/3)+1)):
                             a2.append(((3*k-3*m+3)/(2*n-5))*t[n-1]["prob"][k-2][m-1])
                        else:
                             a2.append(((n-4+3*m-k)/(2*n-5))*t[n-1]["prob"][k-2][m]+((3*k-3*m+3)/(2*n-5))*t[n-1]["prob"][k-2][m-1])
                    elif(k >= (int((n-1)/2)+1)):
                        if(m>= (int((n-1)/3)+1)):
                            a2.append(0) 
                        elif(m == (int((n-1)/3))):
                            a2.append(((n-2*k-m+1)/(2*n-5))*t[n-1]["prob"][k-3][m])                           
                        else:                        
                            a2.append(((n-2*k-m+1)/(2*n-5))*t[n-1]["prob"][k-3][m]+((m+1)/(2*n-5))*t[n-1]["prob"][k-3][m+1])        
                    else:
                        if(m==0):
                            #print("n=",n,"k=", k,"m=",m)
                            a2.append(((n-4+3*m-k)/(2*n-5))*t[n-1]["prob"][k-2][m]+((n-2*k-m+1)/(2*n-5))*t[n-1]["prob"][k-3][m]+((m+1)/(2*n-5))*t[n-1]["prob"][k-3][m+1])
                        elif(m>=( int((n-1)/3)+1)):
                             a2.append(((3*k-3*m+3)/(2*n-5))*t[n-1]["prob"][k-2][m-1])                        
                        elif(m == (int((n-1)/3))):
                             a2.append(((n-4+3*m-k)/(2*n-5))*t[n-1]["prob"][k-2][m]+((3*k-3*m+3)/(2*n-5))*t[n-1]["prob"][k-2][m-1]\
                                      +((n-2*k-m+1)/(2*n-5))*t[n-1]["prob"][k-3][m])
                        else:
                            a2.append(((n-4+3*m-k)/(2*n-5))*t[n-1]["prob"][k-2][m]+((3*k-3*m+3)/(2*n-5))*t[n-1]["prob"][k-2][m-1]\
                                          +((n-2*k-m+1)/(2*n-5))*t[n-1]["prob"][k-3][m]+((m+1)/(2*n-5))*t[n-1]["prob"][k-3][m+1])  
        a1.append(a2)
        #print("for n is "+str(i) +" and m is "+ str(j) +" the probability is "+ str(probtrip(j,i)))      
    t.append(dict(leaves=n, prob=a1)) 

#second part:

def Probtriple(m,k,n): #t[n]["prob"][k-2][m]
    if((m>k) or (m>int(n/3)) or (m<0) or (k>=int(n/2)+1) or (k<2) or (n<6)):
        return(0)
    if( (k==3) and (m==0) and (n==6)):
        return(1/7)
    if((m==1) and (n==6)):
        return(0)
    if( (k==2) and (m==2) and (n==6)):
        return(6/7)        
    else:
        #print(Probtriple(m,k,n-1),Probtriple(m-1,k,n-1),Probtriple(m,k-1,n-1),Probtriple(m+1,k-1,n-1))
        return(((n-4+3*m-k)/(2*n-5))*Probtriple(m,k,n-1)+((3*k-3*m+3)/(2*n-5))*Probtriple(m-1,k,n-1)
               +((n-2*k-m+1)/(2*n-5))*Probtriple(m,k-1,n-1)+((m+1)/(2*n-5))*Probtriple(m+1,k-1,n-1))

def probtrip(m,n):
    a=0
    for i in range(m, int(n/2)+1):
        a= a+Probtriple(m,i,n)
    return(a)    


z=101
#tt=[]
tt=[{'leaves': 0, 'prob': [0]},\
 {'leaves': 1, 'prob': [0]},\
 {'leaves': 2, 'prob': [0]},\
 {'leaves': 3, 'prob': [0]},\
 {'leaves': 4, 'prob': [0]},\
 {'leaves': 5, 'prob': [0]},\
 {'leaves': 6, 'prob': [0.14285714285714285, 0, 0.8571428571428571]},
 {'leaves': 7, 'prob': [0.0, 0.3333333333333333, 0.6666666666666666]},
 {'leaves': 8,
  'prob': [0.030303030303030304, 0.24242424242424243, 0.7272727272727273]},
 {'leaves': 9,
  'prob': [0.02097902097902098,
   0.2517482517482518,
   0.6713286713286715,
   0.055944055944055944]},
 {'leaves': 10,
  'prob': [0.02097902097902098,
   0.2237762237762238,
   0.6433566433566434,
   0.1118881118881119]}]
  
       
for n in range(11,z):
    attt=[]
    for m in range(0, int(n/3)+1):
        a=0
        for k in range(max(2,m), int(n/2)+1):
            a= a+t[n]["prob"][k-2][m]
        attt.append(a)        
        #print("for n is "+str(i) +" and m is "+ str(j) +" the probability is "+ str(probtrip(j,i)))          
    tt.append(dict(leaves=n, prob=attt)) 

        
import matplotlib.pyplot as plt 

for i in range(len(tt)):
    globals()["x"+str(i)]=[]
    globals()["y"+str(i)]=[]


for p in range(6,len(tt),4):     
    globals()["x"+ str(p)]=list(range(int(p/3)+1))
    globals()["y"+ str(p)]=tt[p]["prob"]
    plt.plot(globals()["x"+ str(p)], globals()["y"+ str(p)], label = str(p)+" leaves")

plt.xlabel('Number of triple terminals') 
plt.ylabel('Probability distribution') 
#plt.title('') 
#plt.legend()   
plt.show()        


file="E:/sugerc/probtriple6t100check.txt"
with open(file,"w") as f:
    for s in tt:
        f.write(str(s))
        f.write("\n")

for i in range(len(tt)):
    globals()["z"+str(i)]=0      # mean
    globals()["frac"+str(i)]=0  # for mean/n

for p in range(6,len(tt)):
    for j in range(int(p/3)+1):
        globals()["z"+str(p)] +=globals()["x"+ str(p)][j]*globals()["y"+ str(p)][j]

# mean/n :
for p in range(6,len(tt)):
    globals()["frac"+str(p)]= (globals()["z"+str(p)])/p
    
# st :
        
import math  
for i in range(len(tt)):
    globals()["bigv"+str(i)]=0
    globals()["var"+str(i)]=0
    globals()["st"+str(i)]=0

for i in range(len(tt)):
    globals()["stfrac"+str(i)]=0    #st/m
    
for p in range(6,len(tt)):
    for j in range(int(p/3)+1):
        globals()["bigv"+str(p)] +=(math.pow(globals()["x"+ str(p)][j],2))*globals()["y"+ str(p)][j]


for p in range(6,len(tt)):
     globals()["var"+str(p)]= globals()["bigv"+str(p)]-(math.pow(globals()["z"+str(p)],2))
     
for p in range(6,len(tt)):     
     globals()["st"+str(p)]=math.sqrt(globals()["var"+str(p)])  
        
for p in range(6,len(tt)):     
     globals()["stfrac"+str(p)]=(globals()["st"+str(p)])/p

import pandas as pd
mean=[]
st=[]
fracmean=[]  
fracst=[]
   
for i in range(6,len(tt)): 
    mean.append(globals()["z"+str(i)])
    st.append(globals()["st"+str(i)])
    fracmean.append(globals()["frac"+str(i)])
    fracst.append(globals()["stfrac"+str(i)])
       
d = {"leaves":list(range(6,101)),'Mean': mean, 'St': st,"Mean/n":fracmean,"St/n":fracst}
df = pd.DataFrame(data=d)     

df.to_csv('E:/sugerc/meansttriple.csv')