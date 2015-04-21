# python3
import urllib.request
import re

pid = 37982506938 

def get1():
    url = r'http://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=false&callback=setMdskip&itemId=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "mdskip.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.12.UpuePQ&is_b=1&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    setcount = re.search(r'sellCount":(.*?)}', scode).group(1)
    price = re.findall(r'"price":"([\d\.]{4,})"', scode)
    kucun = re.search(r'"icTotalQuantity":(.*?),"', scode).group(1)
    # print(scode.encode('utf-8','ignore'))
    print('月成交记录/月销量:',
          setcount,
          '原价:',
          price[0],
          '促销价:',
          price[1],
          '总库存:',
          kucun)

def get2():
    url = r'http://dsr.rate.tmall.com/list_dsr_info.htm?itemId=' + str(pid)
    headers1 = {'GET': '',
                'Host': "dsr.rate.tmall.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.8.C2H93V&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    gradeavg = re.search(r'{"gradeAvg":(.*?),"', scode).group(1)
    rate = re.search(r'"rateTotal":(.*?)}', scode).group(1)
    print('平均评分:', gradeavg, '评论数量:', rate)

get1()
get2()
