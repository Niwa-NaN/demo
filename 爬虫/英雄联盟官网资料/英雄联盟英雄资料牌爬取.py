# coding = utf-8
# ***此处乱码可以依靠json格式为字典解决
import requests
import re
import json
import pymysql
# from multiprocessing import Pool

def get_one(hero_num):
    url="https://game.gtimg.cn/images/lol/act/img/js/hero/"+str(hero_num)+".js"
    response = requests.get(url)
    # print(response)
    html = response.text
    html = html.encode('utf-8').decode('utf-8')
    # print(html)
    re_0 = re.search(r'{.*}',html).group()
    data = json.loads(re_0)
    # print(data.keys())
    hero = data["hero"]
    skins = data["skins"]
    spells = data["spells"]
    name=hero['name']+' '+hero['title']
    skin = str(skins[0]["loadingImg"])
    print(name)
    print(skin)
    spell_list=[]
    for spell in spells:
        spell_now=spell["name"]+'\n'+spell["description"]+'\n'+str(spell['abilityIconPath'])
        spell_list.append(spell_now)
    for i in spell_list:
        print(i)
    data_in_db={
        'id':hero_num,
        'name':name,
        'skin':skin,
        'spell_0':spell_list[0],
        'spell_1':spell_list[1],
        'spell_2':spell_list[2],
        'spell_3':spell_list[3],
        'spell_4':spell_list[4]
    }
    # print_to_db(data_in_db)
# 将数据存入mysql
def print_to_db(data_in_db):
    db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='hero')
    cursor = db.cursor()
    table = 'hero'
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
    # hero_num_list=[]
    # pool = Pool()
    for num in range(1,556):
        try:
            get_one(num)
            print('----------------------------------------')
            print(num)
            print('----------------------------------------')
        except:
            continue





