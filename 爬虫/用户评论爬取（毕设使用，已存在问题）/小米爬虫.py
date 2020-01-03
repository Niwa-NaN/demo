# coding = 'utf-8'
import requests
import re
import time
import json
import xlwt

headers = {'Cookie': 'xmuuid=XMGUEST-49451870-CB74-11E8-8767-4FB089069459; mstuid=1539056094459_5329; muuid=1539874091847_2635; netalliance_id=1.2.17489.; muwd=xiaomi%20; mucid=17489.0001; mutid=17489.0001zOHOfnhyUXU57Qpu7a30190207151801; muctm=; muctmr=; XM_agreement=0; lastsource=www.baidu.com; client_id=180100041086; masid=17489.0001; log_code=16e0871d7b28e6a3-63a344b2c651613b|https%3A%2F%2Fwww.mi.com%2Fmi8%2F; xm_comm_sid=h1dp793fpb8t2d43q89j4g8vd2; pageid=e1830aa1492fb981; mstz=||886876995.8||https%253A%252F%252Fitem.mi.com%252Fcomment%252F10000099.html|https%25253A%25252F%25252Fwww.mi.com%25252Fmi8%25252F; xm_vistor=1539056094459_5329_1549523930314-1549523951059; msttime=https%3A%2F%2Fitem.mi.com%2Fcomment%2Fdetail%3Fcomment_id%3D156602849',
            'DNT': '1',
            'Host': 'comment.huodong.mi.com',
            'Referer': 'https://item.mi.com/comment/10000099.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

wb = xlwt.Workbook()

ids = [['小米8','v_pid=10000099'],
       ['小米8se','v_pid=10000100'],
       ['小米8青春版','v_pid=10000117']
       ]

def main(offset,id):
    url = 'https://comment.huodong.mi.com/comment/entry/getList?goods_id=0&'+str(id)+'&orderby=22&showimg=0&profile_id=0&pagesize=5&pageindex='+str(offset)
    response = requests.get(url,headers = headers)
    html = response.text
    get_comments(html)

def get_comments(html):
    global j
    key = re.search('{(.*)}',html).group()
    key = json.loads(key)
    # print(key)
    data = key['data']
    for comment in data['comments']:
        try:
            url_new = 'https://comment.huodong.mi.com/comment/entry/commentDetails?comment_id='+str(comment['comment_id'])+'&jsonpcallback=jQuery111302690964178669395_1550907654335&_=1550907654336'
            headers_new = headers
            headers_new['Refer'] = 'https://item.mi.com/comment/detail?comment_id='+str(comment['comment_id'])
            response_new = requests.get(url_new,headers = headers_new)
            html_new = response_new.text
            # print(html_new)
            # print(response_new)
            data_new = re.search('{.*}',html_new)
            data_new = json.loads(data_new.group())
            data_new = data_new['data']
            comment_info = data_new['commentInfo']
            comment_content = comment_info['comment_content']
            goods_name = comment_info['goods_name']
            demo = goods_name.split(' ')
            if id[1]=='v_pid=10000099':
                name_1 = comment_content
                name_2 = demo[4]
                name_3 = demo[2].split('内存')[0]
                name_4 = demo[3]
            if id[1]=='v_pid=10000100':
                name_1 = comment_content
                name_2 = demo[5]
                name_3 = demo[3].split('内存')[0]
                name_4 = demo[4]
            if id[1]=='v_pid=10000117':
                name_1 = comment_content
                name_2 = demo[4]
                name_3 = demo[3].split('内存')[0]
                name_4 = '未知'

            ws.write(j,0,name_1)
            ws.write(j,1,name_2)
            ws.write(j,2,name_3)
            ws.write(j,3,name_4)
            j+=1

            # print(goods_name)
            print(name_1)
            print(name_2)
            print(name_3)
            print(name_4)
            print('\n')
        except:
            continue
    wb.save('MI小米评论数据第二次完善爬取.xls')

if __name__ == '__main__':
    for id in ids:
        j=1
        ws = wb.add_sheet('MIMI数据demo%s'%id[0])
        ws.write(0,0,'评论')
        ws.write(0,1,'手机颜色')
        ws.write(0,2,'手机运行内存')
        ws.write(0,3,'手机存储内存')
        for i in range(0,100):
            main(i,id[1])
            time.sleep(1)

