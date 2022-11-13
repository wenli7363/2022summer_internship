//right3：右侧第3个图
//全国岗位数据采集量
//由陈季烨完成绘图，曾培益填补数据
function ec_right3() {
    //输入一个字典 [{ value: 1048, name: '华中' },]
    var myChart = echarts.init(document.querySelector('.pine2 .chart'))
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
                name: '七大区待租房数量',
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
                },
                data: [
                    {value: 49834, name: '东北'},
                    {value: 79812, name: '华东'},
                    {value: 110848, name: '华中'},
                    {value: 112440, name: '华北'},
                    {value: 53718, name: '华南'},
                    {value: 60914, name: '西北'},
                    {value: 102678, name: '西南'}
                ]
            }
        ]
    };
    
      myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
    }