import csv
import math
import pandas as pd
import copy
f = open(r'final_result.csv')
path = r'/Users/yang/Downloads/前后车距离/data'
reader = csv.reader(f)
df = pd.read_csv('final_result.csv',index_col='vehicle_id')
m = []
# m用于存储每一行的元素
for row in reader:
    m.append(row)
# 获取行的个数
x = len(m)
print(x)
