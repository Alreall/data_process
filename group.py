import pandas as pd
# 读取文件
path= r'/Users/yang/Downloads/前后车距离/data02/l2f5/1车道时间'
df = pd.read_csv('1.csv')
# 按照time进行分组，并转换为列表形式
timelist=list(df.groupby(['datetime']))
print(timelist)
# 遍历列表
for time in timelist:
    time_pd = pd.DataFrame(time[1])
    time_pd.to_csv(path+'/'+str(time[0])+'.csv')


