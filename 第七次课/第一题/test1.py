# -*- coding: utf-8 -*-
import numpy as np

N=200
#排序的目的是调用plot不会出现杂乱的线
x=np.sort(np.random.random(N)*2-1)       #[-1,1]随机生成N个点，从小到大排序

y=np.zeros(N)
for k in range(0,N):
    y[k]=np.sin(np.pi*x[k]/2-np.pi/2)                     
    y[k]=y[k]+(np.random.random()*2-1)*0.2         #在y上加入扰动



#构建数据集：第一列为x,第二列为x^2
#没有常数项
data=np.zeros([N,2])

for k in range(0,N):
    data[k,0]=x[k]
    data[k,1]=x[k]**2
#列向量
label=np.array([y]).T

''''' LinearRegression '''  
import sklearn.linear_model as skl
lr=skl.LinearRegression()
lr.fit(data, label)
#预测值
y_train_predict=lr.predict(data)
''''' 线性回归建模 '''  




''' 测试模型 '''
M=50
x_test=np.sort(np.random.random(M)*2-1)       #[-1,1]随机生成M个点，从小到大排序

y_test=np.zeros([M,1])
for k in range(0,M):
    y_test[k]=np.sin(np.pi*x_test[k]/2-np.pi/2)

#构建X    
data_test=np.zeros([M,2])
for k in range(0,M):
    data_test[k,0]=x_test[k]
    data_test[k,1]=x_test[k]**2
    
y_predict=lr.predict(data_test)



''' 测试集误差 '''



Error_test=np.sqrt(np.sum((y_predict-y_test)**2)/len(y_test))
print('Error_test',Error_test)




''' 画图 '''

import matplotlib.pyplot as plt  

''' 训练集 '''
fig2 = plt.figure('fig1')
plt.plot(x,y,'r+',lw=1)    #原数据
plt.plot(x,y_train_predict,'b',lw=1)    #模型


''' 测试集 '''
fig2 = plt.figure('fig2')
plt.plot(x_test,y_predict,'b',lw=1)   #预测解
plt.plot(x_test,y_test,'r+',lw=1)     #精确值


















