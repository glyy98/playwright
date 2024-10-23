import pandas as pd
import json


# 读取 Excel 文件，产品提供的现场数据,需要把点位列名改为project_name
#先把参数配置表的数据导出来，pm提供的标准数据丢进去，机构-二级-点位类型-点位名名称，id直接乱码生成
df = pd.read_excel(r'C:\Users\Administrator\AquaProjects\aqua_test\TTTTTTT\zhongyuan.xlsx')

# 读取点位映射表（点位名称到 ID 的映射），数据库点位表中的id，点位名称，去数据库   encoding='ISO-8859-1'
mapping_df = pd.read_excel(r'C:\Users\Administrator\AquaProjects\aqua_test\TTTTTTT\7#3265.xlsx')
print(mapping_df.columns)
# 创建点位名称到 ID 的映射字典
point_mapping = dict(zip(mapping_df['agents'], mapping_df['id']))


# 用点位 ID 替换点位名称，并转换为 JSON 格式
#将原先点位名称改成id，[str(point_mapping.get(x, "unknown"))]  结果是["504872283366490245"]
df['agents'] = df['agents'].apply(lambda x: json.dumps([str(point_mapping.get(x, "unknown"))]))


# 保存结果到新的 Excel 文件或 CSV 文件
df.to_excel(r'C:\Users\Administrator\AquaProjects\aqua_test\TTTTTTT\9.xlsx', index=False)

