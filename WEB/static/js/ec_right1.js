//right1：右侧第一个图
//四大城市数据对比
//由陈季烨完成绘图，曾培益填补数据
function ec_right1(bj,gz,sz,sh) {
    //直接输入数据集
    var bj=[320, 302, 301]
    var sh=[120, 132, 101]
    var sz=[150, 212, 201]
    var gz=[220, 182, 191]
    var myChart = echarts.init(document.querySelector('.bar2 .chart'))
    var option;
    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
            }
        },
        legend: {
            textStyle: {
                color: "rgba(255, 255, 255, 1)",
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            axisLabel: {
                color: "rgba(255, 255, 255, 1)"
            }
        },
        yAxis: {
            type: 'category',
            data: ['购房价(元)', '人均工资(元)', '租房价格(元)'],
            axisLabel: {
                color: "rgba(255, 255, 255, 1)"
            }
        },
        series: [
            {
                name: '北京',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: bj
            },
            {
                name: '上海',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: sh
            },
            {
                name: '广州',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: gz
            },
            {
                name: '深圳',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: sz
            }
        ]
    };
    myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}