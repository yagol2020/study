graph = [[0, 1, 0, 0, 0, 1, 1],
         [1, 0, 1, 0, 0, 0, 1],
         [0, 1, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 0],
         [1, 0, 0, 1, 1, 0, 1],
         [1, 1, 1, 0, 0, 1, 0]]  # 邻接矩阵
c = [0 for i in range(len(graph))]  # 解


def check_legal(node_set, node_color, i, color):
    for j in range(i):
        if node_set[i][j] == 1 and node_color[j] == color:
            return True
    return False


def graphcolor(k):
    if k == len(graph):
        print(c)
    else:
        for color in range(1, 4):
            c[k] = color
            if not check_legal(graph, c, k, color):
                graphcolor(k + 1)


if __name__ == "__main__":
    graphcolor(0)
