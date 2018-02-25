import string

def writeToHTML(room, data):
    l = ['Classroom_1_B002','Classroom_2_B052','Classroom_3_B048',
                    'Classroom_4_B044','Classroom_5_B040','Classroom_6_B032',
                    'Classroom_7_B028','Classroom_8_B024','Classroom_10_B016',
                    'Classroom_3056','Colloquium_3070','Conference_3131',
                    'Conference_A1000','Conference_B1034','Nelson_Auditorium',
                    'Patio','Tamkin_F108','Tamkin_F110','Tamkin_F114',
                    'Telemedicine_Theater_B001','UCIMC_B22A_Room_2112_',
                    'Med_Surge_II_Multi-Labs_A_B_C']
    roomList = ['Classrom 1', 'Classrom 2', 'Classrom 3', 'Classrom 4',
                    'Classrom 5', 'Classrom 6', 'Classrom 7', 'Classrom 8',
                    'Classrom 10', 'Classrom 3056', 'Colloquium 3070',
                    'Conference 3131','Conference A1000','Conference B1034',
                    'Nelson Auditorium','Patio','Tamkin F108','Tamkin F110',
                    'Tamkin F114','Telemedicine_Theater','UCIMC Room 2112',
                    'Med Surge II']
    img = '<img src="src/gif.gif" alt="Have a Good Day!" class="center">' if not bool(data) else ''
    fileName = room + '.html'
    roomName = ''
    for i,r in enumerate(l):
        if room == r:
            roomName = roomList[i]
            break

    html_str = '''<!DOCTYPE HTML>
        <html lang='eng'>

        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <meta name='description' content='EMS Schedule'>
            <meta name='author' content='MedEdIT'>
            <meta name='keywords' content='EMS Schedule Display'>
            <meta http-equiv="refresh" content="600">
            
            <title>EMS Schedule</title>

            <link rel='stylesheet' href='src/style.css' type='text/css'>

            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

            <script src="https://cdnjs.cloudflare.com/ajax/libs/json2html/1.0.0/json2html.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.json2html/1.0.0/jquery.json2html.min.js"></script>
            <script src="src/script.js" type="text/javascript"></script>    
            <link href='http://fonts.googleapis.com/css?family=Great+Vibes' rel='stylesheet' type='text/css'>
			
            <nav>
                <div id="logo"> <img src="src/UCI-School-of-Medicine.jpg" alt="UCI MEDED"></div>
                <div id="room-name">{0}</div>
                <div id="date">Wed Feb 21 2018</div>
            </nav>
            <script>
                var t = {{
                    "item": [{{
                        "<>": "div",
                        "class": "row",
                        "html": [{{
                                "<>": "div",
                                "class": "col-time",
                                "html": [{{
                                        "<>": "div",
                                        "class": "start-time",
                                        "html": "${{startTime}}"
                                    }},
                                    {{
                                        "<>": "div",
                                        "class": "end-time",
                                        "html": "${{endTime}}"
                                    }}
                                ]
                            }},
                            {{
                                "<>": "div",
                                "class": "col-info row-event",
                                "html": "${{eventName}}"
                            }}
                        ]
                    }}]
                }};

                var main = {{
                    "list": {{
                        "<>": "div",
                        "id": "container",
                        "html": function() {{ 
                            return (json2html.transform(d, t.item))
                        }}
                    }}
                }};

                var d = {1};

                document.write(json2html.transform({{}}, main.list));
            </script>

        </head>

        <body>
            {2}
        </body>

        </html>'''.format(roomName, data, img)

    html_file = open(fileName, 'w')
    html_file.write(html_str)
    html_file.close()

