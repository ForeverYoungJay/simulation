import numpy as np
import scipy
from scipy.interpolate  import lagrange
import pandas as pd
import os


def lagrange_stress(x,y,strain):
    ret = lagrange(x,y)
    return ret(strain)


def read_data_simulation(file,sample):
    path = f"/Users/yangjiyi/master/research/damask/result/{file}/{sample}/postProc/"  # 文件夹目录
    files = os.listdir(path)
    strainl = []
    stressl = []
    stran_stress_dict = {}
    for file in files:  # 遍历文件夹
        filename = path + file
        data = pd.read_table(filename
                             , sep='\t')  # 读入txt文件，分隔符为\t
        strain = data["1_ln(V)"].mean()
        stress11 = data["1_Cauchy"].mean()
        strainl.append(strain)
        stressl.append(stress11)
        stran_stress_dict[strain] = stress11
    strainl.sort()

    return stran_stress_dict,strainl

def read_data_experimet():
    path = "/Users/yangjiyi/master/Data-Ni3Al-SG-tensile-test/"
    files = ["Ni3Al17-A1.txt", "Ni3Al19-7.txt", "Ni3Al25011B1.txt"]  #
    sample_data = []
    for file in files:
        filename = path + file
        data = pd.read_table(filename
                             , sep='\t')
        strain = data["true_strain"]
        stress = data["true_stress"]
        min = stress.min()
        max = stress.max()
        if max < 400:
            stress *= 1e6
        strain_stress_dict = dict(zip(strain,stress))
        sample_data.append(strain_stress_dict)

    return sample_data


def loss(y, y_pred):
    """
    loss = 1/2 * (y - y_pred)^2
    :param y:class:`ndarray <numpy.ndarray>` 样本结果(n, m)
    :param y_pred:class:`ndarray <numpy.ndarray>` 样本预测结果(n, m)
    :return: shape(n, m)
    """
    return np.sqrt(0.5*np.sum((np.array(y)-np.array(y_pred))**2))


def fitting(experimentdata=dict,simulationdata=dict,strainl=list):
    strainl_experiment = list(experimentdata.keys())
    stress_simulations = []
    for strain in strainl_experiment:
        stress = []
        strainl.append(strain)
        strainl.sort()
        index = strainl.index(strain)
        strainl.pop(index)
        if index <= 5:
            for i in range(0,10):
                stress.append(simulationdata[strainl[i]])
            strains = strainl[0:10]
        elif index >= len(strainl)-5:
            for i in range(len(strainl)-10,len(strainl)):
                stress.append(simulationdata[strainl[i]])
            strains = strainl[len(strainl)-10:len(strainl)]
        else:
            for i in range(index-5,index+5):
                stress.append(simulationdata[strainl[i]])
            strains = strainl[index-5:index+5]

        stress_simulation = lagrange_stress(strains,stress,strain)
        stress_simulations.append(stress_simulation)
    loss_sample = loss(list(experimentdata.values()),stress_simulations)

    return loss_sample



def creat_csv(data):
    frame = pd.DataFrame(data,
                         columns=["n", 'h0', 's0',"si","loss"])
    frame.to_csv("/Users/yangjiyi/master/research/damask/testcsv_result.csv")



if __name__ == '__main__':
    sample_list = ["17A1","197","250"]
    experiment = ["Ni3Al17-A1.txt", "Ni3Al19-7.txt", "Ni3Al25011B1.txt"]
    path_result = "/Users/yangjiyi/master/research/damask/result/"
    files = os.listdir(path_result)
    datas = []
    for file in files:
        data = file.split("_")
        loss_all = []
        for sample in sample_list:
            stran_stress_dict, strainl = read_data_simulation(file,sample)
            sample_data = read_data_experimet()
            loss_sample = fitting(sample_data[sample_list.index(sample)],stran_stress_dict,strainl)
            loss_all.append(loss_sample)
        losses = np.mean(loss_all)
            # result 为插入的list数据
        dataframe = pd.DataFrame({'n': [int(data[0])]
                                , 'h0': [int(data[1])]
                                , "s0":[int(data[2])]
                                ,"si":[int(data[3])]
                                ,"lo":[losses]})

        print(data,":",losses)
        # 'Experiments.csv' 为导出的文件名
        dataframe.to_csv('data_loss_full.csv', mode='a', header=False,index=False)

