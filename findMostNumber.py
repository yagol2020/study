"""
算法：寻找最多元素
"""
import math


def candidate(m) -> int:
    """
    选出可能的多数元素
    :param m:
    :return:
    """
    j = m
    c = input_list[m]
    count = 1
    while j < n and count > 0:
        j += 1
        if input_list[j] == c:
            count += 1
        else:
            count -= 1
    if j == n:
        return c
    else:
        return candidate(j + 1)
    pass


input_list = [None]
for input_number in input().split():
    input_list.append(input_number)
n = len(input_list) - 1
c = candidate(1)
count = 0
for j in range(1, n, 1):
    if input_list[j] == c:
        count += 1
if count > math.floor(n / 2):
    print("majority number: ", c)
else:
    print("None majority number")
