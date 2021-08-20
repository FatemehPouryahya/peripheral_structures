def Probquad(f,m,k,n):
    #print(f,m,k,n) 
    if((f<0) or (f> int(k/2)) or (f> int(n/4))or (m>k) or (m>int(n/3)) or (m<0) or (k>=int(n/2)+1) or (k<2) or (n<7)):
        print(f,m,k,n)
        print("yes1")
        return(0)    
    elif( (f==0) and (k==2) and (m==2) and (n==7)):
        print(f,m,k,n)
        print("yes2")
        return(42/63)
    elif((f==1)and (k==3) and (m==1) and (n==7)):
        print(f,m,k,n)
        print("yes3")
        return(21/63)
    elif(n==7):
        print(f,m,k,n)
        print("yes4")
        return(0)        
    else:
        print(f,m,k,n)
        print("hell")        
        w=(((m+1)/(2*n-5))*Probquad(f-1,m+1,k-1,n-1)+((6*f+6)/(2*n-5))*Probquad(f+1,m-1,k,n-1)\
                +((3*k-6*f-3*m+3)/(2*n-5))*Probquad(f,m-1,k,n-1)+((n-4-k+3*m)/(2*n-5))*Probquad(f,m,k,n-1)\
                    +((n-2*k-m+1)/(2*n-5))*Probquad(f,m,k-1,n-1))
        #print(w,"for",f,m,k,n)
        return(w)
            
def probquad(f,n):
    a=0
    for i in range(int(n/3)+1):
        for j in range(max(i,2), int(n/2)+1):
            print(f,i,j,n, Probquad(f,i,j,n))
            a= a+Probquad(f,i,j,n)
    return(a)  

for n in range(7,10):
    print(n)
    an=np.zeros((int(n/2)-1,int(n/4)+1,int(n/3)+1))
    for k in range(2,int(n/2)+1):
        for m in range(int(n/3)+1):
            for f in range(int(n/4)+1):
                 an[k-2][f][m]= Probquad(f,m,k,n)
    q.append(dict(leaves=n, prob=an))
    
 
q=[{'leaves': 0, 'prob': [0]},\
 {'leaves': 1, 'prob': [0]},\
 {'leaves': 2, 'prob': [0]},\
 {'leaves': 3, 'prob': [0]},\
 {'leaves': 4, 'prob': [0]},\
 {'leaves': 5, 'prob': [0]},\
 {'leaves': 6, 'prob': [0]},\
 {'leaves': 7,
  'prob': [[[0.        , 0.        , 0.66666667],
          [0.        , 0.        , 0.        ]],
  
         [[0.        , 0.        , 0.        ],
          [0.        , 0.33333333, 0.        ]]]},
 {'leaves': 8,
  'prob': [[[0.        , 0.        , 0.48484848],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ]],
  
         [[0.        , 0.        , 0.24242424],
          [0.        , 0.24242424, 0.        ],
          [0.        , 0.        , 0.        ]],
  
         [[0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          [0.03030303, 0.        , 0.        ]]]},
 {'leaves': 9,
  'prob': [[[0.        , 0.        , 0.33566434, 0.        ],
          [0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ]],
  
         [[0.        , 0.        , 0.33566434, 0.05594406],
          [0.        , 0.16783217, 0.        , 0.        ],
          [0.        , 0.        , 0.        , 0.        ]],
  
         [[0.        , 0.        , 0.        , 0.        ],
          [0.        , 0.08391608, 0.        , 0.        ],
          [0.02097902, 0.        , 0.        , 0.        ]]]}]
