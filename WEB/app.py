
#flask框架，由曾培益完成搭建
import os
from flask import Flask, render_template, url_for, request
# 以下过程，导入后端提供的数据库接口，导入数据库查询函数
import chartpy.avg_salary_num as avg_sa
import chartpy.vary_num as vn
import chartpy.search_db as ecr2
import chartpy.CityAnalyse as CA
import chartpy.analyse as AL
import chartpy.city_rate as CR
from chartpy.get_all_salary import get_all_salary


app = Flask(__name__)

# =======================================================   主页index.html
@app.route('/')
def index():
    # 利用接口函数查询数据库，并传参进HTML文件
    ec_l1 = avg_sa.avg_salary_kinds()
    print(ec_l1)
    ec_l2 = vn.vary_num_v2()
    print(ec_l2)
    er1 = CR.get_city_rate()
    chinaMap = get_all_salary()
    return render_template('index.html', avg_sal=ec_l1[0], avg_num=ec_l1[1], kf_value=ec_l2[0], qd_value=ec_l2[1],
                           sf_value=ec_l2[2], cs_value=ec_l2[3], buy_list=ecr2.get_buy_num(),
                           rent_list=ecr2.get_rent_num(), er1=er1, chinaMap=chinaMap
                           )

@app.context_processor  # 上下文渲染器，给所有html添加渲染参数
def inject_url():
    data = {
        "url_for": dated_url_for,
    }
    return data

# 这个函数主要是获取时间
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
    if filename:
        file_path = os.path.join(app.root_path, endpoint, filename)
        values['v'] = int(os.stat(file_path).st_mtime)  # 取文件最后修改时间的时间戳，文件不更新，则可用缓存
        return url_for(endpoint, **values)


# =============================================  分析页面 ==============================
@app.route('/analyse')
def analyse():
    # 从前端url的问号后得到参数
    # cityMap={'城市缩写':[code,cityCenter]} 城市缩写用全拼 shenzhen beijing之类
    # 城市字典是用来画分析页面的热力图的，需要城市名，城市行政区域划分代码，城市经纬度
    # 城市传参直接用中文，UTF-8编码
    cityMap = {'合肥': [340100, [117.27, 31.86]], '西安': [610100, [108.95, 34.27]], '济南': [370100, [117, 36.65]],
               '哈尔滨': [230100, [126.63, 45.75]],
               '大连': [210200, [121.62, 38.92]], '青岛': [370200, [120.33, 36.07]], '天津': [120000, [117.2, 39.13]],
               '南昌': [360100, [115.89, 28.68]],
               '厦门': [350200, [118.1, 24.46]], '上海': [310000, [121.48, 31.22]], '海口': [460100, [110.206424, 20.050057]],
               '乌鲁木齐': [650100, [87.623314, 43.832806]],
               '贵阳': [520100, [106.636816, 26.652747]], '南京': [320100, [118.802891, 32.064735]],
               '石家庄': [130100, [114.520828, 38.048684]],
               '宁波': [330200, [121.556686, 29.880177]], '成都': [510100, [104.071216, 30.576279]],
               '长春': [220100, [125.33017, 43.82178]],
               '深圳': [440300, [114.066112, 22.548515]], '沈阳': [210100, [123.438973, 41.811339]],
               '北京': [110000, [116.413554, 39.911013]],
               '杭州': [330100, [119.5, 29.7]], '南宁': [450100, [108.373351, 22.823037]],
               '苏州': [320500, [120.589613, 31.304566]],
               '兰州': [620100, [103.840692, 36.067312]], '郑州': [410100, [113.631349, 34.753488]],
               '武汉': [420100, [114.311831, 30.598428]],
               '昆明': [530100, [102.839667, 24.885953]], '福州': [350100, [119.302938, 26.080447]],
               '长沙': [430100, [112.945333, 28.233971]], '广州': [440100, [113.270793, 23.135308]],
               '呼和浩特': [150100, [111.758518, 40.847461]], '重庆': [500000, [106.557165, 29.570997]],
               '太原': [140100, [112.55706, 37.876885]]}
    cityArg = request.args["city"]
    jobArg = request.args["job"]
    Map = cityMap[cityArg]  # map应该是一个二元数组，将其传入分析html中！
    jobDict = {
        'sf': '算法',
        'cs': '测试',
        'qd': '前端',
        'kf': '开发'
    }

    buyDistr = CA.get_district_price(cityArg, 1)
    rentDistr = CA.get_district_price(cityArg, 2)

    wbx = AL.analyse_img(jobDict[jobArg], cityArg)
    rentPer = CA.get_district(cityArg)
    buyPer = CA.get_district(cityArg)

    rentPrice = list(rentDistr.values())
    buyPrice = list(buyDistr.values())
    distrName = list(rentDistr.keys())
    conclusion = AL.analyse_txt(jobDict[jobArg], cityArg)
    return render_template("analyse.html", rentPer=rentPer, buyPer=buyPer, wbx=wbx, buyDistr=buyDistr,
                           buyPrice=buyPrice, rentPrice=rentPrice, rentDistr=rentDistr, Map=Map, distrName=distrName,
                           conclusion=conclusion
                           )

# ==================================================  在这里启动
if __name__ == '__main__':
    app.run(debug=True, port=8000)















