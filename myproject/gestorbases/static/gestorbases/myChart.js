
// LISTA DE CORES
var cores = [
    'rgb(0, 99, 132)', 'rgb(255, 99, 132)', 'rgb(255, 99, 0)',
    '#1232B', '#B5C334', '#FCCE10', '#E87C25', '#27727B', '#FE8463', '#9BCA63', '#FAD860', '#F3A43B', '#60C0DD', '#D7504B', '#C6E579', '#F4E001',
    '#F0805A', '#26C0C0',
    'rgba(255,201,47,0.8)', 'rgba(117,121,146,0.8)', 'rgba(255,202,149,0.8)', 'rgba(85,261,39,0.8)', 'rgba(255,621,50,0.8)', 'rgba(255,0,0,0.8)',
    'rgba(46,139,87,0.8)', 'rgba(0,0,205,0.8)', 'rgba(0,100,0,1)', 'rgba(0,255,0,1)', 'rgba(255,0,255,1)', 'rgba(255,69,0,1)',
    'rgba(255,255,0,1)', 'rgba((0,255,127,1)', 'rgba(30,144,255,1)', 'rgba(123,104,238,1)', 'rgba(47,79,79,1)', 'rgba(112,128,144,1)',
    'rgba(178,34,34,1)', 'rgba(147,112,219,1)', 'rgba(138,43,226,1)', 'rgba(148,0,211,1)', 'rgba(205,92,92,1)', 'rgba(25,25,112,1)',
    'rgba(0,0,128,1)', 'rgba(124,252,0,1)', 'rgba(85,107,47,1)', 'rgba((0,191,255,1)', 'rgba(70,130,180,1)', 'rgba(0,255,255,1)',
    'rgba(0,139,139,1)', 'rgba(102,205,170,1)', 'rgba(128,0,0,1)', 'rgba(128,128,0,1)', 'rgba(139,69,19,1)', 'rgba(210,105,30,1)',
    'rgba(152,251,152,1)', 'rgba(169,169,169,1)',
];


// GRÁFICO DE LINHAS
function chartLine(ctx, labels, datasets) {
    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets,
        },

        options: {
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero: true,
                    },
                }],

                yAxes: [{
                    categoryPercentage: 0.7,
                    barPercentage: 0.7,
                }],
            },
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    botton: 10
                }
            }
        }
    });
}



// Executa uma requisição ajax na api restFul em busca dos dados de atualizaçãoes das bases de dados	
function loadData(container, url) {
    var labels = [];
    var qtds = [];
    var datasets = [];

    $.get(url, function (data) {
        for (var i = 0; i < data.atualizacoes.length; i++) {
            labels[i] = data.atualizacoes[i][0];
            qtds[i] = data.atualizacoes[i][1];
        }

        datasets[0] = {
            label: 'Atualizações',
            borderColor: cores[i],
            backgroundColor: 'rgba(0,0,0,0)',
            data: qtds,
        };
        loadChart(container, labels, datasets)
    }, 'json');
};


function loadChart(container, labels, datasets) {
    var ctx = document.getElementById(container).getContext('2d');
    chartLine(ctx, labels, datasets);
}
