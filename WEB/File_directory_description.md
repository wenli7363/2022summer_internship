# 文件目录说明
## app.py是整个项目的入口
+ .idea文件是pycharm虚拟环境配置文件
+ chartpy文件是后端数据库的查询接口函数
+ static文件用来存放一些样式和资源文件
    1. CSS文件是页面的样式
    2. images是图片资源文件
    3. js文件是用echarts绘图的脚本文件
+ templates是页面的HTML文件
+ HouseAndSalary.db是项目的数据库

===========================================================================
## 文件目录如下

```
C:.
│  .DS_Store
│  app.py                   =======》系统启动器
│  HouseAndSalary.db
│  identifier.sqlite
│  源码必读.md
│
├─.idea                  ==========》pycharm虚拟环境配置
│  │  .gitignore
│  │  .name
│  │  dataSources.local.xml
│  │  dataSources.xml
│  │  flaskProject.iml
│  │  misc.xml
│  │  modules.xml
│  │  sqldialects.xml
│  │  vcs.xml
│  │  workspace.xml
│  │
│  └─inspectionProfiles
│          profiles_settings.xml
│
├─chartpy               ========》后端的查询接口
│  │  analyse.py
│  │  avg_salary_num.py
│  │  CityAnalyse.py
│  │  city_rate.py
│  │  get_all_salary.py
│  │  search_db.py
│  │  vary_num.py
│  │  __init__.py
│  │
│  └─__pycache__
│
│
├─static                    =====================》样式等资源文件
│  ├─css                    =====================》样式文件
│  │      analyse.css
│  │      analyse.less
│  │      index.css
│  │      index.less
│  │
│  ├─images                              ======》图片文件
│  │      bg.jpg
│  │      head_bg.png
│  │      jt.png
│  │      lbx.png
│  │      line.png
│  │      map.png
│  │      weather.png
│  │
│  └─js            ================》js文件，都是绘图的   
|      |           ===============》index.html用到的   
│      │  china.js
│      │  china_map.js
│      │  echarts.min.js
│      │  ec_left1.js
│      │  ec_left2.js
│      │  ec_left3.js
│      │  ec_right1.js
│      │  ec_right2.js
│      │  ec_right3.js
│      │  flexible.js
│      │  index.js
│      │  jquery.js
│      │
│      └─analyse   ==============》analyse.html用到的
│              al_cl1.js
│              al_cl2.js
│              al_cr2.js
│              al_left1.js
│              al_left2.js
│              al_right1.js
│              al_right2.js
│
├─templates                 ==========》html文件
│      analyse.html
│      debug.log
│      index.html
│
└─__pycache__               ======》python解释器生成的编译文件
```







