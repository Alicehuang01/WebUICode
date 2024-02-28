# -*-coding:Utf-8 -*-
# @File:practice01.py
# @Author:hhl
# @Date:2024/2/25 23:03 
# @Dec:

import time

# 导入第三库
import requests

#1.新建浏览器会话
# 接口请求参数
import requests

data = {
    "capabilities":{
        "browserName":"chrome"
    }
}

# 接口请求地址
url = 'http://127.0.0.1:9515/session'
# 发起请求
res = requests.post(url=url , json=data)
print(res.json())
