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
        dayCell.setAttribute('data-day', day); //basically creating an attribute of each daycell to contain the event data specific to that day
        dayCell.innerText = day.toString();
        calendarGrid.appendChild(dayCell);

    }

    $(document).ready(function () {
       $.ajax({
           type:'GET',
           url: "http://127.0.0.1:8000/displayEvents/",//gets display events link so that it can render the data
           success: function (response){
               $("#display").empty();

               for (var key in response.events) { //loop through each event
                   console.log(key)
                   console.log(response.events);
                   //.replace(/-/g, '\/') is so that it displays in the correct days
                   const eventDate = new Date(response.events[key].date_of_event.replace(/-/g, '\/')) //save the date of the event
                  //Debugging
                  //  console.log("this is the eventDay.getday: " + eventDate.getDate())
                   console.log(eventDate)
                   console.log(daysInMonth);

                   for(let day = 1; day < daysInMonth; day++) {
                       // console.log("we're looping through days in the month")
                      if (eventDate.getMonth() === month && eventDate.getFullYear() === year && eventDate.getDate() === day) { //check if the date of the event is the same as the day
                          // Find the dayCell for the corresponding day
                        const dayCell = document.querySelector(`.day[data-day="${day}"]`);
                        if (dayCell) {
                            //retrieve the event data for that day
                        // const dayCell = document.createElement("div");

                            const eventHTML = `<br><li id = "CalendarEventBox" class = "CalendarEventBox" oncontextmenu = testFunction() >${response.events[key].event_name} </li>`;//displays name of the event

                            let EventID = response.events[key].id;
                            let UpdateUrl = "/updateEvent/ pk ".replace('pk', EventID);
                            let DeleteUrl = "/deleteEvent/ pk ".replace('pk', EventID);

                            const MenuHTML = `<div id="EventRightClickMenu2" class = "EventRightClickMenu2" >
                                <ul>
                                    <li><a href='${UpdateUrl}'>Edit</a></li>
                                    <li><a href='${DeleteUrl}'onClick="return confirm('Are you sure you want to delete this event?');">Delete</a>
                                    </li>
                                    <li><a href="#">View More</a></li>
                                </ul>

                            </div>`;//displays description and name of event

                            dayCell.innerHTML += `${eventHTML} ${MenuHTML}`; //add the event data to the data-day of the daycell

                            //highlight the current day
                            if (day === newDate.getDate()) {
                                dayCell.classList.add('highlight'); // Highlight current day
                            }
                        }
                      }
                   }
               }
           },
           error: function (response) {
               alert("error")
           }
       });
    })
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


