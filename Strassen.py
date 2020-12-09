"""
计算矩阵的乘积
Strassen
"""
import numpy as np

a = np.array([[6, 7, 9, 3], [7, 2, 1, 8], [5, 7, 3, 2], [4, 8, 4, 7]])
b = np.array([[4, 8, 6, 3], [9, 2, 1, 7], [7, 8, 2, 9], [9, 2, 6, 8]])


def cutMat(mat):
    """
    切割矩阵，将其按照中线切分为四份
    :param mat:
    :return:
    """
    cutLoc = len(mat) / 2
    a, b, c, d = [], [], [], []
    for i in range(len(mat)):
        if i < cutLoc:
            for j in range(len(mat)):
                if j < cutLoc:
                    a.append(mat[i][j])
                else:
                    b.append(mat[i][j])
        else:
            for j in range(len(mat)):
                if j < cutLoc:
                    c.append(mat[i][j])
                else:
                    d.append(mat[i][j])
    return np.array(a).reshape((2, 2)), np.array(b).reshape((2, 2)), np.array(c).reshape((2, 2)), np.array(d).reshape(
        (2, 2))


def strassen(a, b):
    mLen = len(a)
    if mLen == 2:
        a11, a12, a21, a22 = a[0][0], a[0][1], a[1][0], a[1][1]
        b11, b12, b21, b22 = b[0][0], b[0][1], b[1][0], b[1][1]
        d1 = (a11 + a22) * (b11 + b22)
        d2 = (a21 + a22) * b11
        d3 = a11 * (b12 - b22)
        d4 = a22 * (b21 - b11)
        d5 = (a11 + a12) * b22
        d6 = (a21 - a11) * (b11 + b12)
        d7 = (a12 - a22) * (b21 + b22)
        return np.array([[d1 + d4 - d5 + d7, d3 + d5], [d2 + d4, d1 + d3 - d2 + d6]])
    else:
        A11, A12, A21, A22 = cutMat(a)
        B11, B12, B21, B22 = cutMat(b)
        d1 = strassen((A11 + A22), (B11 + B22))
        d2 = strassen((A21 + A22), B11)
        d3 = strassen(A11, (B12 - B22))
        d4 = strassen(A22, (B21 - B11))
        d5 = strassen((A11 + A12), B22)
        d6 = strassen((A21 - A11), (B11 + B12))
        d7 = strassen((A12 - A22), (B21 + B22))
        return np.array([[d1 + d4 - d5 + d7, d3 + d5], [d2 + d4, d1 + d3 - d2 + d6]])


s = strassen(a, b)
ans1 = np.hstack((s[0][0], s[0][1]))
ans2 = np.hstack((s[1][0], s[1][1]))
ans = np.vstack((ans1, ans2))
print(ans)
