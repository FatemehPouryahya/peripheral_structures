#put it on one plot 
#index of dispersion
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.optimize import curve_fit


meanst = pd.read_csv('E:/sugerc/indicesOfDispersion/pairedtermianls.csv')

a = meanst.values
x1=a[2:502,0]
zy=a[2:502,8]


mst = pd.read_csv('E:/sugerc/indicesOfDispersion/triples.csv')

ta = mst.values
tx1=ta[2:502,0]
tzy=ta[2:502,8]

qmst = pd.read_csv('E:/sugerc/indicesOfDispersion/quadruplestype1.csv')

qa = qmst.values
qx1=qa[1:501,0]
qzy=qa[1:501,8]


nqmst = pd.read_csv('E:/sugerc/indicesOfDispersion/quadruplestype2.csv')

nqa = nqmst.values
nqx1=nqa[:500,0]
nqzy=nqa[:500,8]

for p in range(1,len(x1)):
    ff1, =plt.plot(x1[p],zy[p],'-o', color='magenta',markersize=0.5, label='Terminal pairs')
    ff2, =plt.plot(tx1[p],tzy[p],'-o', color='cyan',markersize=0.5, label='Triples')     
    ff3, =plt.plot(qx1[p],qzy[p],'-o', color='Orange',markersize=0.5, label='Type I Quadruples')  
    ff4, =plt.plot(nqx1[p],nqzy[p],'-o', color='purple',markersize=0.5, label='Type II Quadruples') 
plt.xlabel('Number of terminals') 
plt.ylabel('Index of disparsion') 
plt.ylim(-0.05, 1.4);
#plt.xlim(1, 500);
#plt.title('') 
plt.legend(handles=[ff1,ff2,ff3,ff4])   
plt.show() 

############
#Variance
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.optimize import curve_fit

meanst = pd.read_csv('E:/sugerc/indicesOfDispersion/pairedtermianls.csv')
a = meanst.values
x=a[2:502,1]
y=a[2:502,8]
y22=np.log(y)

def funcd(x, a, b,c):
    return(a*(x**c+b))

v=y**2
v1=np.log(v)
p1,c1=curve_fit(funcd, x,v1, maxfev = 100000)
zzz=((p1[0])*(x**(p1[2])+(p1[1])))
#zzz=((-5.74747297e+01)*(x**(1.55521358e-02)+(-9.45067307e-01)))
plt.plot(x,v1)
plt.plot(x,zzz)
plt.xlabel('Number of terminals') 
plt.ylabel('log normalized variance & fitted curve') 
plt.show()

mst = pd.read_csv('E:/sugerc/indicesOfDispersion/triples.csv')

# fresh start
ta = mst.values
tx=ta[2:502,1]
ty=ta[2:502,8]
ty22=np.log(ty)



tv=ty**2
tv1=np.log(tv)
tp1,tc1=curve_fit(funcd, tx,tv1, maxfev = 100000)
tzzz=((tp1[0])*(tx**(tp1[2])+(tp1[1])))
#tp1=[-9.48562372e+01, -9.66026960e-01,  9.94972992e-03]
#-94.8562372(x^(0.00994972992)-0.966026960)
plt.plot(tx,tv1)
plt.plot(tx,tzzz)
plt.xlabel('Number of terminals') 
plt.ylabel('log normalized variance & fitted curve') 
plt.show()

qmst = pd.read_csv('E:/sugerc/indicesOfDispersion/quadruplestype1.csv')

qa = qmst.values
qx=qa[1:501,1]
qy=qa[1:501,8]
qy22=np.log(qy)


qv=qy**2
qv1=np.log(qv)
qp1,qc1=curve_fit(funcd, qx,qv1, maxfev = 100000)
qzzz=((qp1[0])*(qx**(qp1[2])+(qp1[1])))
#qp1=[-3.64030947e+04, -9.99894547e-01,  2.95202562e-05]
#(-36403.0947)(x^(0.0000295202562)-0.999894547)
plt.plot(qx,qv1)
plt.plot(qx,qzzz)
plt.xlabel('Number of terminals') 
plt.ylabel('log normalized variance & fitted curve') 
plt.show()
########