z=510   
for n in range(10,z):
    print(n)
    an=np.zeros((int(n/2)-1,int(n/4)+1,int(n/3)+1))
    for k in range(2,int(n/2)+1):
        for m in range(int(n/3)+1):
            for f in range(int(n/4)+1):
                #print(f,m,k,n)
                if((m>k) or (f> int(k/2))):
                    an[k-2][f][m]=0
                else:
                    if(k==2):
                        if(m==0):
                            if(f >=(int((n-1)/4)+1)):
                                an[k-2][f][m]=0 
                            else:                                    
                                an[k-2][f][m]=((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]
                        elif(m >= (int((n-1)/3)+1)):
                            if(f >=(int((n-1)/4)+1)):
                                an[k-2][f][m]=((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]
                            else:
                                an[k-2][f][m]=((6*f+6)/(2*n-5))*q[n-1]["prob"][k-2][f+1][m-1]+((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]                                
                        else:
                             an[k-2][f][m]=((6*f+6)/(2*n-5))*q[n-1]["prob"][k-2][f+1][m-1]\
                                +((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]+((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]
                    elif(k >= (int((n-1)/2)+1)):
                        if(m>= (int((n-1)/3)+1)):
                            an[k-2][f][m]=0
                        elif(m == (int((n-1)/3))):
                            if(f >=(int((n-1)/4)+1)):
                                an[k-2][f][m]=0
                            else:    
                                an[k-2][f][m]=((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]                           
                        else:
                            if(f==0):
                                an[k-2][f][m]=((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]
                            elif(f >=(int((n-1)/4)+1)):
                                an[k-2][f][m]=((m+1)/(2*n-5))*q[n-1]["prob"][k-3][f-1][m+1]
                            else:    
                                an[k-2][f][m]=((m+1)/(2*n-5))*q[n-1]["prob"][k-3][f-1][m+1]+((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]               
                    else:
                        if(m==0):
                            if(f==0):
                                an[k-2][f][m]=((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]+((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]                                
                            elif(f >=(int((n-1)/4)+1)):
                                an[k-2][f][m]=((m+1)/(2*n-5))*q[n-1]["prob"][k-3][f-1][m+1]                               
                            else:   
                                an[k-2][f][m]=((m+1)/(2*n-5))*q[n-1]["prob"][k-3][f-1][m+1]\
                                                +((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]+((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]
                        elif(m>=( int((n-1)/3)+1)):
                            if(f >=(int((n-1)/4)+1)):
                                 an[k-2][f][m]=0
                            elif(f ==(int((n-1)/4))): 
                                 an[k-2][f][m]=((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]
                            else:     
                                 an[k-2][f][m]=((6*f+6)/(2*n-5))*q[n-1]["prob"][k-2][f+1][m-1]\
                                                +((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]                     
                        elif(m == (int((n-1)/3))):
                            if(f >=(int((n-1)/4)+1)):
                                an[k-2][f][m]=0
                            elif(f ==(int((n-1)/4))):
                                 an[k-2][f][m]=((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]+((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]\
                                                  +((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]
                            else:
                                an[k-2][f][m]=((6*f+6)/(2*n-5))*q[n-1]["prob"][k-2][f+1][m-1]\
                                             +((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]+((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]\
                                                  +((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]
                        else:
                            if(f==0):
                                an[k-2][f][m]=((6*f+6)/(2*n-5))*q[n-1]["prob"][k-2][f+1][m-1]\
                                                +((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]+((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]\
                                                    +((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]
                            elif(f == (int((n-1)/4))):
                                an[k-2][f][m]=((m+1)/(2*n-5))*q[n-1]["prob"][k-3][f-1][m+1]\
                                                +((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]+((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]\
                                                    +((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]
                            elif(f >=(int((n-1)/4)+1)):
                                an[k-2][f][m]=((m+1)/(2*n-5))*q[n-1]["prob"][k-3][f-1][m+1]                            
                            else:
                                an[k-2][f][m]=((m+1)/(2*n-5))*q[n-1]["prob"][k-3][f-1][m+1]+((6*f+6)/(2*n-5))*q[n-1]["prob"][k-2][f+1][m-1]\
                                                    +((3*k-6*f-3*m+3)/(2*n-5))*q[n-1]["prob"][k-2][f][m-1]+((n-4-k+3*m)/(2*n-5))*q[n-1]["prob"][k-2][f][m]\
                                                        +((n-2*k-m+1)/(2*n-5))*q[n-1]["prob"][k-3][f][m]
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
 {'leaves': 7, 'prob': [0.66666667, 0.33333333]},
 {'leaves': 8, 'prob': [0.72727272, 0.24242424, 0.03030303]},
 {'leaves': 9, 'prob': [0.72727274, 0.25174825, 0.02097902]}]
for n in range(10,z):
    print(n)
    ann=[]
    for f in range(int(n/4)+1):
        a=0
        for k in range(2, int(n/2)+1):
            for m in range(int(n/3)+1):  
                a+= q[n]["prob"][k-2][f][m]
        ann.append(a)
    qq.append(dict(leaves=n, prob=ann))   
    
    
############test    
s=0
n=100
for f in range(int(n/4)+1):
    #s+=probquad(f,15)      
    for k in range(2, int(n/2)+1):
        for m in range(int(n/3)+1): 
            s+= q[n]["prob"][k-2][f][m]
#####################
import matplotlib.pyplot as plt 

for i in range(len(qq)):
    globals()["x"+str(i)]=[]
    globals()["y"+str(i)]=[]


for p in range(7,len(qq)):     
    globals()["x"+ str(p)]=list(range(int(p/4)+1))
    globals()["y"+ str(p)]=qq[p]["prob"]
    plt.plot(globals()["x"+ str(p)], globals()["y"+ str(p)], label = str(p)+" leaves")

plt.xlabel('Number of quadruple terminals') 
plt.ylabel('Probability distribution') 
#plt.title('') 
#plt.legend()   
plt.show()        


file="E:/sugerc/probquadruple7t500check.txt"
with open(file,"w") as f:
    for s in qq:
        f.write(str(s))
        f.write("\n")

for i in range(len(qq)):
    globals()["z"+str(i)]=0      # mean
    globals()["frac"+str(i)]=0  # for mean/n

for p in range(7,len(qq)):
    for j in range(int(p/4)+1):
        globals()["z"+str(p)] +=globals()["x"+ str(p)][j]*globals()["y"+ str(p)][j]

# mean/n :
for p in range(7,len(qq)):
    globals()["frac"+str(p)]= (globals()["z"+str(p)])/p
    
# st :
        
import math  
for i in range(len(qq)):
    globals()["bigv"+str(i)]=0
    globals()["var"+str(i)]=0
    globals()["st"+str(i)]=0

for i in range(len(qq)):
    globals()["stfrac"+str(i)]=0    #st/m
    
for p in range(7,len(qq)):
    for j in range(int(p/4)+1):
        globals()["bigv"+str(p)] +=(math.pow(globals()["x"+ str(p)][j],2))*globals()["y"+ str(p)][j]


for p in range(7,len(qq)):
     globals()["var"+str(p)]= globals()["bigv"+str(p)]-(math.pow(globals()["z"+str(p)],2))
     
for p in range(7,len(qq)):     
     globals()["st"+str(p)]=math.sqrt(globals()["var"+str(p)])  
        
for p in range(7,len(qq)):     
     globals()["stfrac"+str(p)]=(globals()["st"+str(p)])/p

import pandas as pd
mean=[]
st=[]
fracmean=[]  
fracst=[]
   
for i in range(7,len(qq)): 
    mean.append(globals()["z"+str(i)])
    st.append(globals()["st"+str(i)])
    fracmean.append(globals()["frac"+str(i)])
    fracst.append(globals()["stfrac"+str(i)])
       
d = {"leaves":list(range(7,z)),'Mean': mean, 'St': st,"Mean/n":fracmean,"St/n":fracst}
df = pd.DataFrame(data=d)     

df.to_csv('E:/sugerc/meanstquad500.csv')


























