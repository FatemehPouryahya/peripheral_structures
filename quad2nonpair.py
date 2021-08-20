def Probquadnp(e,m,k,n):
    print(e,m,k,n) 
    if((e<0) or (e>k) or (e> int(n/4))or (m>k) or (m>int(n/3)) or (m<0) or (k>=int(n/2)+1) or (k<2) or (n<8)):
        print(e,m,k,n)
        print("yes1")
        return(0)    
    elif((e==2) and (k==2) and (m==2) and (n==8)):
        print(e,m,k,n)
        print("yes2")
        return(336/693)
    elif((e==1)and (k==3) and (m==1) and (n==8)):
        print(e,m,k,n)
        print("yes3")
        return(168/693)
    elif((e==0) and (k==4) and (m==0) and (n==8)):
        print(e,m,k,n)
        print("yes3")
        return(21/693)    
    elif((e==0)and (k==3) and (m==2) and (n==8)):
        print(e,m,k,n)
        print("yes3")
        return(168/693)
    elif(n==8):
        print(e,m,k,n)
        print("yes4")
        return(0)        
    else:
        print(e,m,k,n)
        print("hell")        
        w=(((4*m-4*e+4)/(2*n-5))*Probquadnp(e-1,m,k,n-1)+((e+1)/(2*n-5))*Probquadnp(e+1,m,k-1,n-1)\
            +((e+1)/(2*n-5))*Probquadnp(e+1,m+1,k-1,n-1)+((m+1-e)/(2*n-5))*Probquadnp(e,m+1,k-1,n-1)\
                +((3*k-3*m+3)/(2*n-5))*Probquadnp(e,m-1,k,n-1)+((n-k-m+4*e-4)/(2*n-5))*Probquadnp(e,m,k,n-1)+((n-2*k-m+1-e)/(2*n-5))*Probquadnp(e,m,k-1,n-1))
        print(w,"for",e,m,k,n)
        return(w)
            

       
def probquadnp(e,n):
    a=0
    for i in range(int(n/3)+1):
        for j in range(max(i,2), int(n/2)+1):
            print(e,i,j,n, Probquadnp(e,i,j,n))
            a= a+Probquadnp(e,i,j,n)
    return(a)  

#########################
ala=[]
for n in range(8,13):
    print(n)
    an=np.zeros((int(n/2)-1,int(n/4)+1,int(n/3)+1))
    for k in range(2,int(n/2)+1):
        for m in range(int(n/3)+1):
            for e in range(int(n/4)+1):
                 an[k-2][e][m]= Probquadnp(e,m,k,n)
    ala.append(dict(leaves=n, prob=an))

s=0
n=14
for e in range(int(n/4)+1):
    #s+=probquad(f,15)      
    for k in range(2, int(n/2)+1):
        for m in range(int(n/3)+1): 
            s+= q[n]["prob"][k-2][e][m]
s            
###########
for n in range(8,11):
    print(n)
    an=np.zeros((int(n/2)-1,int(n/4)+1,int(n/3)+1))
    for k in range(2,int(n/2)+1):
        for m in range(int(n/3)+1):
            for e in range(int(n/4)+1):
                 an[k-2][e][m]= Probquadnp(e,m,k,n)
    q.append(dict(leaves=n, prob=an))
    
import numpy as np 
q=[{'leaves': 0, 'prob': [0]},\
 {'leaves': 1, 'prob': [0]},\
 {'leaves': 2, 'prob': [0]},\
 {'leaves': 3, 'prob': [0]},\
 {'leaves': 4, 'prob': [0]},\
 {'leaves': 5, 'prob': [0]},\
 {'leaves': 6, 'prob': [0]},\
 {'leaves': 7, 'prob': [0]},
 {'leaves': 8,
  'prob': [[[0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.48484848]],
  
         [[0.        , 0.        , 0.24242424],
          [0.        , 0.24242424, 0.        ],
          [0.        , 0.        , 0.        ]],
  
         [[0.03030303, 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ]]]},
 {'leaves': 9,
  'prob': [[[0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.33566434, 0.        ]],
  
         [[0.        , 0.        , 0.        , 0.05594406],
          [0.        , 0.16783217, 0.33566434, 0.        ],
          [0.        , 0.        , 0.        , 0.        ]],
  
         [[0.02097902, 0.08391608, 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ]]]},
 {'leaves': 10,
  'prob': [[[0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.22377622, 0.        ]],
  
         [[0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.11188811, 0.22377622, 0.11188811],
          [0.        , 0.        , 0.11188811, 0.        ]],
  
         [[0.01398601, 0.05594406, 0.08391608, 0.        ],
          [0.        , 0.05594406, 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ]],
  
         [[0.00699301, 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ]]]},
 {'leaves': 11,
  'prob': [[[0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.14479638, 0.        ]],
  
         [[0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.07239819, 0.14479638, 0.07239819],
          [0.        , 0.        , 0.14479638, 0.07239819]],
  
         [[0.00904977, 0.0361991 , 0.05429864, 0.0361991 ],
          [0.        , 0.07239819, 0.10859729, 0.        ],
          [0.        , 0.        , 0.        , 0.        ]],
  
         [[0.00904977, 0.02262443, 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ]]]},
 {'leaves': 12,
  'prob': [[[0.        , 0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.09145035, 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        , 0.        ]],
  
         [[0.        , 0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.04572517, 0.09145035, 0.04572517, 0.        ],
          [0.        , 0.        , 0.13717552, 0.09145035, 0.        ],
          [0.        , 0.        , 0.        , 0.01524172, 0.        ]],
  
         [[0.00571565, 0.02286259, 0.03429388, 0.02286259, 0.00571565],
          [0.        , 0.06858776, 0.13717552, 0.06858776, 0.        ],
          [0.        , 0.        , 0.03429388, 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        , 0.        ]],
  
         [[0.00857347, 0.02857823, 0.02857823, 0.        , 0.        ],
          [0.        , 0.01428912, 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        , 0.        ]],
  
         [[0.00166706, 0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        , 0.        ]]]}]
    
