"""
软件测试作业，读取C文件，输出关键字，函数名和指定函数的圈复杂度
"""
from itertools import chain

KEY_WORDS = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else",
             "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return",
             "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned",
             "void", "volatile", "while"]

c_file = open("./data/software testing homework/program2.c", "r")
c_file_content_each_line = []
c_has_keywords = []
for line in c_file:
    line_list = line.split(" ")  # 用空格分割
    line_list = [each_word.split("(") for each_word in line_list]  # 用(分割
    line_list = list(chain.from_iterable(line_list))  # 将高维list降维到1维
    line_list = [each_word.split(")") for each_word in line_list]  # 用)分割
    line_list = list(chain.from_iterable(line_list))
    line_list = [each_word.replace("\n", "") for each_word in line_list]  # 删去多余的\n
    line_list = [each_word.replace("\t", "") for each_word in line_list]  # 删去多余的\t
    c_file_content_each_line.append(line_list)
    for each_word in line_list:
        if each_word in KEY_WORDS:
            c_has_keywords.append(each_word)

c_has_keywords = list(set(c_has_keywords))
print(c_has_keywords)
