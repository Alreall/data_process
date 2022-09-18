import pandas as pd

file = pd.read_csv('final_result.csv',usecols=['vehicle_id','datetime','vehicle_type','velocity','traffic_lane','longitude','latitude','kilopost','vehicle_length','detected_flag','y','lead','follow'])
df=pd.DataFrame(file)
df.to_csv('final_result.csv',index=False)



