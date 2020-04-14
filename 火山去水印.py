#!python2
#coding:utf-8
#2020-4-13@honzou
import requests,re,clipboard,urllib
#  忽略警告代码
requests.packages.urllib3.disable_warnings()

# 获取字符串中指定字符
def getMidString(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end]

def getRealUrl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }

# 重定向地址
    response = requests.get(url, headers=headers, allow_redirects=False,verify=False)

    item_id = getMidString(response.headers["Location"], 'item_id=', '&tag=')

    api_url = 'https://share.huoshan.com/api/item/info?item_id=' + item_id

    api_response = requests.get(api_url,headers=headers,verify=False).json()

    waterMarkVideo = api_response['data']['item_info']['url']

    # 替换reflow为resource mark=2为mark=0
    noWaterMarkVideo = waterMarkVideo.replace('reflow','source').replace('mark=2','mark=0')

    #print(noWaterMarkVideo)

    tite_re = re.compile('item_id=(\w+)')
    #print(tite_re)
    tites = tite_re.search(noWaterMarkVideo)
    #print(tites)
    tite = tites.group(1)
    #print(tite)
    urllib.urlretrieve(noWaterMarkVideo,tite+".mp4")
    print('*' * 84)
    print('\t\t\t\t火山无水印下载')
    print('\t\t\t\t作者:honzou')
    print('*' * 84)
    print('视频('+tite+'.mp4)已下载完成')



if __name__ == '__main__':
	  urls = clipboard.get()
	  url1 = re.compile('(http.*)')
	  url2 = url1.search(urls)
	  url = url2.group(1)
	  getRealUrl(url)
    #测试urls=https://share.huoshan.com/hotsoon/s/yvCRrUngm78
