//left2 租房价格分布图
//由陈季烨完成绘图，曾培益填补数据
function sz_left2(rentDistr,cityMap) {
    var data = rentDistr;
    console.log(rentDistr);
    var mychart = echarts.init(document.querySelector(".pie .chart"));
    //导入阿里云可视化平台热力图api
    $.get('https://geo.datav.aliyun.com/areas_v3/bound/geojson?code=' + cityMap[0] + '_full', function (ret) {
        echarts.registerMap('chinaMap', ret);
        var option = {
            tooltip: {
                trigger: 'item',
            },
            geo: {
                type: 'map',
                map: 'chinaMap', // chinaMap需要和registerMap中的第一个参数保持一致
                roam: true, // 设置允许缩放以及拖动的效果
				label: {
					show: true // 展示标签
				},
				zoom: 1, // 设置初始化的缩放比例
				center: cityMap[1] // 设置地图中心点的坐标
			},
			series: [{
				name:'价格(元/月)',
				data: data,
				geoIndex: 0, // 将数据和第0个geo配置关联在一起
				type: 'map'
			}
			],

			visualMap: {
                min: 1000,
                max: 8000,
                inRange: {
                    color: ['#FFE4B5', 'red'] // 控制颜色渐变的范围
                },
                calculable: true,// 出现滑块
                seriesIndex: 0 // 仅使第一个series生效
            }

		}
		mychart.setOption(option);
      window.addEventListener("resize", function() {
          myChart.resize();
      })
	});

}
