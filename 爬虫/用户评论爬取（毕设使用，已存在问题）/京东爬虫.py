import requests
import re
import xlwt
import json
import time

headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
           }

wb = xlwt.Workbook()


ids = [
    ['小米8','fetchJSON_comment98vv88845&productId=7437788']
    #    ['小米8se','fetchJSON_comment98vv9079&productId=8656283''&productId=8656283']，
    #    ['小米8青春版','fetchJSON_comment98vv20930&productId=100000503295']
       ]




def main(offset,idname):
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback='+str(idname)+'&score=0&sortType=5&page='+str(offset)+'&pageSize=10&isShadowSku=00&rid=0&fold=1'
    response = requests.get(url,headers = headers)
    html = response.text
    print('----------------------------------------------------------------------')
    print(data[1])

    get_comments(html)

def get_comments(html):
    print(ws.name)
    print('-----------------------------------------------------------------------')
    re_0 = re.search(r'{.*}',html).group(0)
    re_0 = json.loads(re_0)
    print(re_0.keys())
    # print(re_0['comments'])
    global j
    for i in re_0['comments']:
        sp = i['productSize']
        if sp == "":
            continue
        else:
            ws.write(j,0,i['content'])
            # ws.write(j,1,i['creationTime'])
            ws.write(j,2,i['productColor'])

            sp = str(sp).split('+')

            ws.write(j,3,sp[0])
            ws.write(j,4,sp[1])
            j+=1
            print(i['productSize'])
            print(i['content'])
            # print(i['creationTime'])
            print(i['productColor'])
            print(sp[0])
            print(sp[1])
            print('\n')
    wb.save('JD小米评论数据第二次完善爬取.xls')

if __name__ == '__main__':
    for data in ids:
        j = 1
        ws = wb.add_sheet('JDMI数据demo%s'%data[0])
        ws.write(0,0,'评论')
        ws.write(0,1,'时间')
        ws.write(0,2,'手机颜色')
        ws.write(0,3,'手机运行内存')
        ws.write(0,4,'手机存储内存')
        for i in range(0,99):
            main(i,data[1])
            time.sleep(0.3)
