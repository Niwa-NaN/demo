import requests
import re
import json
import time
import xlwt


ids = [#['小米8','itemId=570133905140&spuId=982146220','cna=MMsFE5Q2bD8CAXWIAobNGLOU; lid=%E5%90%9B%E9%99%8C%E6%AC%BA%E4%B9%8B%E4%BB%A5%E6%96%B9; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; uss=""; enc=sV7Hj3owjcf4boTo4GsDNB%2BCUAfStnjzDrbHMzLtUUliHBuzVewDu8K0ybMZIgxJKVDHqVNbizt1rlDBPwF0cQ%3D%3D; uc1=cookie14=UoTZ5bHjpK2Xvw%3D%3D; t=3619bb0c6b71276f36c43796bc48f8f2; uc3=vt3=F8dByEzYF8Jpu%2FblRvc%3D&id2=UUBb21SrAb742w%3D%3D&nk2=3SOGh5UQGHYQpSVK&lg2=URm48syIIVrSKA%3D%3D; tracknick=%5Cu541B%5Cu964C%5Cu6B3A%5Cu4E4B%5Cu4EE5%5Cu65B9; lgc=%5Cu541B%5Cu964C%5Cu6B3A%5Cu4E4B%5Cu4EE5%5Cu65B9; _tb_token_=e65e3ee5773e6; cookie2=11a33fad389e7be2c37435715704ba07; _m_h5_tk=24c20cb659f2ef0fa4f3efe0eb6604d4_1551282763063; _m_h5_tk_enc=0c06cbdd3f8816ec19193c4cb3c7bd32; x5sec=7b22726174656d616e616765723b32223a226564663261333762356662643861643539626634383934656164373534373932434e367532754d4645506a37317332556a637a7757673d3d227d;' ],
       # ['小米8se','itemId=572473824056&spuId=991726141','cna=MMsFE5Q2bD8CAXWIAobNGLOU; lid=%E5%90%9B%E9%99%8C%E6%AC%BA%E4%B9%8B%E4%BB%A5%E6%96%B9; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; uss=""; enc=sV7Hj3owjcf4boTo4GsDNB%2BCUAfStnjzDrbHMzLtUUliHBuzVewDu8K0ybMZIgxJKVDHqVNbizt1rlDBPwF0cQ%3D%3D; uc1=cookie14=UoTZ5bDZRkUdyQ%3D%3D; t=3619bb0c6b71276f36c43796bc48f8f2; uc3=vt3=F8dByEzYF8Jpu%2FblRvc%3D&id2=UUBb21SrAb742w%3D%3D&nk2=3SOGh5UQGHYQpSVK&lg2=URm48syIIVrSKA%3D%3D; tracknick=%5Cu541B%5Cu964C%5Cu6B3A%5Cu4E4B%5Cu4EE5%5Cu65B9; lgc=%5Cu541B%5Cu964C%5Cu6B3A%5Cu4E4B%5Cu4EE5%5Cu65B9; _tb_token_=737efe818855b; cookie2=1a37ee6fede751eecd303d91582d1235; _m_h5_tk=fd759229bcbb1a1d03428b746e539753_1551505077292; _m_h5_tk_enc=0ade43d57fd75263739264f919e2c1bb; l=bBSFMg5rvuDZSAIvBOfaiuIRXVQ95IRbzsPzw4ZB8ICPObfkuIeVWZa1GB8DC3GVa63vR3-jQ4LQBvL_uyUB5; isg=BBISxXjXmtSA1OFrKleFIGJPY9g0iz2A1NwpO9xr2kWA77HpxLEFzYxBXwv2n45V'],
       ['小米8青春版','itemId=577345730738&spuId=1063346732','cna=MMsFE5Q2bD8CAXWIAobNGLOU; lid=%E5%90%9B%E9%99%8C%E6%AC%BA%E4%B9%8B%E4%BB%A5%E6%96%B9; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; enc=sV7Hj3owjcf4boTo4GsDNB%2BCUAfStnjzDrbHMzLtUUliHBuzVewDu8K0ybMZIgxJKVDHqVNbizt1rlDBPwF0cQ%3D%3D; uc1=cookie14=UoTZ5iTMHlRwYQ%3D%3D; t=3619bb0c6b71276f36c43796bc48f8f2; uc3=vt3=F8dByEv1QDQFpAXumIg%3D&id2=UUBb21SrAb742w%3D%3D&nk2=3SOGh5UQGHYQpSVK&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=%5Cu541B%5Cu964C%5Cu6B3A%5Cu4E4B%5Cu4EE5%5Cu65B9; lgc=%5Cu541B%5Cu964C%5Cu6B3A%5Cu4E4B%5Cu4EE5%5Cu65B9; _tb_token_=737335ebee3e0; cookie2=16262832bae1c93e036e999e362d489e; x5sec=7b22726174656d616e616765723b32223a226130643539393463663866336332323861386331383263333763323563303865434d61516a2b5146454b6646367036466b4c69327867453d227d; l=bBSFMg5rvuDZSbbUBOCgGuIRXVQtAIRf_uPRwk1pi_5CN_LmKT_OlsVMmEp6Vj5P9bLB4nMZyewtvFMUJy9f.; isg=BHBwogG82PDu44PNPD0HrswFQT4CEX8-6maL3WrBG0u6JRHPEst3kz4TfW3gsgzb']]
