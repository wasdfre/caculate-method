import numpy as np
import matplotlib.pyplot as plt
 
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
  
#数据准备

def f(x):
    y=1/(1+25*x**2)
    return y
#这个计算x和y值的方法
X=np.arange(-1,1,0.1) #定义插值节点X
Y= np.array(list(map(f,X)))
new_x=np.arange(-1,1,0.01) #定义待计算点
Y_actual=np.array(list(map(f,new_x)))
 
#进行样条差值
import scipy.interpolate as spi
 

#进行三次样条拟合
ipo3=spi.splrep(X,Y,k=3) #样本点导入，生成参数
iy3=spi.splev(new_x,ipo3) #根据观测点和样条参数，生成插值

 
error=np.linalg.norm(Y_actual-iy3)
print('error=',error)
 
##作图
plt.plot(X,Y,'o',)
plt.plot(new_x,iy3)
plt.title('三次样条插值')


 