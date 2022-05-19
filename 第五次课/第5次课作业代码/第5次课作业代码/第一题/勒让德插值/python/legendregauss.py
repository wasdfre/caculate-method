import numpy as np
from lengendre import legendre
def legendregauss(n,m):
    if n==0:
        return []

    z=[]
    error=1e-14
    h=n**(-2)
    a=-1
    b=a+h
    number_newton=0;
    for k in range(1,n-m+1):
    
        legendre_a=legendre(n,m,a)
        legendre_b=legendre(n,m,b)
        while(legendre_a*legendre_b>0):
            a=b
            legendre_a=legendre_b
            
            b=a+h
            legendre_b=legendre(n,m,b)
    
        x=(a+b)*0.5
        xright=b
        while(np.abs(x-xright)>error):
            xright=x
            x=x-legendre(n,m,x)/legendre(n,m+1,x)
            number_newton+=1;
        z.append(x)
        a=x+h
        b=a+h
    return np.array(z)
# def legendregauss(n,m):
#     if n==0:
#         return []

#     z=[]
#     error=1e-14
#     h=n**(-2)
#     a=-1
#     b=a+h
    
#     for k in range(1,n-m+1):
    
#         legendre_a=legendre(n,m,a)
#         legendre_b=legendre(n,m,b)
#         while(legendre_a*legendre_b>0):
#             a=b
#             legendre_a=legendre_b
            
#             b=a+h
#             legendre_b=legendre(n,m,b)
    
#         x=(a+b)*0.5
#         xright=b
#         while(np.abs(x-xright)>error):
#             xright=x
#             x=x-legendre(n,m,x)/legendre(n,m+1,x)
    
#         z.append(x)
#         a=x+h
#         b=a+h
    
#     return np.array(z)