# coding = utf-8
import requests
import re
import json
import pymysql
import time

sports=['nba','cba','football','olympic']
# 解析主要数据
def get_data(sport):
    url='https://pacaio.match.qq.com/irs/rcd?cid=146&token=49cbb2154853ef1a74ff4e53723372ce&id=&ext=sports_'+str(sport)
    response = requests.get(url)
    html = response.text
    re_0 = re.search(r'{.*}',html).group()
    Data = json.loads(re_0)
    # print(Data.keys())
    data = Data['data']
    for new in data:
        app_id = new['app_id']#新闻id
        title = new['title']#新闻题目
        tags = new['tags']#标签
        bimg = new['bimg']#图片网络连接
        category_chn = new['category_chn']#新闻种类
        intro = new['intro']#简讯
        source = new['source']#来源
        timing = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#当前时间
        print(app_id)
        print(title)
        # 屏蔽无内容的错误网页和视频页
        try:
            contents = get_page(app_id)
            # print(contents)
            if contents == '':
                continue
        except:
            continue
        # 定义数据库对应字段
        data_in_db = {
            'title': title,  # 标题
            'content': contents,  # 内容
            'publishDate': timing,  # 当前时间
            'author': source,  # 来源
            'typeId': 5,  # 新闻类型
            'click': 0,
            'isHead': 0,
            'isImage': 0,
            'imageName': bimg,  # 图片链接
            'isHot': 0
        }
        # 写入数据库
        print_to_db(data_in_db)

# 通过app_id解析html获取内容
def get_page(app_id):
    url_ing = 'https://new.qq.com/rain/a/'+str(app_id)
    response_ing = requests.get(url_ing)
    html = response_ing.text
    contents = re.search(r'<div class="content-article">(.*)<div id="Comment"></div>', html, re.S).group()
    return contents

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
    for sport in sports:
        get_data(sport)
        print('----------------------------------------------------------------------------')


