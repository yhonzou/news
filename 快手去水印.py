#!python2
#coding:utf-8
#2020-4-13@honzou
import requests
from bs4 import BeautifulSoup
import re,clipboard,urllib

#  忽略警告代码
requests.packages.urllib3.disable_warnings()

def GetRealUrl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.get(url, headers=headers, allow_redirects=False,verify=False)
    share_url = response.headers['Location']
    # print(share_url)

    share_response = requests.get(share_url,headers=headers,verify=False).text
    #print(share_response)
    
    url_re = re.compile('(https:\/\/txmov2\.a\.yximgs\.com\/upic\/.*?\.mp4)&#34\;\}')
    
    urls = url_re.search(share_response)
    #print(urls)
    noWaterMarkVideo = urls.group(1)
    #print(noWaterMarkVideo)
    
    tite_re = re.compile('https://f.kuaishou.com/(\w+)')
    #print(tite_re)
    tites = tite_re.search(url)
    #print(tites)
    tite = tites.group(1)
    #print(tite)
    urllib.urlretrieve(noWaterMarkVideo,tite+".mp4")
    print('*' * 84)
    print('\t\t\t\t快手无水印下载')
    print('\t\t\t\t作者:honzou')
    print('*' * 84)
    print('视频('+tite+'.mp4)已下载完成')




if __name__ == '__main__':
    urls = clipboard.get()
    url1 = re.compile('(http.*)')
    url2 = url1.search(urls)
    url = url2.group(1)
    GetRealUrl(url)
    
    #测试Url('https://f.kuaishou.com/2ZNauR')