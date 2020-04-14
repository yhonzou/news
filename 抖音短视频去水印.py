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


    api_url = 'http://gxqu.top/douyin/ajax.php?act=dy&url=' + url

    api_response = requests.get(api_url,headers=headers,verify=False).json()
    #print(api_response)
    urls = api_response['url']
    #print(urls)
    
    tite = api_response['name']

    
    
    #print(tite)
    urllib.urlretrieve(urls,tite+".mp4")
    print('*' * 84)
    print('\t\t\t\t抖音无水印下载')
    print('\t\t\t\t作者:honzou')
    print('*' * 84)
    print('视频('+tite+'.mp4)已下载完成')



if __name__ == '__main__':
	  urls = clipboard.get()
	  url1 = re.compile('(http.*)')
	  url2 = url1.search(urls)
	  url = url2.group(1)
	  getRealUrl(url)
    #测试urls=真实故事真励志！ #宅家dou剧场 https://v.douyin.com/3rUc81/ 复制此链接，打开【抖音短视频】，直接观看视频！
