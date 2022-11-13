# 爬取房屋数据，由王浩完成
# coding=utf-8
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import sqlite3
import random

agent_list = [
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10"
]


def get_data():
    return random.random()


def get_buy_data(city, city_name):  # 城市购房信息，可获取多个城市
    find_buy_link = re.compile(r'<a alt=".*?" class="select-item multi-item".*?href="(.*?)">.*?</a>', re.S)
    find_buy_name = re.compile(r'<a alt=".*?" class="select-item multi-item".*?href=".*?">(.*?)</a>', re.S)
    find_buy_price = re.compile(r'<p class="price">.*?<span>(\d*?)</span>', re.S)
    datalist_buy = []
    id_num = 0
    for i in city:
        baseurl = "https://%s.fang.anjuke.com/loupan/" % i
        headers = {
            "cookie": "isp=true; isp=true; lps=https%3A%2F%2Fwh.zu.anjuke.com%2F%7C; aQQ_ajkguid=12572D50-5083-522C-9141-E862ABA244BA; id58=CpQBZWLDjosQhirZZZv0Ag==; cmctid=1; xxzl_cid=fda92b0f32474ac094861998cc1f31ce; xzuid=1fa4d5e5-f2e8-4d1b-a816-191b962ae9d0; sessid=84960073-6A2D-AD41-6713-SX0705092719; isp=true; isp=true; obtain_by=2; twe=2; wmda_uuid=a69f5c37718735a47e4706c859431d59; wmda_new_uuid=1; wmda_visited_projects=%3B8788302075828; 58tj_uuid=caba657c-43a9-480b-a877-891b5fd75f80; als=0; wmda_session_id_8788302075828=1656991342123-0a2171eb-658f-3549; init_refer=https%253A%252F%252Fbj.fang.anjuke.com%252Floupan%252Fyanjiao%252F; new_uv=3; new_session=0; ctid=14",
            'User-Agent': random.choice(agent_list)
            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
        }
        print(baseurl)
        count = 0
        html = ask_url(baseurl, headers)
        soup = BeautifulSoup(html, "html.parser")
        item = soup.find('div', class_='filter')
        item = str(item)
        link = re.findall(find_buy_link, item)
        name = re.findall(find_buy_name, item)
        datalist_city_buy = []
        for html in link:
            datalist = []
            for page_num in range(1, 51):
                html_tmp = html + "p%d/" % page_num
                # print(html_tmp)
                html_tmp = ask_url(html_tmp, headers)
                soup = BeautifulSoup(html_tmp, "html.parser")
                prcie_item = soup.findAll('div', class_='item-mod')
                prcie_item = str(prcie_item)
                price = re.findall(find_buy_price, prcie_item)
                if len(price):
                    for price_num in price:
                        datalist.append([id_num + 1, city_name[i], name[count], price_num])
                        id_num += 1
                else:
                    break
            count += 1
            if not datalist:
                break
            datalist_city_buy = datalist_city_buy + datalist
        print(datalist_city_buy)
        datalist_buy = datalist_buy + datalist_city_buy
    print(datalist_buy)
    return datalist_buy


def get_rent_data(city, city_name):  # 城市租房信息，可获取多个城市
    find_rent_link = re.compile(r'<a href="(.*?)" title=".*?">.*?</a>', re.S)
    find_rent_name = re.compile(r'<a href=".*?" title=".*?">(.*?)</a>', re.S)
    find_rent_price = re.compile(r'<b class="strongbox">(\d*?)</b>', re.S)
    datalist_rent = []
    id_num = 0
    for i in city:
        baseurl = "https://%s.zu.anjuke.com/fangyuan/" % i
        headers = {
            "cookie": "isp=true; isp=true; lps=https%3A%2F%2Fwh.zu.anjuke.com%2F%7C; aQQ_ajkguid=12572D50-5083-522C-9141-E862ABA244BA; id58=CpQBZWLDjosQhirZZZv0Ag==; cmctid=1; xxzl_cid=fda92b0f32474ac094861998cc1f31ce; xzuid=1fa4d5e5-f2e8-4d1b-a816-191b962ae9d0; sessid=84960073-6A2D-AD41-6713-SX0705092719; isp=true; isp=true; obtain_by=2; twe=2; wmda_uuid=a69f5c37718735a47e4706c859431d59; wmda_new_uuid=1; wmda_visited_projects=%3B8788302075828; 58tj_uuid=caba657c-43a9-480b-a877-891b5fd75f80; als=0; wmda_session_id_8788302075828=1656991342123-0a2171eb-658f-3549; init_refer=https%253A%252F%252Fbj.fang.anjuke.com%252Floupan%252Fyanjiao%252F; new_uv=3; new_session=0; ctid=14",
            'User-Agent': random.choice(agent_list)
            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
        }
        count = 0
        print(baseurl)
        html = ask_url(baseurl, headers)
        soup = BeautifulSoup(html, "html.parser")
        item = soup.find('div', class_='sub-items sub-level1')
        item = str(item)
        link = re.findall(find_rent_link, item)
        name = re.findall(find_rent_name, item)
        while "" in link:  # 判断是否有空值在列表中
            link.remove("")  # 如果有就直接通过remove删除)
        while "" in name:  # 判断是否有空值在列表中
            name.remove("")  # 如果有就直接通过remove删除
        datalist_city_rent = []
        for html in link:
            datalist = []
            print(html)
            for page_num in range(1, 51):
                html_tmp = html + "p%d/" % page_num
                html_tmp = ask_url(html_tmp, headers)
                soup = BeautifulSoup(html_tmp, "html.parser")
                prcie_item = soup.findAll('div', class_='zu-side')
                prcie_item = str(prcie_item)
                price = re.findall(find_rent_price, prcie_item)
                if len(price):
                    for price_num in price:
                        datalist.append([id_num + 1, city_name[i], name[count], price_num])
                        id_num += 1
                else:
                    break
            count += 1
            if not datalist:
                break
            datalist_city_rent = datalist_city_rent + datalist
        print(datalist_city_rent)
        datalist_rent = datalist_rent + datalist_city_rent
    print(datalist_rent)
    return datalist_rent

