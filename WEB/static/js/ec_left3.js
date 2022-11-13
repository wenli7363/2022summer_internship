//left3：左侧第3个图
//全国岗位数据采集量
//由陈季烨完成绘图，曾培益填补数据
function ec_left3(){
  //datas是一个字典类型
//   datas = {}
// df = pd.read_csv('data/房源数量占比.csv')
// df = df.sort_values('房源数量分布占比', ascending=False)
//
// for item in df.head(10).values:
//     datas[item[0]] = item[1]
// ————————————————
// 版权声明：本文为CSDN博主「飝鱻.」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
// 原文链接：https://blog.csdn.net/heiren_a/article/details/123471559
var myChart =echarts.init(document.querySelector('.pine .chart'))
var option = {
    tooltip: {
      trigger: 'item'
    },
    legend: {
      top: '1%',
      left: 'center',
      textStyle: {
        color: "rgba(255, 255, 255, 1)"
    }
    },
    series: [
      {
          name: '七大区待售房数量',
          type: 'pie',
          top: '13%',
          radius: ['40%', '70%'],
          avoidLabelOverlap: true,
          label: {
              show: true,
              position: 'inner',
              formatter: '{b}:{c}' + '\n\r' + '({d}%)'

          },
          emphasis: {
              label: {
                  show: true,
                  fontSize: '20',
                  fontWeight: 'bold'
              }
        },
        labelLine: {
          show: false
        }, //这里数据直接输入
        data: [
            {value: 885, name: '东北'},
            {value: 3141, name: '华东'},
            {value: 3688, name: '华中'},
            {value: 2677, name: '华北'},
            {value: 1324, name: '华南'},
            {value: 1530, name: '西北'},
            {value: 4681, name: '西南'}
        ]
      }
    ]
  };

  myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}