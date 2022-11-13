//left 1 市场待租房屋数量比
//由陈季烨完成绘图，曾培益填补数据
function sz_left1(numPer){
    var myChart = echarts.init(document.querySelector('.bar .chart'));
    var option = {
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
      },
        legend: {
            bottom: 'bottom',
            textStyle: {
                color: "rgba(255, 255, 255, 1)"
            },
            type:'scroll',
            bottom:10,
            left:5
        },
        series: [
          {
            name: '市场待租房屋数量',
            type: 'pie',
            radius: [15, 100],
            center: ['50%', '40%'],
            roseType: 'area',
            itemStyle: {
              borderRadius: 2
            },
            data: numPer
          }
        ]
      };

      myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}