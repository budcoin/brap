Highcharts.chart('container', {
    data: {
        table: 'datatable'
    },
    chart: {
        type: 'line'
    },
    title: {
        text: 'Session Data'
    },
    yAxis: {
        allowDecimals: true,
        title: {
            text: ''
        }
    }
});
