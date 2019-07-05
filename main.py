# -*- coding: utf-8 -*-

import checkSN
import os

path = "C:\\Users\\admin\\Desktop\\L-whigon\\L-相关文档\\APP测试\\采集数据"
fileName = ''
SN = ''


# 测试目标文件
def test(filePath):
    # 打开文件
    with open(filePath, 'r', encoding='UTF-8') as read_file:
        # lines = []
        # 记录行数
        lineCount = 0
        # 记录有多少的数据条目
        countSN = 0

        while 1:
            line = read_file.readline()
            lineCount += 1

            # 文件结束
            if not line:
                break

            # 去掉换行符 和 回车
            line = line.replace("\n", "")
            line = line.replace("\r", "")

            # 检查站点名
            if line[:3] == 'SN:':
                countSN += 1
                bool = checkSN.check(line, SN)
                print(bool)
                # 检查返回值
                if bool:
                    pass
                else:
                    print('Line ' + str(lineCount) + ': SN error')

        # 输出数据条目总数
        print(SN + ': ' + str(countSN))


def main():
    # 输入文件名
    fileName = input("Filename: ")
    SN = input("SN: ")
    fileName += ".txt"

    # 路径拼接
    filePath = os.path.join(path, fileName)

    # 检查文件是否存在
    if os.path.exists(filePath):
        print("-----------Test-----------")
        test(filePath)
    else:
        print("No file")
        exit(-1)


if __name__ == "__main__":
    main()
