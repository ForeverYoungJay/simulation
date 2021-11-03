"""# 1）import  【引入相关模块】
import tensorflow as tf

# 2）train,test  【告知喂入网络的训练集测试集以及相应的标签】
fashion = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3）model=tf.keras.models.Sequential  【在Sequential中搭建网络结构，相当于走一遍前向传播】
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 4）model.compile  【告知训练时选择哪种优化器，选择哪个损失函数，选择哪种评测指标】
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

# 5）model.fit 【在fit()中执行训练过程，告知训练集合测试集的输入特征和标签，告知batch大小，告知要迭代多少次数据集】
model.fit(x_train, y_train, batch_size=32, epochs=5, validation_data=(x_test, y_test), validation_freq=1)

# 6）model.summary  【打印网络结构和参数统计】
model.summary()"""


#!usr/bin/env python
#_*_ coding:utf-8 _*_
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split #这里是引用了交叉验证
from sklearn.linear_model import LinearRegression  #线性回归
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pd_data = pd.read_csv("data_loss_full.csv")
#剔除日期数据，一般没有这列可不执行，选取以下数据http://blog.csdn.net/chixujohnny/article/details/51095817
x=pd_data.iloc[:,0:4]
y=pd_data.iloc[:,-1]
linreg = LinearRegression()
model=linreg.fit(x, y)
print (model)
# 训练后模型截距
print (linreg.intercept_)
# 训练后模型权重（特征个数无变化）
print (linreg.coef_)

