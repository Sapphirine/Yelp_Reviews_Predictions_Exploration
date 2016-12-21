/// <reference types="angular" />
/// <reference types="ngMap" />
/// <reference path="../../typings/index.d.ts" />
/// <reference path="./services.ts" />
var MapCtrl = (function () {
    function MapCtrl(_scope, _httpSvc) {
        this._scope = _scope;
        this._httpSvc = _httpSvc;
        _httpSvc.get('/restaurants', function (r) {
            _scope.markers = r.data;
        }, null);
        _scope.showDetail = function (event) {
            window.location.href = '/#!/' + this.id.toString();
        };
    }
    return MapCtrl;
}());
MapCtrl.$inject = ['$scope', 'HttpService'];
function liquidFillGaugeDefaultSettings(value) {
    return {
        minValue: 0,
        maxValue: 100,
        circleThickness: 0.15,
        circleFillGap: 0.05,
        circleColor: value < 50 ? "#FF7777" : '#808015',
        waveHeight: 0.1,
        waveCount: 1,
        waveRiseTime: 800,
        waveAnimateTime: 2000,
        waveRise: true,
        waveHeightScaling: true,
        waveAnimate: true,
        waveColor: value < 50 ? "#FFDDDD" : '#AAAA39',
        waveOffset: 0,
        textVertPosition: .5,
        textSize: 1,
        valueCountUp: true,
        displayPercent: true,
        textColor: value < 50 ? "#FF4444" : '#555500',
        waveTextColor: value < 50 ? "#FFAAAA" : '#FFFFAA' // The color of the value text when the wave overlaps it.
    };
}
function loadLiquidFillGauge(elementId, name, value, config) {
    if (config == null)
        config = this.liquidFillGaugeDefaultSettings(value);
    var gauge = d3.select("#" + elementId);
    var radius = Math.min(parseInt(gauge.style("width")), parseInt(gauge.style("height"))) / 2;
    var locationX = parseInt(gauge.style("width")) / 2 - radius;
    var locationY = parseInt(gauge.style("height")) / 2 - radius;
    var fillPercent = Math.max(config.minValue, Math.min(config.maxValue, value)) / config.maxValue;
    var waveHeightScale;
    if (config.waveHeightScaling) {
        waveHeightScale = d3.scale.linear()
            .range([0, config.waveHeight, 0])
            .domain([0, 50, 100]);
    }
    else {
        waveHeightScale = d3.scale.linear()
            .range([config.waveHeight, config.waveHeight])
            .domain([0, 100]);
    }
    var textPixels = (config.textSize * radius / 2);
    var textFinalValue = parseFloat(value).toFixed(2);
    var textStartValue = config.valueCountUp ? config.minValue : textFinalValue;
    var percentText = config.displayPercent ? "%" : "";
    var circleThickness = config.circleThickness * radius;
    var circleFillGap = config.circleFillGap * radius;
    var fillCircleMargin = circleThickness + circleFillGap;
    var fillCircleRadius = radius - fillCircleMargin;
    var waveHeight = fillCircleRadius * waveHeightScale(fillPercent * 100);
    var waveLength = fillCircleRadius * 2 / config.waveCount;
    var waveClipCount = 1 + config.waveCount;
    var waveClipWidth = waveLength * waveClipCount;
    // Data for building the clip wave area.
    var data = [];
    for (var i = 0; i <= 40 * waveClipCount; i++) {
        data.push({ x: i / (40 * waveClipCount), y: (i / (40)) });
    }
    // Scales for drawing the outer circle.
    var gaugeCircleX = d3.scale.linear().range([0, 2 * Math.PI]).domain([0, 1]);
    var gaugeCircleY = d3.scale.linear().range([0, radius]).domain([0, radius]);
    // Scales for controlling the size of the clipping path.
    var waveScaleX = d3.scale.linear().range([0, waveClipWidth]).domain([0, 1]);
    var waveScaleY = d3.scale.linear().range([0, waveHeight]).domain([0, 1]);
    // Scales for controlling the position of the clipping path.
    var waveRiseScale = d3.scale.linear()
        .range([(fillCircleMargin + fillCircleRadius * 2 + waveHeight), (fillCircleMargin - waveHeight)])
        .domain([0, 1]);
    var waveAnimateScale = d3.scale.linear()
        .range([0, waveClipWidth - fillCircleRadius * 2]) // Push the clip area one full wave then snap back.
        .domain([0, 1]);
    // Scale for controlling the position of the text within the gauge.
    var textRiseScaleY = d3.scale.linear()
        .range([fillCircleMargin + fillCircleRadius * 2, (fillCircleMargin + textPixels * 0.7)])
        .domain([0, 1]);
    // Center the gauge within the parent SVG.
    var gaugeGroup = gauge.append("g")
        .attr('transform', 'translate(' + locationX + ',' + locationY + ')');
    // Draw the outer circle.
    var gaugeCircleArc = d3.svg.arc()
        .startAngle(gaugeCircleX(0))
        .endAngle(gaugeCircleX(1))
        .outerRadius(gaugeCircleY(radius))
        .innerRadius(gaugeCircleY(radius - circleThickness));
    gaugeGroup.append("path")
        .attr("d", gaugeCircleArc)
        .style("fill", config.circleColor)
        .attr('transform', 'translate(' + radius + ',' + radius + ')');
    // Text where the wave does not overlap.
    var text1 = gaugeGroup.append("text")
        .text(name)
        .attr("class", "liquidFillGaugeText")
        .attr("text-anchor", "middle")
        .attr("font-size", textPixels + "px")
        .style("fill", config.textColor)
        .attr('transform', 'translate(' + radius + ',' + textRiseScaleY(config.textVertPosition) + ')');
    // The clipping wave area.
    var clipArea = d3.svg.area()
        .x(function (d) { return waveScaleX(d.x); })
        .y0(function (d) { return waveScaleY(Math.sin(Math.PI * 2 * config.waveOffset * -1 + Math.PI * 2 * (1 - config.waveCount) + d.y * 2 * Math.PI)); })
        .y1(function (d) { return (fillCircleRadius * 2 + waveHeight); });
    var waveGroup = gaugeGroup.append("defs")
        .append("clipPath")
        .attr("id", "clipWave" + elementId);
    var wave = waveGroup.append("path")
        .datum(data)
        .attr("d", clipArea)
        .attr("T", 0);
    // The inner circle with the clipping wave attached.
    var fillCircleGroup = gaugeGroup.append("g")
        .attr("clip-path", "url(#clipWave" + elementId + ")");
    fillCircleGroup.append("circle")
        .attr("cx", radius)
        .attr("cy", radius)
        .attr("r", fillCircleRadius)
        .style("fill", config.waveColor);
    // Text where the wave does overlap.
    var text2 = fillCircleGroup.append("text")
        .text(name)
        .attr("class", "liquidFillGaugeText")
        .attr("text-anchor", "middle")
        .attr("font-size", textPixels + "px")
        .style("fill", config.waveTextColor)
        .attr('transform', 'translate(' + radius + ',' + textRiseScaleY(config.textVertPosition) + ')');
    // Make the wave rise. wave and waveGroup are separate so that horizontal and vertical movement can be controlled independently.
    var waveGroupXPosition = fillCircleMargin + fillCircleRadius * 2 - waveClipWidth;
    if (config.waveRise) {
        waveGroup.attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(0) + ')')
            .transition()
            .duration(config.waveRiseTime)
            .attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(fillPercent) + ')')
            .each("start", function () { wave.attr('transform', 'translate(1,0)'); }); // This transform is necessary to get the clip wave positioned correctly when waveRise=true and waveAnimate=false. The wave will not position correctly without this, but it's not clear why this is actually necessary.
    }
    else {
        waveGroup.attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(fillPercent) + ')');
    }
    if (config.waveAnimate)
        animateWave();
    function animateWave() {
        wave.attr('transform', 'translate(' + waveAnimateScale(wave.attr('T')) + ',0)');
        wave.transition()
            .duration(config.waveAnimateTime * (1 - wave.attr('T')))
            .ease('linear')
            .attr('transform', 'translate(' + waveAnimateScale(1) + ',0)')
            .attr('T', 1)
            .each('end', function () {
            wave.attr('T', 0);
            animateWave(config.waveAnimateTime);
        });
    }
}
function floatingTooltip(tooltipId, width) {
    var tt = d3.select('body')
        .append('div')
        .attr('class', 'tooltip')
        .attr('id', tooltipId)
        .style('pointer-events', 'none');
    if (width) {
        tt.style('width', width);
    }
    hideTooltip();
    function showTooltip(content, event) {
        tt.style('opacity', 0.85)
            .html(content);
        updatePosition(event);
    }
    function hideTooltip() {
        tt.style('opacity', 0.0);
    }
    function updatePosition(event) {
        var xOffset = 20;
        var yOffset = 10;
        var ttw = tt.style('width');
        var tth = tt.style('height');
        var wscrY = window.scrollY;
        var wscrX = window.scrollX;
        var curX = (document.all) ? event.clientX + wscrX : event.pageX;
        var curY = (document.all) ? event.clientY + wscrY : event.pageY;
        var ttleft = ((curX - wscrX + xOffset * 2 + ttw) > window.innerWidth) ?
            curX - ttw - xOffset * 2 : curX + xOffset;
        if (ttleft < wscrX + xOffset) {
            ttleft = wscrX + xOffset;
        }
        var tttop = ((curY - wscrY + yOffset * 2 + tth) > window.innerHeight) ?
            curY - tth - yOffset * 2 : curY + yOffset;
        if (tttop < wscrY + yOffset) {
            tttop = curY + yOffset;
        }
        tt.style({ top: tttop + 'px', left: ttleft + 'px' });
    }
    return {
        showTooltip: showTooltip,
        hideTooltip: hideTooltip,
        updatePosition: updatePosition
    };
}
function bubbleChart() {
    var width = window.innerWidth;
    var height = window.innerHeight;
    var tooltip = floatingTooltip('gates_tooltip', 240);
    var center = { x: width / 2, y: height / 2 };
    var damper = 0.04;
    var svg = null;
    var bubbles = null;
    var texts = null;
    var grads = null;
    var nodes = [];
    function charge(d) {
        return -Math.pow(d.radius, 2.0) / 8;
    }
    var force = d3.layout.force()
        .size([width, height])
        .charge(charge)
        .gravity(-0.01)
        .friction(0.9);
    var radiusScale = d3.scale.pow()
        .exponent(0.5)
        .range([2, 85]);
    function createNodes(rawData) {
        var myNodes = [];
        rawData.forEach(function (d) {
            myNodes.push({
                id: d.id,
                count: d.count,
                radius: radiusScale(+d.count),
                positive: d.positive,
                negative: d.negative,
                name: d.name,
                x: Math.random() * 900,
                y: Math.random() * 800
            });
        });
        myNodes.sort(function (a, b) { return b.value - a.value; });
        return myNodes;
    }
    function getColor(d) {
        if (d.positive >= 50) {
            return '#66ff33';
        }
        else {
            return '#ff5050';
        }
    }
    var chart = function chart(selector, rawData) {
        radiusScale.domain(d3.extent(rawData, function (d) { return d.count; }))
            .range([20, 90]);
        nodes = createNodes(rawData);
        force.nodes(nodes);
        svg = d3.select(selector)
            .append('svg')
            .attr('width', width)
            .attr('height', height);
        grads = svg.selectAll('.grad')
            .data(nodes, function (d) { return d.id; });
        var g = grads.enter().append("svg:defs")
            .classed('grad', true)
            .append("svg:linearGradient")
            .attr("id", function (d) { return 'G' + d.id; })
            .attr("x1", "0%")
            .attr("y1", "0%")
            .attr("x2", "0%")
            .attr("y2", "100%")
            .attr("spreadMethod", "pad");
        g.append("svg:stop")
            .attr("offset", function (d) { return d.positive + '%'; })
            .attr("stop-color", "#ccff99")
            .attr("stop-opacity", 1);
        g.append("svg:stop")
            .attr("offset", function (d) { return d.positive + '%'; })
            .attr("stop-color", "#ff9999")
            .attr("stop-opacity", 1);
        bubbles = svg.selectAll('.bubble')
            .data(nodes, function (d) { return d.id; });
        bubbles.enter().append('circle')
            .classed('bubble', true)
            .attr('r', 0)
            .attr('fill', function (d) { return 'url(#G' + d.id + ')'; })
            .attr('stroke', function (d) { return d3.rgb(getColor(d)).darker(); })
            .attr('stroke-width', 2)
            .on('mouseover', showDetail)
            .on('mouseout', hideDetail)
            .on('click', function (d, i) {
            var scope = angular.element('#container').scope();
            scope.showInfo(d);
            scope.$apply();
        });
        bubbles.transition()
            .duration(2000)
            .attr('r', function (d) { return d.radius; });
        texts = svg.selectAll('.text')
            .data(nodes, function (d) { return d.id; });
        texts.enter().append('text')
            .classed('text', true)
            .text(function (d) { return d.name; })
            .attr("text-anchor", "middle");
        groupBubbles();
    };
    function groupBubbles() {
        force.on('tick', function (e) {
            bubbles.each(moveToCenter(e.alpha))
                .attr('cx', function (d) { return d.x; })
                .attr('cy', function (d) { return d.y; });
            texts.each(moveToCenter(e.alpha))
                .attr('dx', function (d) { return d.x; })
                .attr('dy', function (d) { return d.y; });
        });
        force.start();
    }
    function moveTextToCenter(alpha) {
        return function (d) {
            d.x = d.x + (center.x - d.x) * damper * alpha;
            d.y = d.y + (center.y - d.y) * damper * alpha;
        };
    }
    function moveToCenter(alpha) {
        return function (d) {
            d.x = d.x + (center.x - d.x) * damper * alpha;
            d.y = d.y + (center.y - d.y) * damper * alpha;
        };
    }
    function showDetail(d) {
        d3.select(this).attr('stroke', 'black');
        var content = '<span class="name">Text: </span><span class="value">' +
            d.name +
            '</span><br/>' +
            '<span class="name">Count: </span><span class="value">' +
            d.count +
            '</span><br/>' +
            '<span class="name">Positive: </span><span class="value">' +
            d.positive +
            '</span><br/>' +
            '<span class="name">Negative: </span><span class="value">' +
            d.negative +
            '</span>';
        tooltip.showTooltip(content, d3.event);
    }
    function hideDetail(d) {
        tooltip.hideTooltip();
    }
    return chart;
}
function highlight(ele, text, polarity) {
    var innerHTML = ele.innerHTML;
    var reg = new RegExp(text, 'ig');
    if (polarity < 0)
        innerHTML = innerHTML.replace(reg, "<span class='bad'>" + text + "</span>");
    else
        innerHTML = innerHTML.replace(reg, "<span class='good'>" + text + "</span>");
    ele.innerHTML = innerHTML;
}
var DetailCtrl = (function () {
    function DetailCtrl(_scope, _params, _httpSvc) {
        var _this = this;
        this._scope = _scope;
        this._params = _params;
        this._httpSvc = _httpSvc;
        this._replaced = {};
        _httpSvc.get('/restaurants/' + _params.id + '/name', function (r) {
            _scope.restaurant = r.data;
        }, null);
        _httpSvc.get('/restaurants/' + _params.id + '/info', function (r) {
            _scope.items = r.data;
            var myBubbleChart = bubbleChart();
            myBubbleChart('#vis', _scope.items);
            // let scale = d3.scale.linear()
            //     .range([50, 130])
            //     .domain(d3.extent(_scope.items, i => i.count));
            // _scope.items.forEach(i => {
            //     i.style = {
            //         width: scale(i.count) + 'px',
            //         height: scale(i.count) + 'px'
            //     };
            // });
            // angular.element('#bubble')
            //     .ready(() => {
            //         _scope.items.forEach(i => {
            //             loadLiquidFillGauge(i.id, i.name, i.positive, null);
            //         });
            //     });
        }, null);
        _httpSvc.get('/restaurants/' + _params.id + '/reviews', function (r) {
            _scope.reviews = r.data;
        }, null);
        _scope.showInfo = function (i) {
            Object.keys(_this._replaced).forEach(function (k) {
                var ele = document.getElementById(k);
                ele.innerHTML = _this._replaced[k];
            });
            _this._replaced = {};
            _scope.currName = i.name;
            setTimeout(function () {
                _scope.reviews.forEach(function (r) {
                    if (_scope.currName && r.content.toLowerCase().indexOf(_scope.currName.toLowerCase()) >= 0) {
                        var ele = document.getElementById(r.id);
                        _this._replaced[r.id] = ele.innerHTML;
                        highlight(ele, _scope.currName, r.polarity);
                    }
                });
            }, 300);
        };
    }
    return DetailCtrl;
}());
DetailCtrl.$inject = ['$scope', '$routeParams', 'HttpService'];
angular.module('app')
    .controller('MapCtrl', MapCtrl)
    .controller('DetailCtrl', DetailCtrl);

var HttpService = (function () {
    function HttpService(_http) {
        this._http = _http;
        this._urlBase = 'http://localhost:5000';
    }
    HttpService.prototype.init = function (urlBase) {
        if (urlBase.indexOf('/', urlBase.length - '/'.length) !== -1) {
            this._urlBase = urlBase.substr(0, urlBase.length - 1);
        }
        else {
            this._urlBase = urlBase;
        }
    };
    HttpService.prototype.get = function (url, onSuccess, onError) {
        this._http.get(this._urlBase + url)
            .then(onSuccess, onError);
    };
    HttpService.prototype.post = function (url, payload, onSuccess, onError) {
        this._http.post(this._urlBase + url, payload)
            .then(onSuccess, onError);
    };
    return HttpService;
}());
HttpService.$inject = ['$http'];
angular.module('app')
    .service('HttpService', HttpService);