headers = {'cookie': 'cna=MMsFE5Q2bD8CAXWIAobNGLOU; lid=%E5%90%9B%E9%99%8C%E6%AC%BA%E4%B9%8B%E4%BB%A5%E6%96%B9; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; uss=""; enc=sV7Hj3owjcf4boTo4GsDNB%2BCUAfStnjzDrbHMzLtUUliHBuzVewDu8K0ybMZIgxJKVDHqVNbizt1rlDBPwF0cQ%3D%3D; uc1=cookie14=UoTZ5bDZRkUdyQ%3D%3D; t=3619bb0c6b71276f36c43796bc48f8f2; uc3=vt3=F8dByEzYF8Jpu%2FblRvc%3D&id2=UUBb21SrAb742w%3D%3D&nk2=3SOGh5UQGHYQpSVK&lg2=URm48syIIVrSKA%3D%3D; tracknick=%5Cu541B%5Cu964C%5Cu6B3A%5Cu4E4B%5Cu4EE5%5Cu65B9; lgc=%5Cu541B%5Cu964C%5Cu6B3A%5Cu4E4B%5Cu4EE5%5Cu65B9; _tb_token_=737efe818855b; cookie2=1a37ee6fede751eecd303d91582d1235; _m_h5_tk=72eb45fefe9fdf6e9f89818596655e4b_1551325945772; _m_h5_tk_enc=efe5c7b254c5d6698514976f240bf0b8; x5sec=7b22726174656d616e616765723b32223a223732366134626461303066623166623138616232313533613931353137626134434a4f6233654d46454d7a386b61614c30385a43227d;',
            'dnt': '1',
            'referer': 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-14756119800.81.79d248feB4xTbJ&id=570133905140&rn=fd8ee7f741b66a1933c09b6280a1f5a0&abbucket=18&sku_properties=10004:1617715035;5919063:6536025',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

wb = xlwt.Workbook()

def main(offset,id):
    url = 'https://rate.tmall.com/list_detail_rate.htm?'+str(id)+'&sellerId=1714128138&order=3&currentPage='+str(offset)+'&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvAQvovZhvUpCkvvvvvjiPRLzWAj3ERsSUtjrCPmPvzjl8P2S9tj3vRLdpgjYnRUhCvCLNq0JwNxdNzY%2FTrN1waYY9zYPw5OhCvCWpvR6GMxdNzYY4UYAYAZrqv6rudphvhhamn9sovhvPDMoYKLuAbDurvpvEph7G2hGvpvOgRphvChCvvvmCvpvWzM%2F8PvtwzYMNVbzw3QhvChCCvvm5vpvhphvhHvGCvvpvvvvvmphvLhL1a9mFdcpiNB3rl8gcW6W%2BBaV9hBHiBox%2Flj7J%2B3%2BSjLPEDLKAWyhD24oQ%2Bul68c6OfaoKHAiH8ZJ9kCVZfvyfb5c6nqUzH1Ez5B7tvpvIphvvvvvvphCvpC9vvvCm%2BZCvVvvvvhWFphvOvvvvpzDvpC9vvvC2J4yCvv3vpvoDVO338IyCvvXmp99hVtQCvpvVphhvvvvvRphvChCvvvmrvpvEphp42nZvpH4%2FRphvChCvvvvtvpvhphvvvv%3D%3D&needFold=0&_ksTS=1551323201947_2990&callback=jsonp2991'
    response = requests.get(url,headers = headers)
    html = response.text
    # print(html)
    get_comments(html)
def get_comments(html):
    re_0 = re.search(r'({.*})', html)
    re_0 = json.loads(re_0.group())
    rate_detail = re_0['rateDetail']
    rate_list = rate_detail['rateList']
    # print(rate_list)
    global j
    for comment in rate_list:
        try:
            auction_sku = comment['auctionSku']
            rate_content = comment['rateContent']#评论
            if rate_content == '此用户没有填写评论!':
                rate_content = comment['appendComment']['content']
            auction_sku = re.search(r'网络类型:4G\+全网通;机身颜色:(.*?);套餐类型:官方标配;存储容量:(.*)',auction_sku)
            auction_1 = auction_sku.group(1)#颜色
            auction_2 = auction_sku.group(2).split('+')[0]+'GB'#手机运行内存
            auction_3 = auction_sku.group(2).split('+')[1]#手机存储内存
            ws.write(j,0,rate_content)
            ws.write(j,1,auction_1)
            ws.write(j,2,auction_2)
            ws.write(j,3,auction_3)
            j+=1
            print(rate_content)
            print(auction_1)
            print(auction_2)
            print(auction_3)
            print('\n')
        except:
            continue
    wb.save('TM小米评论数据首次完善爬取.xls')

if __name__ == '__main__':
    for id in ids:
        headers['cookie'] = id[2]
        j = 1
        ws = wb.add_sheet('TMMI数据demo%s'%id[0])
        ws.write(0,0,'评论')
        ws.write(0,1,'手机颜色')
        ws.write(0,2,'手机运行内存')
        ws.write(0,3,'手机存储内存')
        for i in range(0,99):
            main(i,id[1])
            time.sleep(1)
        print(id[0])
        print('------------------------------------------------------------------')
