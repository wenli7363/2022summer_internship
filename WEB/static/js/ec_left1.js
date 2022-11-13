// left1左图柱状图绘制（left1指左侧第一幅图）
//由陈季烨完成绘图，曾培益填补数据
function ec_left1(value1,value2) {
	var myChart = echarts.init(document.querySelector('.bar .chart'));
	//参数均为list类型
	//指定配置项Option
	var option = {
		title: {
			text: "",
		},
		tooltip: {
			trigger: 'axis',
			axisPointer: {
				type: 'shadow'
			}
		},
		legend: {
			right: "0%",
			textStyle: {
				color: "rgba(255, 255, 255, 1)"
			},
		},
		grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
		},
		xAxis: [{
            name: '平均月薪(千元)',
            nameRotate: '0.1',
            nameTextStyle: {color: '#FFF'},
            type: 'value',
            boundaryGap: [0, 0.01],
            axisLabel: {
                color: "rgba(255, 255, 255, 1)",
                show: true,
                interval: 0,
            },
        },
			{
                name: '岗位数(千个)',
                nameRotate: '0.1',
                nameTextStyle:{ color:'#FFF' },
			type: 'value',
			boundaryGap: [0, 0.01],
			axisLabel: {
				color: "rgba(255, 255, 255, 1)"
			}}],
		yAxis: {
			type: 'category',
			data: ['算法', '测试', '前端', '开发'],
			axisLabel: {
				color: "rgba(255, 255, 255, 1)"
			}
		},
		series: [{
            name: '平均月薪(千元)',
            type: 'bar',
            data: value1,
        },
			{
				name: '岗位数(千个)',
				type: 'bar',
				data: value2,
				xAxisIndex:1,
				color:'#FFE4B5'
			}
		]
	};

	myChart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
}
