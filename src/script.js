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
        var offset = 0;
			
		if (ampm == "AM" && hour == 0)
				offset = 24;
		else if (ampm == "PM"){
			if (!(hour == 12))
				offset = 12;
		}

        return (hour + offset) * 60 + minute;
    };

    var found = false;
    var i = 0;

    var dt = new Date();
    var hour = dt.getHours();
    var minute = dt.getMinutes();
    var time = (hour == 0 ? 24 : hour) * 60 + minute; //time in minute

    //Get list of all elements have class = "row"
    var l = document.getElementsByClassName("row");
    var len = l.length;

    //Not empty
    if (len > 0) {
            //Loop till find the time needed
            do {
                if (time >= timeToMinute((l[i].querySelector(".col-time .start-time")).textContent) &&
					time <= timeToMinute((l[i].querySelector(".col-time .end-time")).textContent))
                    found = true;
                else
					++i;
            } while (i < len && !found);
    }
    if (found)
        l[i].classList.add("highlight");
});