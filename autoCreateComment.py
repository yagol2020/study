def main():
    file = open(".//data//autoCreateComment//score.txt")
    lines = file.readlines()
    comment = ""
    for line in lines:
        line = line.replace("\t\n", "")
        score = line.split("\t")
        score = [int(onescore) for onescore in score]
        # 数据流图详细程度
        if score[0] >= 0 and score[0] <= 5:
            comment += "实验报告内容不够详细，给出了数据流图、用例图，"
        elif score[0] >= 6 and score[0] <= 8:
            comment += "实验报告内容详细程度一般，给出了数据流图、用例图，"
        else:
            comment += "实验报告内容详细，给出了数据流图、用例图，"
        # 数据流图描述说明
        if score[1] >= 0 and score[1] <= 5:
            comment += "对数据流图、用例图描述不够详细，"
        elif score[1] >= 6 and score[1] <= 8:
            comment += "对数据流图、用例图描述详细程度一般，"
        else:
            comment += "对数据流图、用例图有详细的描述说明，"
        # 实体关系图、类图的详细程度
        if score[2] >= 0 and score[2] <= 5:
            comment += "建立的实体关系图、类图不够合理，"
        elif score[2] >= 6 and score[2] <= 8:
            comment += "建立的实体关系图、类图较为合理，给出了描述"
        else:
            comment += "建立了合理的实体关系图、类图，并给出了详细描述，"
        # 功能层次结构图的详细程度
        if score[3] >= 0 and score[3] <= 5:
            comment += "功能层次结构图不够合理，"
        elif score[3] >= 6 and score[3] <= 8:
            comment += "功能层次结构图较为合理，并给出了描述"
        else:
            comment += "画出了合理的功能层次结构图，并给出了详细的描述，"
        # 模块结构图、类图、包图
        if score[4] >= 0 and score[4] <= 5:
            comment += "画出的模块结构图、类图、包图不够合理，"
        elif score[4] >= 6 and score[4] <= 8:
            comment += "画出了较为合理的模块结构图、类图、包图，"
        else:
            comment += "画出了合理的模块结构图、类图、包图，"
        # 表结构设计
        if score[5] >= 0 and score[5] <= 5:
            comment += "给出的系统数据库设计的表结构不够合理，"
        elif score[5] >= 6 and score[5] <= 8:
            comment += "给出了较为合理的系统数据库设计的表结构，"
        else:
            comment += "给出了合理的系统数据库设计的表结构，"
        # 处理流程图
        if score[6] >= 0 and score[6] <= 5:
            comment += "画出的典型模块详细设计的处理流程图合理程度一般，"
        elif score[6] >= 6 and score[6] <= 8:
            comment += "画出了较为合理的典型模块详细设计的处理流程图，"
        else:
            comment += "画出了合理的典型模块详细设计的处理流程图，"

        #  过程模型
        if score[7] >= 0 and score[7] <= 5:
            comment += "对过程模型没有较为清楚的认识，"
        elif score[7] >= 6 and score[7] <= 8:
            comment += "对过程模型有较为清楚的认识，"
        else:
            comment += "对过程模型有清楚的认识，"

        # 参考文献
        if score[8] >= 0 and score[8] <= 5:
            comment += "给出的参考文献较少，"
        elif score[8] >= 6 and score[8] <= 8:
            comment += "给出了参考文献，但数量一般，"
        else:
            comment += "给出了较多且合理的参考文献，"
        # 系统规模估算
        if score[9] >= 0 and score[9] <= 5:
            comment += "对系统的规模估算不够清楚，"
        elif score[9] >= 6 and score[9] <= 8:
            comment += "对系统的规模有较为清楚的估算，"
        else:
            comment += "对系统的规模估算清楚，"
        # 心得体会
        if score[10] >= 0 and score[10] <= 5:
            comment += "心得体会较少。"
        elif score[10] >= 6 and score[10] <= 8:
            comment += "介绍了较为详细的心得体会。"
        else:
            comment += "介绍了详细的心得体会。"
        sum = 0
        for i in range(8):
            sum += score[i] * 0.2
        sum += score[8] * 0.1
        sum += score[9] * 0.1
        sum += score[10] * 0.2
        comment += "\n" + str(round(sum, 3) * 5) + "分"
        print(comment)


if __name__ == '__main__':
    main()
