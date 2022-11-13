//right2：右侧第2个图
// 七大区房价对比
//由陈季烨完成绘图，曾培益填补数据
function ec_right2(buy_list,rent_list) {
    //输入两个列表，顺序为['东北', '华东', '华中','华北','华南','西北','西南']
    var myChart = echarts.init(document.querySelector('.line2 .chart'));
    var app = {};

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
            data: ['买房', '租房'],
            top: 'top',
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
                data: ['东北', '华东', '华中','华北','华南','西北','西南'],
                axisLabel: {
                    color: "rgba(255, 255, 255, 1)",

            },}

        ],
        yAxis: [
            {
                type: 'value',
                name: '价格(元/月 或 元/m²)',
                nameRotate: '0.1',
                nameTextStyle:{ color:'#FFF' },
                axisLabel: {
                    color: "rgba(255, 255, 255, 1)",
                    interval: 0,//横轴信息全部显示
                    rotate: 45, //倾斜度 -90 至 90 默认为0
                    margin: 5, //刻度标签与轴线之间的距离
                }
            }
        ],
        series: [
            {
                name: '买房',
                type: 'bar',
                barGap: 1,
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: buy_list
            },
            {
                name: '租房',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: rent_list,
                color: '#FFE4B5'
            }
        ]
    };

    myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}