#(((4*m-4*e+4)/(2*n-5))*Probquadnp(e-1,m,k,n-1)+((e+1)/(2*n-5))*Probquadnp(e+1,m,k-1,n-1)\
 #           +((e+1)/(2*n-5))*Probquadnp(e+1,m+1,k-1,n-1)+((m+1-e)/(2*n-5))*Probquadnp(e,m+1,k-1,n-1)\
     #           +((3*k-3*m+3)/(2*n-5))*Probquadnp(e,m-1,k,n-1)+((n-k-m+4*e-4)/(2*n-5))*Probquadnp(e,m,k,n-1)+((n-2*k-m+1-e)/(2*n-5))*Probquadnp(e,m,k-1,n-1))   
   
z=511   
for n in range(13,z):
    print(n)
    an=np.zeros((int(n/2)-1,int(n/4)+1,int(n/3)+1))
    for k in range(2,int(n/2)+1):
        for m in range(int(n/3)+1):
            for e in range(int(n/4)+1):
                #print(e,m,k,n)
                if((m>k) or (e> k)):
                    an[k-2][e][m]=0
                else:                    
                    if(k==2):
                        if(m==0):
                            if(e==0):
                                an[k-2][e][m]=(((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m])
                            elif(e >=(int((n-1)/4)+1)):
                                an[k-2][e][m]=((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]                          
                            else:                                    
                                an[k-2][e][m]=((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]+((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]
                        elif(m >= (int((n-1)/3)+1)):
                            an[k-2][e][m]=((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]
                        else:                            
                            an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]+((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]+((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m])
                    elif(k >= (int((n-1)/2)+1)):
                        if(m>= (int((n-1)/3)+1)):
                            an[k-2][e][m]=0
                        elif(m == (int((n-1)/3))):
                            if(e >=(int((n-1)/4)+1)):
                                an[k-2][e][m]=0
                            elif(e==(int((n-1)/4))):
                                an[k-2][e][m]=((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m]
                            else:
                                an[k-2][e][m]=((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m]
                        else:
                            if(e >=(int((n-1)/4)+1)):
                                an[k-2][e][m]=0
                            elif(e==(int((n-1)/4))):
                                an[k-2][e][m]=(((m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m+1]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                            else:
                                an[k-2][e][m]=(((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m]+((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m+1]
                                               +((m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m+1]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                    else:
                        if(m==0):
                            if(e==0):
                                an[k-2][e][m]=(((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m]+((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m+1]+((m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m+1]
                                                        +((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                            elif(e >=(int((n-1)/4)+1)):
                                an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m])
                            elif(e ==(int((n-1)/4))):
                                an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]+((m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m+1]
                                                +((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                            else:
                                an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]+((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m]
                                               +((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m+1]+((m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m+1]
                                                   +((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                        elif(m>=( int((n-1)/3)+1)):
                            if(e >=(int((n-1)/4)+1)):
                                 an[k-2][e][m]=0
                            else:
                                 an[k-2][e][m]=((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]
                        elif(m == (int((n-1)/3))):
                            if(e==0):
                                an[k-2][e][m]=(((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m]+((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]
                                                +((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                            if(e >=(int((n-1)/4)+1)):
                                an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m])
                            elif(e ==(int((n-1)/4))):
                                 an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]+((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]
                                                +((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                            else:
                                an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]+((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m]
                                               +((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]+((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                        else:
                            if(e==0):
                                an[k-2][e][m]=(((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m]+((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m+1]+((m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m+1]
                                               +((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]+((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                            elif(e >=(int((n-1)/4)+1)):
                                an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m])
                            elif(e == (int((n-1)/4))):
                                an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]+((m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m+1]
                                               +((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]+((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
                            else:
                                an[k-2][e][m]=(((4*m-4*e+4)/(2*n-5))*q[n-1]["prob"][k-2][e-1][m]+((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m]
                                               +((e+1)/(2*n-5))*q[n-1]["prob"][k-3][e+1][m+1]+((m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m+1]
                                                   +((3*k-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][e][m-1]+((n-k-m+4*e-4)/(2*n-5))*q[n-1]["prob"][k-2][e][m]+((n-2*k-m+1-e)/(2*n-5))*q[n-1]["prob"][k-3][e][m])
    q.append(dict(leaves=n, prob=an))
    


#############
#second part:
def probquad(f,n):
    a=0
    for i in range(int(n/3)+1):
        for j in range(max(i,2), int(n/2)+1):
            #print(f,i,j,n, Probquad(f,i,j,n))
            a= a+Probquad(f,i,j,n)
    return(a)  
 

qq=[{'leaves': 0, 'prob': [0]},\
 {'leaves': 1, 'prob': [0]},\
 {'leaves': 2, 'prob': [0]},\
 {'leaves': 3, 'prob': [0]},\
 {'leaves': 4, 'prob': [0]},\
 {'leaves': 5, 'prob': [0]},\
 {'leaves': 6, 'prob': [0]},\
 {'leaves': 7, 'prob': [0]},
 {'leaves': 8,
  'prob': [0.2727272727272727, 0.24242424242424243, 0.48484848484848486]},
 {'leaves': 9,
  'prob': [0.16083916083916083, 0.5034965034965035, 0.3356643356643357]},
 {'leaves': 10,
  'prob': [0.16083916083916086, 0.5034965034965035, 0.3356643356643357]}]
    
for n in range(11,z):
    print(n)
    ann=[]
    for e in range(int(n/4)+1):
        a=0
        for k in range(2, int(n/2)+1):
            for m in range(int(n/3)+1): 
                #print(q[n]["prob"][k-2][e][m])
                a+= q[n]["prob"][k-2][e][m]
        ann.append(a)
    qq.append(dict(leaves=n, prob=ann))   
    
    
############test    
s=0
n=250
for f in range(int(n/4)+1):
    #s+=probquad(f,15)      
    for k in range(2, int(n/2)+1):
        for m in range(int(n/3)+1): 
            s+= q[n]["prob"][k-2][f][m]
s            
#####################
import matplotlib.pyplot as plt 

for i in range(len(qq)):
    globals()["x"+str(i)]=[]
    globals()["y"+str(i)]=[]


for p in range(8,101,4):     
    globals()["x"+ str(p)]=list(range(int(p/4)+1))
    globals()["y"+ str(p)]=qq[p]["prob"]
    plt.plot(globals()["x"+ str(p)], globals()["y"+ str(p)], label = str(p)+" leaves")

plt.xlabel('Number of quadruple terminals( type II)') 
plt.ylabel('Probability distribution') 
#plt.title('') 
#plt.legend()   
plt.show()        


file="E:/sugerc/type2quadprobquadruple500.txt"
with open(file,"w") as f:
    for s in qq:
        f.write(str(s))
        f.write("\n")

for i in range(len(qq)):
    globals()["z"+str(i)]=0      # mean
    globals()["frac"+str(i)]=0  # for mean/n

for p in range(8,len(qq)):
    for j in range(int(p/4)+1):
        globals()["z"+str(p)] +=globals()["x"+ str(p)][j]*globals()["y"+ str(p)][j]

# mean/n :
for p in range(8,len(qq)):
    globals()["frac"+str(p)]= (globals()["z"+str(p)])/p
    
# st :
        
import math  
for i in range(len(qq)):
    globals()["bigv"+str(i)]=0
    globals()["var"+str(i)]=0
    globals()["st"+str(i)]=0

for i in range(len(qq)):
    globals()["stfrac"+str(i)]=0    #st/m
    
for p in range(8,len(qq)):
    for j in range(int(p/4)+1):
        globals()["bigv"+str(p)] +=(math.pow(globals()["x"+ str(p)][j],2))*globals()["y"+ str(p)][j]


for p in range(8,len(qq)):
     globals()["var"+str(p)]= globals()["bigv"+str(p)]-(math.pow(globals()["z"+str(p)],2))
     
for p in range(8,len(qq)):     
     globals()["st"+str(p)]=math.sqrt(globals()["var"+str(p)])  
        
for p in range(8,len(qq)):     
     globals()["stfrac"+str(p)]=(globals()["st"+str(p)])/p

import pandas as pd
mean=[]
st=[]
fracmean=[]  
fracst=[]
   
for i in range(8,len(qq)): 
    mean.append(globals()["z"+str(i)])
    st.append(globals()["st"+str(i)])
    fracmean.append(globals()["frac"+str(i)])
    fracst.append(globals()["stfrac"+str(i)])
       
d = {"leaves":list(range(8,z)),'Mean': mean, 'St': st,"Mean/n":fracmean,"St/n":fracst}
df = pd.DataFrame(data=d)     

df.to_csv('E:/sugerc/type2quadmeanstquad500.csv')


























