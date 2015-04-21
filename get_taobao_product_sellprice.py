# python3
import urllib.request
import re

#pid = 37982506938 

def get1(pid):
    url = r'http://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=false&callback=setMdskip&itemId=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "mdskip.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.12.UpuePQ&is_b=1&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    price = re.findall(r'"price":"([\d\.]{4,})"', scode)
    print(
          '原价:',
          price[0],
          '促销价:',
          price[1]
          )

def get_taobao_product_sellprice(pid):
    url = r'http://detailskip.taobao.com/json/sib.htm?p=1&itemId=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "detailskip.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://item.taobao.com/item.htm?p=1&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    price = re.findall(r'(?:price\W*)(\d*\.\d*)', scode)
    print(
           '原价:', ###原价不是从这里获取的，淘宝和天猫这里还是有区别的，淘宝完全可以从原始页面获取。
           price[1],
           '促销价:',
           price[0] 
           )

if __name__ == '__main__':
    pid = input("please input the website:")
    get_taobao_product_sellprice(pid)
