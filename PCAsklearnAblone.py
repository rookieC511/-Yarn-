# -*- coding: utf-8 -*-
import xlrd
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

# 读取表格数据，填充到矩阵作为数据集


# def read_data(X):
#     worksheet = xlrd.open_workbook('C.xlsx', '表单2')
#     sheet_names = worksheet.sheet_names()
#
#     for sheet_name in sheet_names:
#         sheet = worksheet.sheet_by_name(sheet_name)
#         rows = sheet.nrows  # 获取行数
#         cols = sheet.ncols  # 获取列数，尽管没用到
#         all_content = []
#
#         for m in range(1, rows):
#             for n in range(1, cols):
#                 X[m - 1][n - 1] = sheet.cell_value(m, n)  # 获取行列数据
#

# 读取xlsx的数据
# df = pd.read_excel('C.xlsx', '表单2')
# dataset = df.values  # 读取表格中的数据，放到矩阵中
#
# pca = PCA(n_components='mle')  # 'mle'：PCA类会用MLE算法根据特征的方差分布情况自己去选择一定数量的主成分特征来降维
# # pca = PCA(n_components=1)
# newX = pca.fit_transform(df)  # 等价于pca.fit(X)-训练 + pca.transform(X)-将数据X转换成降维后的数据
# invX = pca.inverse_transform(df)  #将降维后的数据转换成原始数据


# print(dataset)
# print("降维后的数据：", newX)
# print("维度：", newX.shape)
# print("保留成分的个数：", pca.n_components_)
# print("具有最大方差的成分：", pca.components_)
# print("所保留的n个成分各自的方差：", pca.explained_variance_)
# print("所保留的n个成分各自的方差百分比：", pca.explained_variance_ratio_)
# print("所保留的n个成分各自的方差百分比之和：", pca.explained_variance_ratio_.sum())

# 1.pca.components_：返回具有最大方差的成分。
# 2.pca.explained_variance_ratio_：返回 所保留的n个成分各自的方差百分比。
# 3.pca.n_components_：返回所保留的成分个数n。
# 4.pca对象的n_components值为n，即保留n个特征。
# 5.方差百分比之和大于95%时意味着几乎保留了所有的信息。即可以95%表达整个数据集，因此我们可以降到k维。
df = pd.read_excel('C.xlsx', '表单2')
dataset = df.values  # 读取表格中的数据，放到矩阵中
# pca = PCA()
# pca.fit(dataset)


pca = PCA(n_components='mle')  # 'mle'：PCA类会用MLE算法根据特征的方差分布情况自己去选择一定数量的主成分特征来降维
newX = pca.fit_transform(df)
invX = pca.inverse_transform(newX)  # 将降维后的数据转换成原始数据
data = pd.DataFrame(newX)
data.to_excel('C降维后.xlsx', index=False)
print('各个特征向量：', pca.components_)  # 返回模型的各个特征向量(具有最大方差的成分)
print('各个成分各自的方差百分比：', pca.explained_variance_ratio_)  # 返回各个成分各自的方差百分比
