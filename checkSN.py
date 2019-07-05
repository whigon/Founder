# -*- coding: utf-8 -*-

import os

path = "C:\\Users\\admin\\Desktop\\L-whigon\\L-相关文档\\APP测试\\采集数据"
fileName = ''
SN = ''


# 检查SN
def check(str_SN, SN):
    str = str_SN[3:]

    # 频道为空，频道不是目标频道，频道是目标频道
    if str == SN:
        return True
    else:
        return False
