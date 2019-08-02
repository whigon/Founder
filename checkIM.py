import os
import re
import requests
import urllib2


# 获取当前目录下所有TXT格式的文件
def eachFile():
    files = []
    pathFiles = os.listdir()

    for eachfile in pathFiles:
        # 把TXT格式的文件加入到列表里
        if eachfile[-4:] == '.txt':
            files.append(os.path.join(os.getcwd(), eachfile))

    return files


def checkIMForm(files):
    for file in files:
        with open(file, 'r', encoding='UTF-8') as read_file:
            while 1:
                line = read_file.readline()

                if not line:
                    break

                '''
                while line[:3] == 'IM:':
                    #url_IM.join(line)
                    url_IM += line
                    print(line)

                    line = read_file.readline()
                    if line[:3] == 'SN:':
                        urls = url_IM.split('http:')
                        # urls.remove(0)
                       # print(urls)
                        break
                '''

                # IM:\n 这里的 \n 去不掉？ 迷
                # 获取IM字段的链接，并尝试连接
                if line[:3] == 'IM:' and len(line) > 5:
                    # 可以考虑用正则解决一下
                    # urls = line.split('http:')
                    # print(line)

                    urls = re.split(r';', line)
                    urls[0] = urls[0][3:]

                    '''
                    # 这里的正则配的不够好
                    # urls = re.split(r'(http)(s)?:', line)
                    if 'https:' in line:
                        urls = re.split(r'(https:)', line)
                        urls.pop(0)
                    if 'http:' in line:
                        urls = re.split(r'(http:)', line)
                        urls.pop(0)
                    '''
                    total = len(urls)
                    code_404 = 0
                    code_400 = 0
                    code_200 = 0
                    for url in urls:
                        pass
                        # print(url)
                        resp = requests.get(url)
                        code = resp.status_code
                        if code == 200:
                            code_200 += 1
                            # print(1)
                        if code == 400:
                            code_400 += 1
                            # 没配置header？？？
                            print("语法错误：" + url)
                        elif code == 404:
                            code_404 += 1


if __name__ == '__main__':
    file = eachFile()
    checkIMForm(file)
