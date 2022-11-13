#salary薪资和岗位的爬虫
# 该程序由方博完成

import sqlite3
from calendar import month
from http.cookiejar import Cookie
from pymysql import *
import requests
from bs4 import BeautifulSoup
import re
import random
import datetime
import time

def get_ua():
    first_num = random.randint(55, 76)
    third_num = random.randint(0, 3800)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_14_5)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


def send_requests1(place, job, ua):
    url = 'https://www.jobui.com/trends/{0}-{1}/'.format(place, job)
    headers = {
        'User-Agent': ua
    }
    resp = requests.get(url, headers=headers)
    return resp.text


def send_requests2(kinds, city, page, ua):
    url = 'https://www.jobui.com/jobs?jobKw={0}&cityKw={1}&n={2}'.format(kinds, city, page)
    headers = {
        'User-Agent': ua
    }
    resp = requests.get(url, headers=headers)
    return resp.text


def pares_html1(html):
    bs = BeautifulSoup(html, 'html.parser')
    x = bs.find('div', class_='jobui-copyright-logo-box mb10')
    if x == None: return None
    y = x.find('div', id='month-job')
    if y == None: return None
    return y


def pares_html2(html):
    bs = BeautifulSoup(html, 'html.parser')
    x = bs.findAll('span', class_='job-pay-text')
    if x == None: return None
    i = len(x)
    for j in range(0, i - 1):
        x[j] = x[j].text
    if x == None: return None
    return x


def clean1(a, year, tt):
    b = re.search('"year":"{0}","month":"{1}","jobNum":\d+'.format(year, tt), str(a))
    if b == None: return None
    b = b.group()
    b = re.sub('"year":"{0}","month":"{1}","jobNum":'.format(year, tt), '', b)
    if b == None: return None
    b = float(b) / 1000
    if b == None: return None
    return float(b)


def clean2(a):
    i = len(a)
    allsalary = 0
    allnumber = 0
    for j in range(0, i - 1):
        b = re.search("\d+-\d+元", a[j])
        if b != None:
            b = b.group()
            b = re.sub("-\d+元", '', b)
            b = float(b)
            allsalary = allsalary + b
            allnumber = allnumber + 1
    return allsalary, allnumber


def start1(place, job, ua, year, tt):
    resp_data = send_requests1(place, job, ua)
    a = pares_html1(resp_data)
    if a == None: return None
    b = clean1(a, year, tt)
    if b == None: return None
    return b


def start2(kinds, city, ua, page):
    resp_data = send_requests2(kinds, city, page, ua)
    a = pares_html2(resp_data)
    if a == None: return 0
    b = clean2(a)
    if b == None: return 0
    return b


