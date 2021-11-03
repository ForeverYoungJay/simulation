import pandas as pd # 导入pandas 模块
# 读取数据


def experiment():
    path = "/Users/yangjiyi/master/Data-Ni3Al-SG-tensile-test/"
    files = ["Ni3Al17-A1.txt", "Ni3Al19-7.txt", "Ni3Al25011B1.txt"] #
    for file in files:
        filename = path + file
        data = pd.read_table(filename
                             , sep='\t')
        strain = data["true_strain"].to_list()
        stress = data["true_stress"]
        add(strain)


def add(list):
    data_csv = pd.read_csv('my_csv.csv',header=None) # 读取刚才写入的文件
    data_csv['strain'] = list # 新增列sresult 并写入数据
    data_csv.to_csv('my_csv.csv',mode="a", index=False, sep=',') # 将新增的列数据，增加到原始数据中

    data_csv = pd.read_csv('my_csv.csv') # 读取新增列后的csv文件
    print("新增后csv文件数据为：")
    print(data_csv)

if __name__ == '__main__':

    experiment()

