"""
寻找最小矩阵相乘方法，以及最小矩阵数量乘法次数
"""

import numpy as np

ans = []


def getAns(matDir, toBeFind):
    """
    递归调用，从[1,5]得到选择路劲
    :param matDir:
    :param toBeFind:
    :return:
    """
    if toBeFind not in matDir.keys():
        ans.append(toBeFind)
        return
    ans.append(toBeFind)
    toBeFind_this = matDir[toBeFind][0]
    getAns(matDir, toBeFind_this)
    toBeFind_this = matDir[toBeFind][1]
    getAns(matDir, toBeFind_this)


def handleAns():
    m1 = "M1"
    m2 = "M2"
    m3 = "M3"
    m4 = "M4"
    m5 = "M5"
    for oneAns in ans:
        if oneAns == "C[1,5]":  # 最外层的括号，不需要加
            continue
        start, end = oneAns.replace("C[", "").replace("]", "").split(",")  # start的加在左边，end的加在右边
        if start == "1":
            m1 = "(" + m1
        if start == "2":
            m2 = "(" + m2
        if start == "3":
            m3 = "(" + m3
        if start == "4":
            m4 = "(" + m4
        if start == "5":
            m5 = "(" + m5
        if end == "1":
            m1 = m1 + ")"
        if end == "2":
            m2 = m2 + ")"
        if end == "3":
            m3 = m3 + ")"
        if end == "4":
            m4 = m4 + ")"
        if end == "5":
            m5 = m5 + ")"
    # 去除自身的括号
    m1 = m1.replace("(M1)", "M1")
    m2 = m2.replace("(M2)", "M2")
    m3 = m3.replace("(M3)", "M3")
    m4 = m4.replace("(M4)", "M4")
    m5 = m5.replace("(M5)", "M5")
    # 去除自身的括号
    print(m1, m2, m3, m4, m5)


r = [2, 3, 6, 4, 2, 7]
n = len(r)
c = []
kline = [[] for i in range(3)]
for i in range(n):
    c.append(np.zeros(n))
c = np.array(c)
for d in range(1, n):
    for i in range(1, n - d):
        j = i + d
        c[i][j] = 99999
        for k in range(1 + i, j + 1):
            if c[i][k - 1] + c[k][j] + r[i - 1] * r[k - 1] * r[j] < c[i][j]:
                flag = k
            c[i][j] = np.min([c[i][j], c[i][k - 1] + c[k][j] + r[i - 1] * r[k - 1] * r[j]])
        kline[2].append(flag)
        kline[1].append(j)
        kline[0].append(i)
matDir = {}
for i in range(len(kline[0])):
    m = r[kline[0][i] - 1] * r[kline[2][i] - 1] * r[kline[1][i]]
    matDir["C[%d,%d]" % (kline[0][i], kline[1][i])] = ["C[%d,%d]" % (kline[0][i], (kline[2][i] - 1)),
                                                       "C[%d,%d]" % (kline[2][i], kline[1][i])]
getAns(matDir=matDir, toBeFind="C[1,5]")
print(c)
print("C[1,5]: ", c[1][n - 1])
handleAns()
