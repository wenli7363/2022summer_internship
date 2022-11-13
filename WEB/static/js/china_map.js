//主页面中国地图
//由陈季烨完成绘图，曾培益填补数据
function china_map(chinaMap) {
	var data = chinaMap;		//用来从数据库中调用城市薪资数据
//geoCoordMap设置经纬坐标
	var geoCoordMap = {
		合肥: [117.27, 31.86],
		西安: [108.95, 34.27],
		济南: [117, 36.65],
		哈尔滨: [126.63, 45.75],
		大连: [121.62, 38.92],
		青岛: [120.33, 36.07],
		天津: [117.2, 39.13],
		南昌: [115.89, 28.68],
		厦门: [118.1, 24.46],
		上海: [121.48, 31.22],
		海口: [110.206424, 20.050057],
		乌鲁木齐: [87.623314, 43.832806],
		贵阳: [106.636816, 26.652747],
		南京: [118.802891, 32.064735],
		石家庄: [114.520828, 38.048684],
		宁波: [121.556686, 29.880177],
		成都: [104.071216, 30.576279],
		长春: [125.33017, 43.82178],
		深圳: [114.066112, 22.548515],
		沈阳: [123.438973, 41.811339],
		北京: [116.413554, 39.911013],
		杭州: [120.161693, 30.280059],
		南宁: [108.373351, 22.823037],
		苏州: [120.589613, 31.304566],
		兰州: [103.840692, 36.067312],
		郑州: [113.631349, 34.753488],
		武汉: [114.311831, 30.598428],
		昆明: [102.839667, 24.885953],
		福州: [119.302938, 26.080447],
		长沙: [112.945333, 28.233971],
		广州: [113.270793, 23.135308],
		呼和浩特: [111.758518, 40.847461],
		重庆: [106.557165, 29.570997],
		太原: [112.55706, 37.876885]
	};

// ConvertData函数，将数据集重组为字典元素，返回一个列表
	var convertData = function (data) {
		var res = []; //res是个以dict为元素的字典集
		for (var i = 0; i < data.length; i++) {
			var geoCoord = geoCoordMap[data[i].name];
			if (geoCoord) {
				res.push({
					name: data[i].name,
					value: geoCoord.concat(data[i].value)
				});
			}
		}
		return res;
	};


	//利用echarts直接绘制中国地图
	var ec_center = echarts.init(document.querySelector('.map'));
	var optionMap = {
		title: {
			text: '全国IT行业薪资分布图',
			textStyle: {
				color: 'white'
			},
			x: 'center'
		},
		tooltip: {
			trigger: 'item',
			"formatter": (p) => {//自定义提示信息
				let dataCon = p.data;
				txtCon = dataCon.name + '<br>月薪:' + dataCon.value[2] + '(K/月)';
				return txtCon;
			}
		},
		//左侧小导航图标
		visualMap: {
			min: 5,
			max: 22,
			splitNumber: 5,
			show: true,
			x: 'left',
			y: 'bottom',
			textStyle: {
				fontSize: 12,
				color: "rgba(255, 255, 255, 1)"
			},
			color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
		},
		//中国地图依赖geo属性
		geo: {
			map: 'china',
			roam: true,
			zoom: 1.3,
			label: {
				emphasis: {
					show: false
				}
			},
			itemStyle: {
				//每个省份未选中时的样式
				normal: {
					areaColor: '#698B69',
					borderColor: '#111'
				},
				//省份选中的样式
				emphasis: {
					areaColor: '#2a333d'
				}
			}
		},
		//配置属性
		series: [
			{
				name: '城市散点',
				type: "scatter",
				coordinateSystem: 'geo',
				data: convertData(data),
				symbolSize: 12,
				label: {
					show: true,
					formatter: "{b}",
					offset: [0, -20],	//文字的相对偏移
					color: 'white'
				},
				emphasis: {
					label: {
						show: true,
						formatter: "{b}",
						offset: [0, -20],
						color: "red",
						fontSize: 18,
					},
				},
			}]
	};

	//使用制定的配置项和数据显示图表
	ec_center.setOption(optionMap);
}