if __name__ == '__main__':
    conn = sqlite3.connect("HouseAndSalary.db")  # 打开或创建数据库文件
    print("成功打开数据库")
    cur_obj = conn.cursor()  # 获取游标
    id = 1
    for place in {'beijing', 'shanghai', 'chengdu', 'hefei', 'xiamen', 'lanzhou', 'guangzhou', 'shenzhen', 'nanning',
                  'guiyang', 'haikou', 'shijiazhuang', 'haerbin', 'zhengzhou', 'wuhan', 'changsha', 'nanjing', 'suzhou',
                  'nanchang', 'changchun', 'shenyang', 'dalian', 'huhehaote', 'qingdao', 'jinan', 'xian', 'taiyuan',
                  'wulumuqi', 'kunming', 'hangzhou', 'fuzhou', 'chongqing', 'tianjin', 'ningbo'}:
        if place == 'beijing':
            city = '北京'
        elif place == 'shanghai':
            city = '上海'
        elif place == 'chengdu':
            city = '成都'
        elif place == 'hefei':
            city = '合肥'
        elif place == 'xiamen':
            city = '厦门'
        elif place == 'lanzhou':
            city = '兰州'
        elif place == 'guangzhou':
            city = '广州'
        elif place == 'shenzhen':
            city = '深圳'
        elif place == 'nanning':
            city = '南宁'
        elif place == 'guiyang':
            city = '贵阳'
        elif place == 'haikou':
            city = '海口'
        elif place == 'shijiazhuang':
            city = '石家庄'
        elif place == 'haerbin':
            city = '哈尔滨'
        elif place == 'zhengzhou':
            city = '郑州'
        elif place == 'wuhan':
            city = '武汉'
        elif place == 'changsha':
            city = '长沙'
        elif place == 'nanjing':
            city = '南京'
        elif place == 'suzhou':
            city = '苏州'
        elif place == 'nanchang':
            city = '南昌'
        elif place == 'changchun':
            city = '长春'
        elif place == 'shenyang':
            city = '沈阳'
        elif place == 'dalian':
            city = '大连'
        elif place == 'huhehaote':
            city = '呼和浩特'
        elif place == 'qingdao':
            city = '青岛'
        elif place == 'jinan':
            city = '济南'
        elif place == 'xian':
            city = '西安'
        elif place == 'taiyuan':
            city = '太原'
        elif place == 'wulumuqi':
            city = '乌鲁木齐'
        elif place == 'kunming':
            city = '昆明'
        elif place == 'hangzhou':
            city = '杭州'
        elif place == 'fuzhou':
            city = '福州'
        elif place == 'chongqing':
            city = '重庆'
        elif place == 'tianjin':
            city = '天津'
        else:
            city = '宁波'

        for job in ['qianduan', 'kaifa', 'suanfa', 'ceshi']:
            if job == 'qianduan':
                kinds = '前端'
            elif job == 'kaifa':
                kinds = '开发'
            elif job == 'suanfa':
                kinds = '算法'
            else:
                kinds = '测试'
            allsalary = 0
            allnumber = 0
            for page in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
                ua = get_ua()
                x = start2(kinds, city, ua, page)
                if x != None:
                    allsalary = allsalary + x[0]
                    allnumber = allnumber + x[1]
            if allnumber == 0: allnumber = 100
            salary = float(allsalary) / float(allnumber)
            salary = float(salary / 1000)
            for datt in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                         '18']:
                if datt == '1':
                    tt = '06'
                    year = '2022'
                    str1 = "'2022-06-01'"
                elif datt == '2':
                    tt = '05'
                    year = '2022'
                    str1 = "'2022-05-01'"
                elif datt == '3':
                    tt = '04'
                    year = '2022'
                    str1 = "'2022-04-01'"
                elif datt == '4':
                    tt = '03'
                    year = '2022'
                    str1 = "'2022-03-01'"
                elif datt == '5':
                    tt = '02'
                    year = '2022'
                    str1 = "'2022-02-01'"
                elif datt == '6':
                    tt = '01'
                    year = '2022'
                    str1 = "'2022-01-01'"
                elif datt == '7':
                    tt = '12'
                    year = '2021'
                    str1 = "'2021-12-01'"
                elif datt == '8':
                    tt = '11'
                    year = '2021'
                    str1 = "'2021-11-01'"
                elif datt == '9':
                    tt = '10'
                    year = '2021'
                    str1 = "'2021-10-01'"
                elif datt == '10':
                    tt = '09'
                    year = '2021'
                    str1 = "'2021-09-01'"
                elif datt == '11':
                    tt = '08'
                    year = '2021'
                    str1 = "'2021-08-01'"
                elif datt == '12':
                    tt = '07'
                    year = '2021'
                    str1 = "'2021-07-01'"
                elif datt == '13':
                    tt = '06'
                    year = '2021'
                    str1 = "'2021-06-01'"
                elif datt == '14':
                    tt = '05'
                    year = '2021'
                    str1 = "'2021-05-01'"
                elif datt == '15':
                    tt = '04'
                    year = '2021'
                    str1 = "'2021-04-01'"
                elif datt == '16':
                    tt = '03'
                    year = '2021'
                    str1 = "'2021-03-01'"
                elif datt == '17':
                    tt = '02'
                    year = '2021'
                    str1 = "'2021-02-01'"
                else:
                    tt = '01'
                    year = '2021'
                    str1 = "'2021-01-01'"
                ua = get_ua()
                number = start1(place, job, ua, year, tt)
                if number == None: number = 0
                cur_obj.execute(
                    'insert into salary(id,city,month,kinds,salary,number) values("%s","%s",{0},"%s","%s","%s")'.format(
                        str1), (id, city, kinds, float(salary), float(number)))
                print(id)
                id = id + 1
    conn.commit()
    cur_obj.close()
    conn.close()  # 关闭数据库连接
