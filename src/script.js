//Get current date
$(document).ready(function () {
    var days = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ];

    var months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    var currentdate = new Date();
    var datetime = days[currentdate.getDay()] + ", " +
        months[currentdate.getMonth()] + " " + currentdate.getDate() + ", " +
        currentdate.getFullYear();
    $('#date').text(datetime)
});

//Highlight
$(document).ready(function () {
    //Convert time to minute -> easier to compare
    function timeToMinute(str) {

        var hour = parseInt(str.substring(0, str.search(":")));
        var minute = parseInt(str.substring(str.search(":") + 1, str.search(" ")));
        var ampm = str.substring(str.search(" ") + 1, str.length);
        var offset = ampm == "AM" || (hour == 12 && ampm == "PM") ? 0 : 12;

        return (hour + offset) * 60 + minute;
    };

    var check = false;
    var i = 0;

    var dt = new Date();
    var hour = dt.getHours();
    var minute = dt.getMinutes();
    var time = (hour == 0 ? 24 : hour) * 60 + minute; //time in minute

    //Get list of all elements have class = "row"
    var l = document.getElementsByClassName("row");
    var len = l.length;

    //Not empy
    if (len > 0) {
        //Case 1 booking
        if (len == 1 && (time >= timeToMinute((l[0].querySelector(".col-time .start-time")).textContent)) &&
            time <= timeToMinute((l[0].querySelector(".col-time .end-time")).textContent))
            check = true;
        else {
     
            var stop = false;
            //Loop till find the time needed
            do {
                if (time >= timeToMinute((l[i].querySelector(".col-time .start-time")).textContent))
                    stop = true;
                else
					++i;
            } while (i < len && !stop);

            //first booking of the day
			if (i == 0 && time == timeToMinute((l[i].querySelector(".col-time .start-time")).textContent))
				check = true;
            else if (i > 0){ //not the first booking of the day
                var currStartTime = timeToMinute((l[i].querySelector(".col-time .start-time")).textContent);
                var currEndTime = timeToMinute((l[i].querySelector(".col-time .end-time")).textContent);
                var prevStartTime = timeToMinute((l[i - 1].querySelector(".col-time .start-time")).textContent);
                var prevEndTime = timeToMinute((l[i - 1].querySelector(".col-time .end-time")).textContent);

                if (currStartTime == prevEndTime && time == currStartTime)
                    check = true;
                else if (!(time < currStartTime && time > prevEndTime)) {
                    if (i == len - 1 && time <= currEndTime)
                        check = true;

                    if (time >= prevStartTime && time <= prevEndTime) {
                        --i;
                        check = true;
                    }
                }
            }
        }
    }
    if (check)
        l[i].classList.add("highlight");
});