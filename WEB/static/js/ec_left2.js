//left2:左侧第2个图
// 4到6月各个岗位的需求量图
//由陈季烨完成绘图，曾培益填补数据
function ec_left2(kf_value,qd_value,sf_value,cs_value) {
    //参数均为list类型
    var myChart = echarts.init(document.querySelector('.line .chart'));
    var app = {}

    app.config = {
        rotate: 90,
        align: 'left',
        verticalAlign: 'middle',
        position: 'insideBottom',
        distance: 15,
    };
    const labelOption = {
        show: true,
        position: app.config.position,
        distance: app.config.distance,
        align: app.config.align,
        verticalAlign: app.config.verticalAlign,
        rotate: app.config.rotate,
        formatter: '{c}',
        fontSize: 15,
        rich: {
            name: {}
        }
    };
    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['开发', '前端', '算法', '测试'],
            top:'top',
            textStyle: {
                color: "rgba(255, 255, 255, 1)"
            }
        },
        toolbox: {
        },
        xAxis: [
            {
                type: 'category',
                axisTick: { show: false },
                data: ['4月', '5月', '6月'],
                axisLabel: {
                    color: "rgba(255, 255, 255, 1)"
                }
            },

        ],
        yAxis: [
            {
                name: '数量(千个)',
                nameRotate: '0.1',
                nameTextStyle: {color: '#FFF'},
                type: 'value',
                axisLabel: {
                    color: "rgba(255, 255, 255, 1)"
                },
                splitNumber: 5, //段数是4
                min: 0, //最小是0
                max: 1.41
            }
        ],
        series: [
            {
                name: '开发',
                type: 'bar',
                barGap: 0,
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: kf_value
            },
            {
                name: '前端',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: qd_value,
                color: '#EECFA1'
            },
            {
                name: '算法',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: sf_value,
                color: '#F4A460'
            },
            {
                name: '测试',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: cs_value,
                color: '#9ACD32'
            }
        ]
    };

    myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}