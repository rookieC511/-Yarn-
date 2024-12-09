import pandas as pd

# 读取 iris.data 文件
file_path = "./datasets/iris/iris.data"

# 定义列名
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# 转换 iris.data 文件
file_path = "./datasets/iris/iris.data"
iris_data = pd.read_csv(file_path, header=None, names=columns)