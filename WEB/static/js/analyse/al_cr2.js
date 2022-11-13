//center right 2房价对比图
//由陈季烨完成绘图，曾培益填补数据
function sz_cr2(rentPrice,buyPrice,distrName) {
    var myChart = echarts.init(document.querySelector('.center2 .chart'));
    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                crossStyle: {
                    color: '#999'
                }
            }
        },
        toolbox: {
            feature: {
                dataView: { show: true, readOnly: false },
                magicType: { show: true, type: ['line', 'bar'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        xAxis: [
            {
                type: 'category',
                //////////////////////////////////////////////////////////////////data放几个区的名字
                data: distrName,
                axisPointer: {
                    type: 'shadow'
                },
                axisLabel: {
                    color: "rgba(255, 255, 255, 1)"
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: '租房价格',
                nameTextStyle:{color: "rgba(255, 255, 255, 1)"},
                axisLabel: {
                    formatter: '{value} ',
                    color: "rgba(255, 255, 255, 1)",
                    interval: 0,//横轴信息全部显示
                    rotate: 60, //倾斜度 -90 至 90 默认为0
                    margin: 0, //刻度标签与轴线之间的距离
                }
            },
            {
                type: 'value',
                name: '买房价格',
                nameTextStyle:{color: "rgba(255, 255, 255, 1)"},
                axisLabel: {
                    formatter: '{value} ',
                    color: "rgba(255, 255, 255, 1)",
                    interval: 0,//横轴信息全部显示
                    rotate: -60, //倾斜度 -90 至 90 默认为0
                    margin: 0, //刻度标签与轴线之间的距离
                }
            }
        ],
        series: [
            {
                name: '租房价格',
                type: 'bar',
                itemStyle:{
                    normal:{color:'aqua'}
                },
                tooltip: {
                    valueFormatter: function (value) {
                        return value + '元/月';
                    }
                },
                data: rentPrice
            },
            {
                name: '买房价格',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 元/平';
                    }
                },
                data: buyPrice
            }
        ]
    };

    myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}