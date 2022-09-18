import csv
import math
import pandas as pd
import copy
f = open(r'1949.5.csv')
path = r'/Users/yang/Downloads/前后车距离/data'
reader = csv.reader(f)
df = pd.read_csv('1949.5.csv',index_col='vehicle_id')
m = []
# m用于存储每一行的元素
for row in reader:
    m.append(row)
# 获取行的个数
x = len(m)
aa = {}                 # 字典，用于表示对应编号的前后车
y = df['y']
z = list(y)
for i in range(1, x):
    subOD = []  # sub outputdata
    a1 = []
    a2 = []
    b = []
    temf = []  # 存储后方车辆的距离
    temfdic = []  # 存储后方车辆的编号
    teml = []  # 存储前方车辆的距离
    temldic = []  # 存储前方车辆的编号
    for j in range(1, x):
        deltY = float(m[i][13]) - float(m[j][13])  # 第i行，第1列的元素，对应的x坐标
        x1 = m[i][3]
        x2 = m[j][3]
        # 如果小于0，那么就存储为前车，否则存储为后车
        if deltY < 0:
            teml.append(abs(deltY))
            temldic.append(x2)
        else:
            temf.append(deltY)
            temfdic.append(x2)
    # print(teml)
    '''
    出现空值的情况是，如果这是头车，那么就不存在比他大的了，那么在这一时刻她就是空值
    '''
    '''
    如果teml不是空，那么就存储到hebingl里面，添加一个b
    如果不设置else，那么就只存储了一个b
    '''
    # 如果都不是空的话
    # subOD存储的是前后车的一个编号
    # print(temf)
    if teml and len(temf) != 1:
        hebingl = dict(zip(teml, temldic))              # 存储前方车辆的字典
        for t1 in hebingl.keys():                       # 遍历距前方车辆的距离
            a1.append(t1)
        c1 = min(a1)                                    # 距离最近的前方车辆
        b.append(c1)
        subOD.append(hebingl[b[0]])                     # 添加第一个元素,前车
        hebingf = dict(zip(temf, temfdic))              # 存储后方车辆的字典
        for t2 in hebingf.keys():                       # 遍历距后方车辆的距离
            a2.append(t2)
        a2.remove(0)
        c2 = min(a2)                                    # 距离最近的后方车辆
        b.append(c2)
        subOD.append((hebingf[b[1]]))                   # 添加第二个元素，后车
    # 如果前方是空，后方不是空，就前方的添加None，后方添加车辆
    elif not teml and len(temf) != 1:
        subOD.append(9999)
        hebingf = dict(zip(temf, temfdic))              # 存储后方车辆的字典
        for ii in hebingf.keys():                       # 遍历距后方车辆的距离
            a2.append(ii)
        a2.remove(0)
        c2 = min(a2)
        b.append(c2)
        subOD.append((hebingf[b[0]]))                   # 添加第二个元素，后车
    # 如果后方是空，前方不是空，就后方的添加None，前方添加车辆
    elif teml and len(temf) == 1:
        hebingl = dict(zip(teml, temldic))              # 存储前方车辆的字典
        for ii in hebingl.keys():                       # 遍历距前方车辆的距离
            a1.append(ii)
        c1 = min(a1)
        b.append(c1)
        subOD.append(hebingl[b[0]])                     # 添加第一个元素,前车
        subOD.append(9999)
    if subOD:
        bb = {m[i][3]: subOD}                           # 车辆对应的前后车的字典情况
        aa.update(bb)                                   # 存储车辆的前后车的字典

# 遍历的是按照顺序的，所以aa里面存储的也是按照顺序来的
df.loc[:, 'lead'] = -1000
df.loc[:, 'follow'] = -1000
for key, value in aa.items():
    # if x != 1:
    if df.loc[int(key), 'y'] == min(z):
        df.loc[int(key), 'lead'] = value[0]
        df.loc[int(key), 'follow'] = -1000
    elif df.loc[int(key), 'y'] == max(z):
        df.loc[int(key), 'lead'] = -1000
        df.loc[int(key), 'follow'] = value[1]
    else:
        df.loc[int(key), 'lead'] = value[0]
        df.loc[int(key), 'follow'] = value[1]
    # else:
    #     df.loc[int(key), 'lead'] = -1000
    #     df.loc[int(key), 'follow'] = -1000
df.to_csv('data_result.csv')