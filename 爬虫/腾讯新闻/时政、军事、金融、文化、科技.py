# coding = utf-8
import requests
import re
import json
import pymysql
import time

choices = [
    ['cid=135&token=6e92c215fb08afa901ac31eca115a34f&ext=world','1'],#时政
    ['cid=135&token=6e92c215fb08afa901ac31eca115a34f&ext=milite_pc','2'],#军事
    ['cid=92&token=54424c1ebe77ea829a41040a3620d0e7&ext=finance','3'],#金融
    ['cid=146&token=49cbb2154853ef1a74ff4e53723372ce&ext=cul','4'],#文化
    ['cid=92&token=54424c1ebe77ea829a41040a3620d0e7&ext=tech','6']#科技
           ]
# 解析主要数据
def get_data(num,choice,code):
    url='https://pacaio.match.qq.com/irs/rcd?'+str(choice)+'&page='+str(num)
    response = requests.get(url)
    html = response.text
    re_0 = re.search(r'{.*}',html).group()
    Data = json.loads(re_0)
    data = Data['data']
    for new in data:
        app_id = new['app_id']#新闻id
        print(app_id)
        title = new['title']#新闻题目
        # tags = new['tags']#标签
        bimg = new['bimg']#图片网络连接
        # category_chn = new['category_chn']#新闻种类
        # intro = new['intro']#简讯
        source = new['source']#来源
        timing = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#当前时间
        contents = get_page(app_id)
        if contents=='':
            continue
            # print(contents)
        # 定义数据库对应字段
        data_in_db = {
            'title': title,#标题
            'content': contents,#内容
            'publishDate':timing,#当前时间
            'author':source,#来源
            'typeId':code,#新闻类型
            'click':0,
            'isHead':0,
            'isImage':0,
            'imageName': bimg,#图片链接
            'isHot':0
        }
        # 写入数据库
        print_to_db(data_in_db)

# 通过app_id解析html获取内容
def get_page(app_id):
    date = app_id[0:8]
    url_ing = 'https://new.qq.com/omn/'+str(date)+'/'+str(app_id)+'.html'
    response_ing = requests.get(url_ing)
    html = response_ing.text
    try:
        contents = re.search(r'<div class="content-article">(.*)<div id="Comment"></div>',html,re.S).group()
    # print(contents)
    #无用数据过滤
        return contents
    except:
        return '0'

# 将数据存入mysql
def print_to_db(data_in_db):
    db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='db_news')
    cursor = db.cursor()
    table = 't_news_copy'
    keys = ', '.join(data_in_db.keys())
    values = ', '.join(['%s'] * len(data_in_db))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
       cursor.execute(sql, tuple(data_in_db.values()))
       print('Successful')
       db.commit()
    except:
       print('Failed')
       db.rollback()
    cursor.close()
    db.close()

if __name__ == '__main__':
    for choice in choices:
        for num in range(0,5):
            get_data(num,choice[0],choice[1])
            print('***************************************')

