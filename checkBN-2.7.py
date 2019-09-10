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
    file = './readme.txt'

    if not os.path.isfile(file):
        print("No readme!")
        print("----------------")

        return None

    with open('./readme.txt', 'r') as read_file:
        while 1:
            line = read_file.readline()

            if not line:
                break

            line = line.strip()
            channels.append(line)

    channels.sort()
    print("Readme: ")
    for c in channels:
        print(c)
    print("----------------")

    return channels


def getCollectChannel(appName):
    channels = []

    # os.system("cat ./Main/* | grep 'BN:' | sort | uniq > channel.txt")
    command = "cat ./Main/* | grep -A1 'SN:" + appName + "' | grep 'BN:'  | sort | uniq > channel.txt"
    print(command)
    os.system(command)

    with open('channel.txt', 'r') as read_file:
        while 1:
            line = read_file.readline()

            if not line:
                break

            line = line.strip()
            line = line[3:]
            channels.append(line)

    channels.sort()
    print("Collection data: ")
    for c in channels:
        print(c)
    print("----------------")

    return channels


if __name__ == '__main__':
    # file = eachFile()
    appName = raw_input("APP name: ")

    # 获取Readme中的频道名称
    channels = getChannel()
    # 获取采集到的文件中的频道名称
    collectChannels = set(getCollectChannel(appName))

    # 如果readme存在
    if channels is not None:
        channels = set(channels)

        print("Different data: ")
        # 找出不同的元素
        diff = channels ^ collectChannels

        for d in diff:
            print(d)
