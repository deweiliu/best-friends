function TimeToBirthday() {
    let now = Date.now();
    let finish_time = new Date("2018-12-11T00:00:00Z");
    let delta_time = finish_time - now;
    let seconds = Math.floor(delta_time / 1000);

    let minutes = Math.floor(seconds / 60);
    seconds %= 60;

    let hours = Math.floor(minutes / 60);
    minutes %= 60;

    let days = Math.floor(hours / 24);
    hours %= 24;

    str = "There are " + days + " days, " + hours + " hours, " + minutes + " minutes and " + seconds + " seconds to Kexin's birthday! ";
    document.getElementById("dateField").innerHTML = str;
    setTimeout("TimeToBirthday()", 1000);
}
TimeToBirthday()