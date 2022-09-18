import pandas as pd
import numpy as np
from tqdm import tqdm
import os
def get_data(path):
    df_list = []
    for file in tqdm(os.listdir(path)):  ## 进度条
        file_path = os.path.join(path, file)
        df = pd.read_csv(file_path)
        df_list.append(df)
    df = pd.concat(df_list)
    return df
cPath = '/Users/yang/Downloads/前后车距离/data02/l2f2/f2汇总'
test_df = get_data(cPath)
test_df.to_csv(path_or_buf="/Users/yang/Downloads/前后车距离/data02/l2f2/f2汇总/final_result.csv", index=False)         # 保存为CS/Users/yang/Downloads/前后车距离/data1V文件