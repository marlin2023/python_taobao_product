# python3
import urllib.request
import re

def get_tmall(pid):
    url = r'http://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=false&callback=setMdskip&itemId=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "mdskip.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.12.UpuePQ&is_b=1&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    price = re.findall(r'"price":"([\d\.]{4,})"', scode)
    if len(price) != 0 :   
        print (price[1])
    else:
        print ('-下架')
def get_taobao(pid):
    url = r'http://detailskip.taobao.com/json/sib.htm?p=1&itemId=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "detailskip.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://item.taobao.com/item.htm?p=1&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    price = re.findall(r'(?:price\W*)(\d*\.\d*)', scode)
    if len(price) != 0: 
        print (price[0])
    else:
        print ('下架') 

def get_product_price(product_url):
    website = product_url;
    m = re.match('http:\/\/(.*).(com|cn)',website).group(1)
    productIdTmp = re.search(r'(\?|&)(id=)\d+' ,website).group()
    productId = re.search(r'\d+', productIdTmp).group()
    print ("productId" ,productId)
    if m == 'item.taobao':	##淘宝
        get_taobao (productId)
        print ("taobao")
    elif m == 'detail.tmall' or m == 'chaoshi.detail.tmall':  ##天猫
        get_tmall(productId)
        print ("tianmao")

if __name__ == '__main__':
	
    pid = input("please input the website:")
    #get_taobao(pid)
    get_product_price(pid)