#这部分由方博完成
def ask_url(url, headers):
    html = ""
    try:
        req = urllib.request.Request(url=url, headers=headers)
        request = urllib.request.urlopen(req)
        html = request.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


def save_buy_data(db, conn, datalist):
    print("save buy data...")
    for data in datalist:
        for index in range(len(data)):
            if index == 1 or index == 2:
                data[index] = data[index].replace("'", "\"")
            else:
                data[index] = int(data[index])
        sql_insert = '''
                               insert into buy_houses(id,city, district, buy_price)
                               values (%d,\"%s\",\"%s\",%d)''' % (data[0], data[1], data[2], data[3]) + ";"
        db.execute(sql_insert)  # 执行sql语句
        conn.commit()  # 提交数据库操作
    print("save complete!")


def save_rent_data(db, conn, datalist):
    print("save rent data...")
    for data in datalist:
        for index in range(len(data)):
            if index == 1 or index == 2:
                data[index] = data[index].replace("'", "\"")
            else:
                data[index] = int(data[index])
        sql_insert = '''
                                   insert into rent_houses(id,city, district, rent_price)
                                   values (%d,\"%s\",\"%s\",%d)''' % (data[0], data[1], data[2], data[3]) + ";"
        db.execute(sql_insert)  # 执行sql语句
        conn.commit()  # 提交数据库操作
    print("save complete!")


def create_db(db, conn):
    sql_create_buy = '''
        create table buy_houses(
            id int primary key,
            city varchar(30) not null,
            district varchar(30) not null,
            buy_price int not null
        );
    '''
    sql_create_rent = '''
        create table rent_houses(
            id int primary key,
            city varchar(30) not null,
            district varchar(30) not null,
            rent_price int not null
        );
    '''
    sql_create_salary = '''
        create table salary (
        id int NOT NULL,
        city varchar(20) DEFAULT NULL,
        month date DEFAULT NULL,
        kinds varchar(20) DEFAULT NULL,
        salary float DEFAULT NULL,
        number float DEFAULT NULL,
        primary key (id)
        ) '''
    db.execute(sql_create_buy)  # 执行sql语句
    conn.commit()  # 提交数据库操作
    db.execute(sql_create_rent)  # 执行sql语句
    conn.commit()  # 提交数据库操作
    db.execute(sql_create_salary)  # 执行sql语句
    conn.commit()  # 提交数据库操作


def delete_table(db, conn):
    sql_delete = '''
            drop table buy_houses;
        '''
    db.execute(sql_delete)  # 执行sql语句
    conn.commit()  # 提交数据库操作
    sql_delete = '''
            drop table rent_houses;
        '''
    db.execute(sql_delete)  # 执行sql语句
    conn.commit()  # 提交数据库操作
    sql_delete = '''
            drop table salary;
        '''
    db.execute(sql_delete)  # 执行sql语句
    conn.commit()  # 提交数据库操作


def create():  # 获取数据并创建数据库
    # ['bj', 'hz', 'tj', 'hf', 'sh', 'fz', 'cq', 'nc']
    city = ['bj', 'hz', 'tj', 'hf', 'sh', 'fz', 'cq', 'nc',
     'jn', 'zz', 'hhht', 'wh', 'wlmq',
     'cs',  'gz',  'nn', 'cd',
    'sjz', 'gy', 'ty', 'km', 'shen', 'xa', 'cc', 'lz']
    city_name = {'bj': '北京', 'hz': '杭州', 'tj': '天津', 'hf': '合肥', 'sh': '上海', 'fz': '福州', 'cq': '重庆', 'nc': '南昌',
     'jn': '济南', 'zz': '郑州', 'hhht': '呼和浩特', 'wh': '武汉', 'wlmq': '乌鲁木齐',
     'cs': '长沙',  'gz': '广州', 'nn': '南宁', 'cd': '成都',
    'sjz': '石家庄', 'gy': '贵阳', 'ty': '太原', 'km': '昆明', 'shen': '沈阳', 'xa': '西安', 'cc': '长春', 'lz': '兰州'}

    datalist_buy = get_buy_data(city, city_name)  # 爬取购房数据
    datalist_rent = get_rent_data(city, city_name)  # 爬取租房数据
    conn = sqlite3.connect("HouseAndSalary.db")  # 打开或创建数据库文件
    print("成功打开数据库")
    c = conn.cursor()  # 获取游标
    # delete_table(c, conn)  # 删除数据库中的表
    # create_db(c, conn)  # 创建数据库表格
    save_buy_data(c, conn, datalist_buy)  # 存储购房数据到数据库中
    save_rent_data(c, conn, datalist_rent)# 存储购房数据到数据库中
    c.close()
    conn.close()  # 关闭数据库连接
    print("成功建表")


if __name__ == '__main__':
    create()  # 获取数据并创建数据库(还原数据库)
