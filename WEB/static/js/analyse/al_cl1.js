//cl1:中间左边第一个图
//五边形图分析
//由陈季烨完成绘图，曾培益填补数据
function sz_cl1(wbx){
    var myChart = echarts.init(document.querySelector('.analysis1 .chart'));
    var option = {
        tooltip:{
          show:true,
          trigger:'item'
        },
        legend: {
          data: ['Actual Spending']
        },
        radar: {
          // shape: 'circle',
          indicator: [
            { name: '购房成本', max: 1 },
            { name: '租房成本', max: 1 },
            { name: '薪资水平', max: 1 },
            { name: '就业机会', max: 1 },
            { name: '居住面积', max: 1 }
          ]
        },
        series: [
          {
            name: '综合分析',
            type: 'radar',
            data: [
              {
                value: wbx,
                name: ''
              }
            ]
          }
        ]
      };

      myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}