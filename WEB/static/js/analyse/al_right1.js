//right1 市场在售房屋数量比
//由陈季烨完成绘图，曾培益填补数据
function sz_right1(buyPercent){
    var myChart = echarts.init(document.querySelector('.bar2 .chart'));
    var option = {
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
      },
        legend: {
            textStyle: {
                color: "rgba(255, 255, 255, 1)"
            },
            type:'scroll',
            bottom:10,
            left:5
        },
        series: [
          {
            name: '待售房屋数量',
            type: 'pie',
            radius: [15, 100],
            center: ['50%', '40%'],
            roseType: 'area',
            itemStyle: {
              borderRadius: 2
            },
            
            data: buyPercent
          }
        ]
      };

      myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}