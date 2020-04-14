#!python2
#coding:utf-8
#2020-4-13@honzou

from bs4 import BeautifulSoup
import re,clipboard,urllib
import requests,re
import json

def get_video_src(vid):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    }

    api_url = 'http://vv.video.qq.com/getinfo?vids=' + vid + '&platform=101001&charge=0&otype=json&defn=shd'

    html = requests.get(api_url, headers=headers).text

    # 获取json数据
    p = re.compile(r'({.*})', re.S)
    jsonstr = re.findall(p, html)[0]
    json_data = json.loads(jsonstr)

    # 解析json数据获取url
    baseurl = json_data['vl']['vi'][0]['ul']['ui'][0]['url']
    fn = json_data['vl']['vi'][0]['fn']
    fvkey = json_data['vl']['vi'][0]['fvkey']

    real_url = baseurl + fn + '?vkey=' + fvkey

    #print('无水印链接:'+real_url)
    
    urllib.urlretrieve(real_url,url+".mp4")
    print('*' * 84)
    print('\t\t\t腾讯视频热点无水印下载')
    print('\t\t\t\t作者:honzou')
    print('*' * 84)
    print('视频('+url+'.mp4)已下载完成')

if __name__ == '__main__':
    urls = clipboard.get()
    url1 = re.compile('http.*vid=(.*?)&')
    url2 = url1.search(urls)
    url = url2.group(1)
    #print(url)
    get_video_src(url)
    
    #http://m.v.qq.com/play/play.html?vid=u303399llia&url_from=share&second_share=0&share_from=copy
    #http://m.v.qq.com/play/play.html?vid=j09354cwuky&url_from=share&second_share=0&share_from=copy