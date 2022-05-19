# -*- coding: utf-8 -*-
import numpy as np


def xk(x,L):
    y=[]
    y.append(x)
    for n in range(1,L):
        p=x*y[-1]
        y.append(p)
        
    return y






N=2000
x=np.sort(np.random.random(N)*2-1)       #[-1,1]随机生成N个点，从小到大排序

y=np.zeros(N)
for k in range(0,N):
    y[k]=1/(1+25*x[k]**2)                     
    y[k]=y[k]+(np.random.random()*2-1)*0.1         #在y上加入扰动



#构建数据集：

L=25         #用25次多项式进行逼近
data=[]

for k in range(0,N):
    data.append(xk(x[k],L))

data=np.array(data)

label=np.array([y]).T

''''' LinearRegression '''  
X=np.hstack((data,np.ones(label.shape)))
Y=label

W=np.dot(np.linalg.pinv(X),Y)#利用广义逆求系数
w=W[0:-1]
b=W[-1]

y_train_predict=np.dot(data,w)+b
''''' 线性回归建模 '''  




''' 测试模型 '''
M=120
x_test=np.sort(np.random.random(M)*2-1)       #[-1,1]随机生成M个点，从小到大排序

y_test=np.zeros([M,1])
for k in range(0,M):
    y_test[k]=1/(1+25*x_test[k]**2)

    
data_test=[]
for k in range(0,M):
    data_test.append(xk(x_test[k],L))

data_test=np.array(data_test)

y_predict=np.dot(data_test,w)+b



''' 测试集误差 '''

Error_test=np.sqrt(np.sum((y_predict-y_test)**2)/len(y_test))
print('Error_test',Error_test)




''' 画图 '''

import matplotlib.pyplot as plt  

''' 训练集 '''
fig1 = plt.figure('fig1')
plt.plot(x,y,'r+',lw=1)    #训练集数据
plt.plot(x,y_train_predict,'b',lw=1)    #模型


''' 测试集 '''
fig2 = plt.figure('fig2')
plt.plot(x_test,y_predict,'b',lw=1)   #预测值
plt.plot(x_test,y_test,'r+',lw=1)     #测试集精确值














