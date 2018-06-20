#coding:utf-8
#!python2
import urllib2,urllib
import requests
import re,clipboard

#    @ honzou
#    2018/6/21


urls = clipboard.get()
url1 = re.compile('(http.*)')
url2 = url1.search(urls)
url = url2.group(1)
#print(url)
req = urllib2.Request(url)
req.add_header('user-agent','Mozilla/5.0')
html = urllib2.urlopen(req)
htm = html.read()



playaddr_re = re.compile('playAddr: "(.*?)",')
playaddr = playaddr_re.search(htm)
playad = playaddr.group(1)
urls = playad.replace('playwm','play')
#print urls


tite_re = re.compile('jpeg" alt="(.*?)"></div><div class="info"><p class="name')
tites = tite_re.search(htm)
tite = tites.group(1)
#print(tite)

urllib.urlretrieve(urls,tite+".mp4")
print('*' * 84)
print('\t\t\t\t抖音无水印下载')
print('\t\t\t\t\t作者:honzou')
print('*' * 84)
print('视频('+tite+'.mp4)已下载完成')