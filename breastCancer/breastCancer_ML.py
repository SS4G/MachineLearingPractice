
# coding: utf-8

# In[54]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
column_names = ['Sample code number',            
'Clump Thickness',               
'Uniformity of Cell Size',       
'Uniformity of Cell Shape',      
'Marginal Adhesion',             
'Single Epithelial Cell Size',
'Bare Nuclei',                   
'Bland Chromatin',               
'Normal Nucleoli',               
'Mitoses',                       
'Class',]  
data = pd.read_csv("D:/work_space/ML_practice/data/breast-cancer-wisconsin.csv", names=column_names)#.head(50)
print(type(data))#
data = data.replace('?', np.nan) # 去掉任何包含NAN的行
data=data.dropna(how='any')
data.shape
#data.dropna


# In[86]:

sr = data['Uniformity of Cell Size']
vc = sr.value_counts()
idxs = list(vc.index)
idxs.sort()
vals = [vc[i] for i in idxs]
#for i in sr.ind:
#    print(i)
#vc.sort_indexs()
#plt.plot()
plt.plot(idxs, vals)
plt.show()


# In[ ]:




# In[ ]:




# In[56]:

X_train, X_test, Y_train, Y_test=train_test_split(data[column_names[1:10]], data[column_names[10]], test_size=0.25, random_state=33)


# In[57]:

Y_test.value_counts()


# In[58]:

Y_train.value_counts()


# In[59]:

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
ss = StandardScaler()

#数据预处理 使其均值为 0 标准差为1 消除各个特征之间的 权重不一样的情况
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

lr = LogisticRegression()
sgdc = SGDClassifier()

lr.fit(X_train, Y_train) # 训练得出逻辑回归的参数
lr_y_predict = lr.predict(X_test) # 把测试集放到预测函数中得出结果

sgdc.fit(X_train, Y_train)
sgdc_y_predict = lr.predict(X_test)

print("acc of LR:", lr.score(X_test, Y_test))
print (classification_report(Y_test, lr_y_predict, target_names=['Benign', 'Malignant']))

print("acc of SGDC:", sgdc.score(X_test, Y_test))
print (classification_report(Y_test, sgdc_y_predict, target_names=['Benign', 'Malignant']))


# In[ ]:



