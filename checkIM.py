# -*- coding: utf-8 -*-
"""
检查IM字段里的url的格式是否正确以及此链接是否有效

Created on Thur Aug 1 16:26:39 2019
@author: LiYuexiang
"""

import os
import re
import requests
import validators


# 获取当前目录下所有TXT格式的文件
def eachFile():
    files = []
    pathFiles = os.listdir('.')

    for eachfile in pathFiles:
        # 把TXT格式的文件加入到列表里
        if eachfile[-4:] == '.txt':
            files.append(os.path.join(os.getcwd(), eachfile))

    return files


def checkIMValidation(files):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Connection": "close"
    }

    code_200 = 0
    code_400 = 0
    code_404 = 0
    code_502 = 0
    code_504 = 0
    other_code = 0
    connection_fail = 0
    read_fail = 0
    invalid_schema = 0
    other_err = 0
    total = 0

    for file in files:
        with open(file, 'r', encoding='UTF-8') as read_file:
            while 1:
                line = read_file.readline()

                if not line:
                    break

                # 获取非空的IM字段
                if line[:3] == 'IM:' and len(line) > 5:

                    # 去掉前面的“IM:”和结尾的“\n”
                    line = line.strip()[3:]
                    # line = line[3:-1]
                    urls = re.split(r';', line)

                    '''
                    # 正则切分后要重新拼接
                    # urls = re.split(r'(https?://）', line)
                    print(urls)
                    '''

                    for url in urls:
                        total += 1

                        # 发起请求，获取状态码
                        try:
                            # It’s a good practice to set connect timeouts to slightly larger than a multiple of 3,
                            # which is the default TCP packet retransmission window.
                            resp = requests.get(url=url, timeout=(3.05, 1), headers=header)
                        except requests.exceptions.ConnectTimeout:
                            connection_fail += 1
                            print("Connection timeout: " + url)
                        except requests.exceptions.ReadTimeout:
                            read_fail += 1
                            print("Read timeout: " + url)
                        except requests.exceptions.InvalidSchema:
                            invalid_schema += 1
                            print("Invalid schema: " + url)
                        except Exception as err:
                            print(str(err) + ": " + url)
                            other_err += 1
                        else:
                            code = resp.status_code

                            if code == 200:
                                code_200 += 1
                                # print("200: " + url)
                            elif code == 400:
                                code_400 += 1
                                print("400: " + url)
                            elif code == 404:
                                code_404 += 1
                                print("404: " + url)
                            elif code == 502:
                                code_502 += 1
                                print("502: " + url)
                            elif code == 504:
                                code_504 += 1
                                print("504: " + url)
                            else:
                                other_code += 1
                                print(str(code) + ": " + url)

                        if total % 100 == 0:
                            print("#urls: " + str(total))

    print("----------------------")
    print("#200: " + str(code_200))
    print("#400: " + str(code_400))
    print("#404: " + str(code_404))
    print("#502: " + str(code_502))
    print("#504: " + str(code_504))
    print("#other code: " + str(other_code))
    print("#connection fail: " + str(connection_fail))
    print("#read fail: " + str(read_fail))
    print("#invalid schema: " + str(invalid_schema))
    print("#other error: " + str(other_err))
    print("total: " + str(total))


def checkIMForm(files):
    for file in files:
        with open(file, 'r', encoding='UTF-8') as read_file:
            while 1:
                line = read_file.readline()

                if not line:
                    break

                # 先拆分成单个的链接，对于每个链接用正则表达校验是否是一个有效的链接
                if line[:3] == 'IM:' and len(line) > 5:

                    # 去掉前面的“IM:”和尾巴的“\n”
                    line = line.strip()[3:]

                    urls = re.split(r';', line)

                    for url in urls:
                        # 检查是否是http(s)开头
                        if re.match(r'https?://[\d\w\:\/\.\?=&_\-]*', url) is None:
                            print("Incorrect Form: " + str(url))

                        # 检查url是否是个有效链接
                        if not validators.url(str(url)):
                            print(str(url) + " is an invalid url")


if __name__ == '__main__':
    file = eachFile()
    # 检查链接的格式
    checkIMForm(file)
    # 检查链接是否有效
    checkIMValidation(file)
