import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图
import pandas as pd
# 数据


import numpy as np



df = pd.read_csv("data_loss_full.csv")
print(df.iloc[:,-1].min())

"""y_train = np.genfromtxt(path,delimiter=",",skip_header=1,usecols=(-1))
print(y_train/max(y_train))"""

"""data_20 = data[data["n"]=="20"]
data_100 = data[data["n"]=="100"]

loss_20 = data_20["ex"].apply(float) - data_20["sr"].apply(float)
loss_100 = data_100["ex"].apply(float) - data_100["sr"].apply(float)

print("20:",loss_20.mean(),"100:",loss_100.mean())
print()


data_200 = data[data["h0"]=="200"]
data_180 = data[data["h0"]=="180"]

loss_200 = data_200["ex"].apply(float) - data_200["sr"].apply(float)
loss_180 = data_180["ex"].apply(float) - data_180["sr"].apply(float)
print("200:",loss_200.mean(),"180:",loss_180.mean())


data_5000 = data[data["si"]=="5000"]
data_3500 = data[data["si"]=="3500"]

loss_5000 = data_5000["ex"].apply(float) - data_5000["sr"].apply(float)
loss_3500 = data_3500["ex"].apply(float) - data_3500["sr"].apply(float)
print("5000:",loss_200.mean(),"3500:",loss_180.mean())

#100大 200大  x 500大"""

