def StatementCover(JudgeCoverNode):
    f = open(".//data//coverageCriteria//1_statement.txt")
    lines = f.readlines()
    for line in lines:
        data = line.split(",")
        x = int(data[0])
        y = int(data[1])
        z = int(data[2])
        if x > 0 or y > 10:  # 判定1为真
            JudgeCoverNode.append("J1T")
            z -= 1
        else:
            JudgeCoverNode.append("J1F")
            z += 1
        if x < 0 and z > 3:  # 判定2为真
            JudgeCoverNode.append("J2T")
        else:
            JudgeCoverNode.append("J2F")
    JudgeCoverNode = sorted(set(JudgeCoverNode))
    return JudgeCoverNode


def JudgeCover(JudgeCoverNode):
    f = open(".//data//coverageCriteria//2_judge.txt")
    lines = f.readlines()
    for line in lines:
        data = line.split(",")
        x = int(data[0])
        y = int(data[1])
        z = int(data[2])
        if x > 0 or y > 10:  # 判定1为真
            JudgeCoverNode.append("J1T")
            z -= 1
        else:
            JudgeCoverNode.append("J1F")
            z += 1
        if x < 0 and z > 3:  # 判定2为真
            JudgeCoverNode.append("J2T")
        else:
            JudgeCoverNode.append("J2F")
    JudgeCoverNode = sorted(set(JudgeCoverNode))
    return JudgeCoverNode


def ConditionCover(ConditionCoverNode):
    f = open(".//data//coverageCriteria//3_condition.txt")
    lines = f.readlines()
    for line in lines:
        data = line.split(",")
        x = int(data[0])
        y = int(data[1])
        z = int(data[2])
        if x > 0:
            ConditionCoverNode.append("C1T")
        else:
            ConditionCoverNode.append("C1F")
        if y > 10:
            ConditionCoverNode.append("C2T")
        else:
            ConditionCoverNode.append("C2F")

        if x > 0 or y > 10:  # 判定1为真
            z -= 1
        else:
            z += 1

        if x < 0:
            ConditionCoverNode.append("C3T")
        else:
            ConditionCoverNode.append("C3F")
        if z > 3:
            ConditionCoverNode.append("C4T")
        else:
            ConditionCoverNode.append("C4F")
    ConditionCoverNode = sorted(set(ConditionCoverNode))
    return ConditionCoverNode


def JudgeConditionCover(JudgeConditionCoverNode):
    f = open(".//data//coverageCriteria//4_judgecondition.txt")
    lines = f.readlines()
    for line in lines:
        data = line.split(",")
        x = int(data[0])
        y = int(data[1])
        z = int(data[2])

        # 判定部分
        if x > 0 or y > 10:  # 判定1为真
            JudgeConditionCoverNode.append("J1T")
            z -= 1
        else:
            JudgeConditionCoverNode.append("J1F")
            z += 1
        if x < 0 and z > 3:  # 判定2为真
            JudgeConditionCoverNode.append("J2T")
        else:
            JudgeConditionCoverNode.append("J2F")

        # 条件部分
        if x > 0:
            JudgeConditionCoverNode.append("C1T")
        else:
            JudgeConditionCoverNode.append("C1F")
        if y > 10:
            JudgeConditionCoverNode.append("C2T")
        else:
            JudgeConditionCoverNode.append("C2F")
        if x < 0:
            JudgeConditionCoverNode.append("C3T")
        else:
            JudgeConditionCoverNode.append("C3F")
        if z > 3:
            JudgeConditionCoverNode.append("C4T")
        else:
            JudgeConditionCoverNode.append("C4F")
    JudgeConditionCoverNode = sorted(set(JudgeConditionCoverNode))
    return JudgeConditionCoverNode


def ConditionCombineCover(ConditionCombineCoverNode):
    # 判定1,2各有TT,TF,FT,FF
    f = open(".//data//coverageCriteria//5_conditioncombine.txt")
    lines = f.readlines()
    for line in lines:
        data = line.split(",")
        x = int(data[0])
        y = int(data[1])
        z = int(data[2])
        if x > 0:
            C1 = "T"
        else:
            C1 = "F"
        if y > 10:
            C2 = "T"
        else:
            C2 = "F"

        if x > 0 or y > 10:  # 判定1为真
            z -= 1
        else:
            z += 1

        if x < 0:
            C3 = "T"
        else:
            C3 = "F"
        if z > 3:
            C4 = "T"
        else:
            C4 = "F"
        ConditionCombineCoverNode.append("12" + C1 + C2)
        ConditionCombineCoverNode.append("34" + C3 + C4)
    ConditionCombineCoverNode = sorted(set(ConditionCombineCoverNode))
    return ConditionCombineCoverNode


if __name__ == "__main__":
    StatementCoverNode = []  # 本题比较特殊，满足判定覆盖则满足语句覆盖
    JudgeCoverNode = []  # 学生编写的测试用例是否覆盖了全部判定的真假各取一次，总共有两个判定结点，因此有2*2=4个结果
    ConditionCoverNode = []  # 学生编写的测试用例是否覆盖了全部条件的真假各取一次，总共有4个条件，因此有4*2=8个结果
    JudgeConditionCoverNode = []  # 学生编写的测试用例是否满足条件的真假各取一次和判定的真假各取一次，因此如果是12个结果就是对的
    ConditionCombineCoverNode = []  # 学生编写的测试用例是否满足条件的真假组合各有一次，本体有4个判定，
    # 每个判定的里有两个条件，因此有2*2+2*2=8个结果

    score = 0

    # 在同目录下放5个txt文件，txt文件名字区分大小写，内容是x,y,z，并且之间用英文逗号隔开

    # 1_statement.txt是语句覆盖的测试用例
    # 2_judge.txt是判定覆盖的测试用例
    # 3_condition.txt是条件覆盖的测试用例
    # 4_judgecondition.txt是判定条件覆盖的测试用例
    # 5_conditioncombine.txt是条件组合覆盖的测试用例

    StatementCoverNode = StatementCover(StatementCoverNode)  # 长度为4则正确
    score += 20 * len(StatementCoverNode) / 4
    JudgeCoverNode = JudgeCover(JudgeCoverNode)  # 长度为4则正确
    score += 20 * len(JudgeCoverNode) / 4
    ConditionCoverNode = ConditionCover(ConditionCoverNode)  # 长度为8则正确
    score += 20 * len(ConditionCoverNode) / 8
    JudgeConditionCoverNode = JudgeConditionCover(JudgeConditionCoverNode)  # 长度为12则正确
    score += 20 * len(JudgeConditionCoverNode) / 12
    ConditionCombineCoverNode = ConditionCombineCover(ConditionCombineCoverNode)  # 长度为8则正确
    score += 20 * len(ConditionCombineCoverNode) / 8

    print("语句覆盖结果:", StatementCoverNode, "\n长度为", len(StatementCoverNode))
    print("判定覆盖结果:", JudgeCoverNode, "\n长度为", len(JudgeCoverNode))
    print("条件覆盖结果:", ConditionCoverNode, "\n长度为", len(ConditionCoverNode))
    print("判定条件覆盖结果:", JudgeConditionCoverNode, "\n长度为", len(JudgeConditionCoverNode))
    print("条件组合覆盖结果:", ConditionCombineCoverNode, "\n长度为", len(ConditionCombineCoverNode))
    print("\n建议得分%d\n" % (score))
