#!/usr/bin/env
# coding:utf-8
"""
Author = miker
Created on 2017/2/13 18:10
Description:

"""

import sys
import urllib2
import json

reload(sys)
sys.setdefaultencoding('utf-8')

# 设置Headers
headers = {"content-type": "application/json"}

# 入参
pa = {"orgcode": "20011O"}
Data = json.dumps(pa)

# url
url = "http://172.22.3.231:8000/lineTemplate/search"

req = urllib2.Request(url)
req.add_header("content-type", "application/json")
response = urllib2.urlopen(req, data=Data)
print response.read()
