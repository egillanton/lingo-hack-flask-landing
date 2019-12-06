function changeTimezone(date, ianatz) {
    var invdate = new Date(date.toLocaleString('en-US', {
        timeZone: ianatz
    }));
    var diff = date.getTime() - invdate.getTime();
    return new Date(date.getTime() + diff);
}

function getTimeOfEvent() {
    var there = new Date("Apr 24 2020 08:00:00 GMT +0000");
    var here = changeTimezone(there, "Atlantic/Reykjavik");
    return here
}

var clock = $('#clock');

clock.countdown(getTimeOfEvent(), function (event) {
    $(this).html(event.strftime('%D days %H:%M:%S'));
});

clock.countdown(getTimeOfEvent());



$(document).ready(function () {
    clock.countdown('resume');

    document.getElementById("send_button").addEventListener("click", sendEmail, false);
});
