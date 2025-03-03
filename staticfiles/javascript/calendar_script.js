let currentDate = new Date; //start from current user's device date

function generateCalendar(newDate) {
    //retrieve the current newDate and calculate/retrieve all of its information
    const month = newDate.getMonth(); // 0 - 11
    const year = newDate.getFullYear();
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const daysInMonth = lastDay.getDate();
    const startingDay = firstDay.getDay();

    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    //update month name h2 tag in html with the correct month and year
    document.getElementById("month_name").querySelector("h2").innerText = months[month] + ' ' + year;

    //clear previous calendar by redefining the calendarGrid for a new one
    const calendarGrid = document.getElementById('calendar_grid');
    //fixed display of all the days of the week
    calendarGrid.innerHTML = '<p>Sunday</p><p>Monday</p><p>Tuesday</p><p>Wednesday</p><p>Thursday</p><p>Friday</p><p>Saturday</p>';

    for (let i = 0; i < startingDay; i++) {
        calendarGrid.innerHTML += '<p></p>'; //empty squares for days before the first of the month
    }

    //add all the rest of the days to the calendarGrid
    for (let day = 1; day <= daysInMonth; day++) {
        const dayCell = document.createElement("div");
        dayCell.className = 'day';
        dayCell.innerText = day.toString();
        calendarGrid.appendChild(dayCell);

        $(document).ready(function () {
               setInterval(function () {
               $.ajax({
                   type:'GET',
                   url: "http://127.0.0.1:8000/displayEvents/",//gets display events link so that it can render the data
                   // startDateObj = datetime.strptime(response.events[key].date_of_event,%d-%m-%y - %H:%M:%S)
                   success: function (response){
                   // {#console.log(response)#}
                       $("#display").empty();

                       if (day === newDate.getDate()){
                       dayCell.innerHTML = day.toString() + " "//clears boxes
                            dayCell.classList.add('highlight'); //highlights the current day
                           $("#display").empty()
                       }

                       for (var key in response.events) { //loop through each event
                           console.log(key)
                           console.log(response.events);
                           const eventDate = new Date(response.events[key].date_of_event) //save the date of the event
                           console.log("this is the eventDay.getday" + eventDate.getDate())
                           console.log(eventDate)
                           console.log(daysInMonth);

                           for(let day = 1; day < daysInMonth; day++) {
                               console.log("we're looping through days in the month")
                              if (eventDate.getMonth() === month && eventDate.getFullYear() === year && eventDate.getDate() === day) { //check if the date of the event is the same as the day
                             // if (eventDate.getDate() === day) { //check if the date of the event is the same as the day
                                   var temp = "<li>" + response.events[key].date_of_event + " " + response.events[key].description + "</li>";
                                   dayCell.innerHTML = dayCell.innerText + "___" + temp
                                   $("#display").append(temp);
                                   console.log("we're doing something")
                              }
                           }

                           // if (response.events[key].date_of_event === num.toString(day)) {
                           //     var temp = "<li>" + response.events[key].date_of_event + " " + response.events[key].description + "</li>";
                           //     dayCell.innerHTML = dayCell.innerText + "___" + temp
                           //     $("#display").append(temp);
                           // }
                       }
                   },
                   error: function (response){
                       alert("error")
                   }
               });
               },1000);
        })
    }
}

function nextMonth() {
    currentDate.setMonth(currentDate.getMonth() + 1); //increases the value of month (0-11)
    generateCalendar(currentDate);
}

function prevMonth() {
    currentDate.setMonth(currentDate.getMonth() - 1); //decreases the value of month (0-11)
    generateCalendar(currentDate);
}

window.onload = function() {
    generateCalendar(currentDate);
}