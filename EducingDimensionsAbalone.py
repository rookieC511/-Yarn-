# -*- coding: utf-8 -*- 
import numpy as np
import xlrd


# 读取表格数据，填充矩阵作为数据集
def read_data(X):
    worksheet = xlrd.open_workbook(u'abalone.xlsx')
    sheet_names = worksheet.sheet_names()

    for sheet_name in sheet_names:
        sheet = worksheet.sheet_by_name(sheet_name)
        rows = sheet.nrows  # 获取行数
        cols = sheet.ncols  # 获取列数
        all_content = []

        for m in range(1, rows):
            for n in range(1, cols):
                print(m, n)
                X[m - 1][n - 1] = sheet.cell_value(m, n)  # 获取行列数据


class PCA(object):
    def __init__(self, X, K):
        self.X = X  # 样本矩阵X
        self.K = K  # K阶降维矩阵的K值
        self.centralX = []  # 矩阵X的中心化
        self.C = []  # 样本集的协方差矩阵C
        self.U = []  # 样本矩阵X的降维转换矩阵
        self.Z = []  # 样本矩阵X的降维矩阵Z

        self.centralX = self._centralized()
        self.C = self._cov()
        self.U = self._U()
        self.Z = self._Z()  # Z = XU求得

    # 矩阵X的中心化
    def _centralized(self):
        centralX = []
        mean = np.array([np.mean(attr) for attr in self.X.T])  # 样本集的特征均值
        centralX = self.X - mean  # 样本集的中心化
        print('样本集的特征均值:\n', mean)

        return centralX

    # 求样本矩阵X的协方差矩阵C
    def _cov(self):
        # 样本集的样例总数
        ns = np.shape(self.centralX)[0]
        # 样本矩阵的协方差矩阵C
        C = np.dot(self.centralX.T, self.centralX) / (ns - 1)
        print('样本矩阵X的协方差矩阵C:\n', C)
        return C

    # 求协方差矩阵C的特征值、特征向量
    def _U(self):
        # 先求X的协方差矩阵C的特征值和特征向量
        a, b = np.linalg.eig(self.C)  # 特征值赋值给a，对应特征向量赋值给b
        print('样本集的协方差矩阵C的特征值:\n', a)
        print('样本集的协方差矩阵C的特征向量:\n', b)

        # 给出特征值降序的topK的索引序列
        ind = np.argsort(-1 * a)

        # 构建K阶降维的降维转换矩阵U
        UT = [b[:, ind[i]] for i in range(self.K)]  # 获取最大的k个值的
        U = np.transpose(UT)  # 构成降维转换矩阵
        print('%d阶降维转换矩阵U:\n' % self.K, U)
        return U

    # 通过低阶转换矩阵，把原矩阵转换成低维矩阵
    def _Z(self):
        Z = np.dot(self.X, self.U)  # 计算X和转换矩阵的乘积，得到降维后的矩阵
        print('样本矩阵X的降维矩阵Z:\n', Z)
        print('原矩阵的维度:', np.shape(X))
        print('降维后的维度:', np.shape(Z))
        return Z


if __name__ == '__main__':
    # 读取xlsx的数据
    X = np.zeros([4177, 8])  # 创建0矩阵
    dataset = read_data(X)  # 读取表格中的数据，放到矩阵中

    # 降维
    K = np.shape(X)[1] - 7  # 降低维数，k为得到结果的维度 []里0—表示行数、1—表示列数
    pca = PCA(X, K)  # 调用PCA主函数
