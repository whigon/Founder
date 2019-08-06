# -*- coding: utf-8 -*-
import os
import re
import requests

# 获取当前目录下所有TXT格式的文件
def eachFile():
    files = []
    pathFiles = os.listdir('./Main/')

    for eachfile in pathFiles:
        # 把TXT格式的文件加入到列表里
        if eachfile[-4:] == '.txt':
	    eachfile = 'Main/' + eachfile
            files.append(os.path.join(os.getcwd(),eachfile))

    return files


def checkIMForm(files):
    for file in files:
        with open(file, 'r') as read_file:
            while 1:
                line = read_file.readline()

                if not line:
                    break

                # IM:\n 这里的 \n 去不掉？ 迷
                # 获取IM字段的链接，并尝试连接
                if line[:3] == 'IM:' and len(line) > 5:
                    # 可以考虑用正则解决一下
                    # urls = line.split('http:')
                    # print(line)

                    # 去掉前面的“IM:”和尾巴的“\n”
                    line = line[3:-1]
                    urls = re.split(r';', line)

                    code_200 = 0
                    code_400 = 0
                    code_404 = 0
                    code_502 = 0
                    print(urls)
                    for url in urls:
                        header = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
			    "Connection": "close" 
			}

                        # 发起请求，获取状态码
                        try:
                            resp = requests.get(url=url, timeout=2.0, headers=header)

                        except requests.exceptions.ConnectTimeout:
                            print("Connection timeout: " + url)
			except requests.exceptions.ReadTimeout:
                            print("Read timeout: " + url)
                        else:
                            code = resp.status_code

                            if code == 200:
                                code_200 += 1
                                print("200: " + url)
                            elif code == 400:
                                code_400 += 1
                                # 没配置header？？？
                                print("400: " + url)
                            elif code == 404:
                                code_404 += 1
                                print("404: " + url)
                            elif code == 502:
                                code_502 += 1
                                print("502: " + url)
                            else:
                                print(str(code) + ": " + url)


if __name__ == '__main__':
    file = eachFile()
    checkIMForm(file)
