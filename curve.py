import os
from numpy import *
# 需导入要用到的库文件
import numpy as np  # 数组相关的库
import matplotlib.pyplot as plt  # 绘图库
import pandas as pd



def strain_stress_curve(files,color,label):
    strainl = []
    stressl = []
    for file in files: # 遍历文件夹
        filename = path+file
        delete_lines(filename)
        data = pd.read_table(filename
                             , sep='\t')  # 读入txt文件，分隔符为\t
        strain = data["1_ln(V)"].mean()
        stress11 = data["1_Cauchy"].mean()
        strainl.append(strain)
        stressl.append(stress11)
    plt.ylabel("stress")
    plt.xlabel("strain")
    plt.scatter(strainl, stressl,color=color,label= label)


def experiment():
    path = "/Users/yangjiyi/master/Data-Ni3Al-SG-tensile-test/"
    files = ["Ni3Al17-A1.txt", "Ni3Al19-7.txt", "Ni3Al25011B1.txt"] #
    for file in files:
        filename = path + file
        data = pd.read_table(filename
                             , sep='\t')
        strain = data["true_strain"]
        stress = data["true_stress"]
        min = stress.min()
        max = stress.max()
        if max < 400 :
            stress *= 1e6
        plt.scatter(strain, stress, label=file)
    plt.legend()

def delete_lines(filename):
    fin = open(filename, 'r')
    a = fin.readlines()
    count = 0
    for row in a:
        first = row.split("\t")[0]
        if first == "inc":
            break
        else:
            count += 1
            fout = open(filename, 'w')
            b = ''.join(a[count:])  # count为前N行
            fout.write(b)

if __name__ == '__main__':

    path_result = "/Users/yangjiyi/master/research/damask/result/"
    files = os.listdir(path_result)
    #files = ["20_200_30_5000",]
    for file in files:
        sample = ["17A1","197","250"]
        for sm in sample:
            path = f"/Users/yangjiyi/master/research/damask/result/{file}/{sm}/postProc/"   # 文件夹目录
            #path = f"/Users/yangjiyi/master/research/damask/bad/20_200_30_5000/{sm}/postProc/"
            files = os.listdir(path)  # 得到文件夹下的所有文件名称
            colorlist = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'chocolate', 'darkmagenta', 'deeppink', 'gold', 'orange']
            strain_stress_curve(files,colorlist[sample.index(sm)],file+sm)
            plt.legend()

        experiment()
        plt.savefig(f"/Users/yangjiyi/master/research/damask/{file}.jpg")
        plt.show()

