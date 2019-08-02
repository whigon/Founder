# -*- coding: utf-8 -*-

import Check
import CheckSN
import CheckBN
import os

path = "C:\\Users\\admin\\Desktop\\L-whigon\\L-相关文档\\APP测试\\采集数据"
fileName = ''
SN = ''


# 测试目标文件
def test(filePath):
    sel = -1
    print('1. 检查站点名')
    print('2. 检查频道采集数目')

    try:
        sel = eval(input('输入检测序号：'))
    except (SyntaxError, NameError):
        return 0

    if sel == 1:
        SN = input('SN: ')
        # 记录有多少的数据条目
        countSN = Check.check(filePath, sel, SN)

        # # 打开文件
        # with open(filePath, 'r', encoding='UTF-8') as read_file:
        #     # 记录行数
        #     lineCount = 0
        #
        #     while 1:
        #         line = read_file.readline()
        #
        #         # 文件结束
        #         if not line:
        #             break
        #
        #         lineCount += 1
        #
        #         # 去掉换行符 和 回车
        #         line = line.replace("\n", "")
        #         line = line.replace("\r", "")
        #
        #         # 检查站点名
        #         if line[:3] == 'SN:':
        #             bool = CheckSN.check(line, SN)
        #             print(bool)
        #             # 检查返回值
        #             if bool:
        #                 countSN += 1
        #                 pass
        #             else:
        #                 print('Line ' + str(lineCount) + ': SN error')

        # 输出数据条目总数

        print('正确抓取站点名数: ' + str(countSN))
    elif sel == 2:
        BN = input('BN:')
        #记录频道名出现的次数
        countBN = Check.check(filePath,sel, BN=BN)

        # with open(filePath, 'r', encoding='UTF-8') as read_file:
        #     # 记录行数
        #     lineCount = 0
        #
        #     while 1:
        #         line = read_file.readline()
        #
        #         # 文件结束
        #         if not line:
        #             break
        #
        #         lineCount += 1
        #
        #         # 去掉换行符 和 回车
        #         line = line.replace("\n", "")
        #         line = line.replace("\r", "")
        #
        #         # 检查站点名
        #         if line[:3] == 'BN:':
        #             val = CheckBN.check(line, BN)
        #             # 检查返回值
        #             if val == 0:
        #                 print('Line ' + str(lineCount) + ': BN miss')
        #             elif val == 1:
        #                 countBN += 1
        #                 pass
        #             else:
        #                 print('Line ' + str(lineCount) + ': BN error')
        print(countBN)

def main():
    # 输入文件名
    fileName = input("Filename: ")
    fileName += ".txt"

    # 路径拼接
    filePath = os.path.join(path, fileName)

    filePath = 'C:\\Users\\admin\\Desktop\\L-whigon\\L-相关文档\\APP测试\\采集数据\\20190705110907.txt'
    # 检查文件是否存在
    if os.path.exists(filePath):
        with open(filePath, 'r', encoding='UTF-8') as read_file:
            # 记录行数
            lineCount = 0
            # 记录有多少的数据条目
            countSN = 0

            while 1:
                line = read_file.readline()

                if not line:
                    break
                lineCount += 1
                if line[:3] == 'SN:':
                    countSN += 1

            print('总行数：' + str(lineCount))
            print('SN字段数量: ' + str(countSN))
        print("-----------Test-----------")
        test(filePath)
    else:
        print("-----------No such file-----------")
        exit(-1)


if __name__ == "__main__":
    main()
