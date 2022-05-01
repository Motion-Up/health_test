$(function () {
    $("#chart").shieldChart({
    theme: "light",
    primaryHeader: {
    text: "{{ test.title }}"
    },
    exportOptions: {
    image: false,
    print: false
    },
    axisX: {
    categoricalValues: {{ day|safe }}
    },
    axisY: [{
    min: {{ min }},
    max: {{ max }},
    title: {
    text: 'График результатов {{ test.title }}',
    style: {
    color: '#4DB0F5'
    }
    },
    axisTickText: {
    style: {
    color: '#4DB0F5'
    }
    }
    }],
    dataSeries: [{
    seriesType: 'line',
    axis: 1,
    collectionAlias: "Результат",
    data: {{ results }}
   
    }]
    });
    });