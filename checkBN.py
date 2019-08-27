# -*- coding: utf-8 -*-
"""
检查Readme里的频道是否都采集到了，
没采集到的可能是被查重了，需要查看采集日志

Created on Wed Aug 21 14:58:26 2019
@author: LiYuexiang
"""

import os


# 获取当前目录下所有TXT格式的文件
def eachFile():
    files = []
    pathFiles = os.listdir('.')

    for eachfile in pathFiles:
        # 把TXT格式的文件加入到列表里
        if eachfile[-4:] == '.txt':
            files.append(os.path.join(os.getcwd(), eachfile))

    return files


def getChannel():
    channels = []

    # Readme的相对路径
    path = './../apps/'
    path = os.path.join(path, os.listdir(path)[0])
    file = ''

    if os.path.isfile(os.path.join(path, 'readme.txt')):
        file = os.path.join(path, 'readme.txt')
        print(1)
    elif os.path.isfile(os.path.join(path, 'Readme.txt')):
        file = os.path.join(path, 'Readme.txt')
        print(2)
    else:
        print(os.path.join(path, 'readme.txt'))
        print("No readme!")

    with open(file, 'r', encoding='UTF-8') as read_file:
        flag = 0

        while 1:
            line = read_file.readline()

            if not line:
                break

            line = line.strip()

            if line == '频道：':
                flag = 1
            elif line == '分页：':
                flag = 0

            if flag == 1:
                channels.append(line)

        channels.pop(0)
        channels.pop(-1)

    return channels


def getCollectChannel():
    channels = []

    os.system("cat ./Main/* | grep 'BN:' | sort | uniq > channel.txt")

    print("Collection data: ")
    with open('channel.txt', 'r', encoding='UTF-8') as read_file:
        while 1:
            line = read_file.readline()

            if not line:
                break

            line = line.strip()
            line = line[3:]
            print(line)
            channels.append(line)

    print("----------------")
    return channels


if __name__ == '__main__':
    # file = eachFile()
    # 获取Readme中的频道名称
    channels = set(getChannel())
    collectChannels = set(getCollectChannel())

    print("Different data: ")
    # 找出不同的元素
    diff = channels & collectChannels

    for d in diff:
        print(d)
