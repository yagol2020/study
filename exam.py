def JudgeCover():
    JudgeCoverNode = []
    f = open("data/exam/1_judge.txt")
    lines = f.readlines()
    count = 1
    branch = []
    for line in lines:
        branch.clear()
        data = line.split(",")
        w = int(data[0])
        x = int(data[1])
        y = int(data[2])
        z = int(data[3])
        print("%d,%d,%d,%d" % (w, x, y, z))
        if w > 0 or x > 10:  # 判定1为真
            JudgeCoverNode.append("J1T")
            branch.append("b")
            w -= 1
        else:
            JudgeCoverNode.append("J1F")
            branch.append("c")
            x += 1
        if y > 5 and z > 3:  # 判定2为真
            JudgeCoverNode.append("J2T")
            branch.append("d")
            y -= 1
        else:
            JudgeCoverNode.append("J2F")
            branch.append("e")
            z += 1
        print("\033[0;32m测试用例", count, "\033[0m覆盖到了", branch)
        count += 1
        print("Sum:", w + x + y + z)
    JudgeCoverNode = sorted(set(JudgeCoverNode))
    if len(JudgeCoverNode) == 4:
        print("满足判定覆盖.")
    else:
        print("\033[0;31m不满足判定覆盖,\033[0m应当减%d分." % (4 - len(JudgeCoverNode)))
    print("JudgeCover:", JudgeCoverNode)


def ConditionCover():
    ConditionCoverNode = []
    result = []
    count = 1
    f = open("data/exam/2_condition.txt")
    lines = f.readlines()
    for line in lines:
        ConditionCoverNode.clear()
        data = line.split(",")
        w = int(data[0])
        x = int(data[1])
        y = int(data[2])
        z = int(data[3])
        print("\033[0;32m测试用例%d\033[0m: %d,%d,%d,%d" % (count, w, x, y, z))
        if w > 0:
            ConditionCoverNode.append("C1T")
        else:
            ConditionCoverNode.append("C1F")
        if x > 10:
            ConditionCoverNode.append("C2T")
        else:
            ConditionCoverNode.append("C2F")

        if w > 0 or x > 10:  # 判定1为真
            w -= 1
        else:
            x += 1

        if y > 5:
            ConditionCoverNode.append("C3T")
        else:
            ConditionCoverNode.append("C3F")
        if z > 3:
            ConditionCoverNode.append("C4T")
        else:
            ConditionCoverNode.append("C4F")
        if y > 5 and z > 3:  # 判定2为真
            y -= 1
        else:
            z += 1
        print("Sum:", w + x + y + z)
        ConditionCoverNode = sorted(set(ConditionCoverNode))
        print(ConditionCoverNode)
        count += 1
        result.extend(ConditionCoverNode)
    result = sorted(set(result))
    if len(result) == 8:
        print("满足条件覆盖.")
    else:
        print("\033[0;31m不满足条件覆盖，\033[0m应当减%d分." % (8 - len(result)))
    print(result)


def ConditionCombineCover():
    # 判定1,2各有TT,TF,FT,FF
    ConditionCombineCoverNode = []
    result = []
    count = 1
    f = open("data/exam/3_conditioncombine.txt")
    lines = f.readlines()
    for line in lines:
        ConditionCombineCoverNode.clear()
        data = line.split(",")
        w = int(data[0])
        x = int(data[1])
        y = int(data[2])
        z = int(data[3])
        print("\033[0;32m测试用例%d\033[0m: %d,%d,%d,%d" % (count, w, x, y, z))
        if w > 0:
            C1 = "T"
        else:
            C1 = "F"
        if x > 10:
            C2 = "T"
        else:
            C2 = "F"

        if w > 0 or x > 10:  # 判定1为真
            w -= 1
        else:
            x += 1

        if y > 5:
            C3 = "T"
        else:
            C3 = "F"
        if z > 3:
            C4 = "T"
        else:
            C4 = "F"
        if y > 5 and z > 3:
            y -= 1
        else:
            z += 1
        ConditionCombineCoverNode.append("1" + C1 + "2" + C2)
        ConditionCombineCoverNode.append("3" + C3 + "4" + C4)
        result.append("1" + C1 + "2" + C2)
        result.append("3" + C3 + "4" + C4)
        ConditionCombineCoverNode = sorted(set(ConditionCombineCoverNode))
        print("Sum:", w + x + y + z)
        print(ConditionCombineCoverNode)
        count += 1
    result = sorted(set(result))
    if len(result) == 8:
        print("满足条件组合覆盖.")
    else:
        print("\033[0;31m不满足条件组合覆盖，\033[0m应当减%d分." % (8 - len(result)))
    print(result)


if __name__ == "__main__":
    print("判定覆盖:")
    JudgeCover()
    print("\n条件覆盖:")
    ConditionCover()
    print("\n条件组合覆盖:")
    ConditionCombineCover()