nqmst = pd.read_csv('E:/sugerc/indicesOfDispersion/quadruplestype2.csv')

nqa = nqmst.values
nqx=nqa[:500,1]
nqy=nqa[:500,8]
nqy22=np.log(nqy)

nqv=nqy**2
nqv1=np.log(nqv)
nqp1,nqc1=curve_fit(funcd, nqx,nqv1, maxfev = 100000)
nqzzz=((nqp1[0])*(nqx**(nqp1[2])+(nqp1[1])))
#nqp1=[-2.66857961e+04, -9.99883484e-01,  3.89960569e-05]
#(-2.66857961e+04)(x^( 3.89960569e-05)-9.99883484e-01)
plt.plot(nqx,nqv1)
plt.plot(nqx,nqzzz)
plt.xlabel('Number of terminals') 
plt.ylabel('log normalized variance & fitted curve') 
plt.show()


#now
i1,=plt.plot(x,v1,'-o', color='magenta',markersize=0.7, label='Terminal pairs')
i2,=plt.plot(x,zzz, color='yellow')
ii1,=plt.plot(tx,tv1,'-o', color='cyan',markersize=0.7, label='Triples') 
ii2,=plt.plot(tx,tzzz, color='yellow')   
iii1,=plt.plot(qx,qv1,'-o', color='Orange',markersize=0.7, label='Type I Quadruples')
iii2,=plt.plot(qx,qzzz, color='yellow',label='Fitted curve')
niii1,=plt.plot(nqx,nqv1,'-o', color='purple',markersize=0.7, label='Type II Quadruples')
niii2,=plt.plot(nqx,nqzzz, color='yellow',label='Fitted curve')
plt.xlabel('Number of terminals') 
plt.ylabel('log normalized variance & fitted curve') 
plt.legend(handles=[i1,ii1,iii1,niii1,iii2])
plt.show()
############################
#type 2
#quadruple
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.optimize import curve_fit

nqmst = pd.read_csv('E:/sugerc/type2quadmeanstquad500.csv')

nqa = nqmst.values
nqx1=nqa[:,1]
nqzy=nqa[:,4]


for p in range(1,len(nqx1)):     
    plt.plot(nqx1[p],nqzy[p],'-o', color='black',markersize=0.5)
plt.xlabel('Number of terminals') 
plt.ylabel('Normalized expected value') 
#plt.ylim(0, 0.05);
#plt.title('') 
#plt.legend()   
plt.show() 

nqx=nqa[:,1]
nqy=nqa[:,5]

nqy22=np.log(nqy)
def funcd(x, a, b,c):
    return(a*(x**c+b))

nqp,nqc=curve_fit(funcd, nqx,nqy22, maxfev = 100000)
nqfz=((nqp[0])*(nqx**(nqp[2])+(nqp[1])))
#nqp=[,, ]
plt.plot(nqx,nqy22)
plt.plot(nqx,nqfz)
plt.xlabel('Number of terminals') 
plt.ylabel('log normalized st & fitted curve') 
plt.show()

nqv=nqy**2
nqv1=np.log(nqv)
nqp1,nqc1=curve_fit(funcd, nqx,nqv1, maxfev = 100000)
nqzzz=((nqp1[0])*(nqx**(nqp1[2])+(nqp1[1])))
#nqp1=[-2.66857961e+04, -9.99883484e-01,  3.89960569e-05]
#(-2.66857961e+04)(x^( 3.89960569e-05)-9.99883484e-01)
plt.plot(nqx,nqv1)
plt.plot(nqx,nqzzz)
plt.xlabel('Number of terminals') 
plt.ylabel('log normalized variance & fitted curve') 
plt.show()
    
