# -*- coding: utf8 -*-
import json
import requests
def main_handler(event, context):
    content = ''
    s = requests.session()
    token = '你的token'
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': 'token {}'.format(token)}
    put_urls = ['https://api.github.com/repos/你的用户名/你的项目1/actions/workflows/你的.yml文件名/enable',
                'https://api.github.com/repos/你的用户名/你的项目2/actions/workflows/你的.yml文件名/enable']
    for url in put_urls:
        res = s.put(url, headers=headers)
        content += str(res.content, encoding='utf-8')
    return(content)
