$(document).ready(function () {
    var l = ['Classroom_1_B002', 'Classroom_2_B052', 'Classroom_3_B048',
        'Classroom_4_B044', 'Classroom_5_B040', 'Classroom_6_B032',
        'Classroom_7_B028', 'Classroom_8_B024', 'Classroom_10_B016',
        'Classroom_3056', 'Colloquium_3070', 'Conference_3131',
        'Conference_A1000', 'Conference_B1034', 'Nelson_Auditorium',
        'Patio', 'Tamkin_F108', 'Tamkin_F110', 'Tamkin_F114',
        'Telemedicine_Theater_B001', 'UCIMC_B22A_Room_2112_',
        'Med_Surge_II_Multi-Labs_A_B_C'
    ];
    var roomList = ['Classroom 1', 'Classroom 2', 'Classroom 3', 'Classroom 4',
        'Classroom 5', 'Classroom 6', 'Classroom 7', 'Classroom 8',
        'Classroom 10', 'Classroom 3056', 'Colloquium 3070',
        'Conference 3131', 'Conference A1000', 'Conference B1034',
        'Nelson Auditorium', 'Patio', 'Tamkin F108', 'Tamkin F110',
        'Tamkin F114', 'Telemedicine Theater', 'UCIMC Room 2112',
        'Med Surge II'
    ];


    var link = 'https://itgmededservice.github.io/';
    var extension = '';

    for (var i = 0; i < l.length; ++i) {
        extension = l[i];
        $('ul').append('<li><a href=' + (link + extension) + '>' + roomList[i] + '</a></li>')
    }
});

