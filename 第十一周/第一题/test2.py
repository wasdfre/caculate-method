# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:00:51 2020

@author: pc
"""


import numpy as np  

def f(x):
    return np.tan(x)+x


def f1(x):
    return 2+(np.tan(x)**2)


x=[np.pi/2+0.2]
eps=1e-14

fx=np.abs(f(x))
number_iteration=0;
F=[fx]
L=[]


while(fx>eps):
    Lambda=1
    
    df=np.double(f(x[-1])/f1(x[-1]))
    x1=x[-1]-Lambda*df         
    fx=np.abs(np.double(f(x1)))
    number_iteration=number_iteration+1

    
    while(fx>=F[-1]):
  
        Lambda=Lambda/2
        x1=x[-1]-Lambda*df
        fx=np.abs(np.double(f(x1)))
        
        number_iteration=number_iteration+1

    F.append(fx)
    x.append(x1)
    L.append(Lambda)



print('number_iteration=', number_iteration);
print('x*=', x[-1]);
print('f(x*)=', F[-1]);