import CheckSN
import CheckBN
import os


def check(filePath, sel, SN='', BN=''):
    with open(filePath, 'r', encoding='UTF-8') as read_file:
        # 记录行数
        lineCount = 0
        # 记录检查的项的正确个数
        count = 0
        while 1:
            line = read_file.readline()

            # 文件结束
            if not line:
                break

            lineCount += 1

            # 去掉换行符 和 回车
            line = line.replace("\n", "")
            line = line.replace("\r", "")

            if sel == 1:
                # 检查站点名
                if line[:3] == 'SN:':
                    val = CheckSN.check(line, SN)
                    # 检查返回值
                    if val:
                        count += 1
                        pass
                    else:
                        print('Line ' + str(lineCount) + ': SN error')
            elif sel == 2:
                if line[:3] == 'BN:':
                    val = CheckBN.check(line, BN)
                    # 检查返回值
                    if val == 0:
                        print('Line ' + str(lineCount) + ': BN miss')
                    elif val == 1:
                        count += 1
                        pass
                    else:
                        print('Line ' + str(lineCount) + ': BN error')

        return count
    #首页-新闻  20190705110706
