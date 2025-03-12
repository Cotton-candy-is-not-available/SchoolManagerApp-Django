let currentDate = new Date; //start from current user's device date
var numOfEvents = 0; //counter for number of events on a specific day
var currDayNum = 0; //counter for the number of the day

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

               for (let dayNum = 1; dayNum < daysInMonth; dayNum++) { //loop through each day individually
                   for (var key in response.events) { //loop through all the events in the database
                        const eventDate = new Date(response.events[key].date_of_event.replace(/-/g, '\/')) //save the date of the event

                      if (eventDate.getMonth() === month && eventDate.getFullYear() === year && eventDate.getDate() === dayNum) { //check if the date of the event is the same as the day
                        //if yes

                        //get the dayCell for the corresponding day
                        const dayCell = document.querySelector(`.day[data-day="${dayNum}"]`);

                        if (dayCell) {
                            //retrieve the event data for that day
                            const eventHTML = `<li>${response.events[key].event_name}</li>`; //displays name of the event

                            dayCell.innerHTML += `${eventHTML}`; //add the event data to the data-day of the daycell

                            //highlight the current day
                            if (dayNum === newDate.getDate()) {
                                dayCell.classList.add('highlight'); // Highlight current day
                            }
                        }

                          numOfEvents += 1
                          console.log("number of events is:" + numOfEvents + " day number is:" + dayNum);

                          if(numOfEvents > 3) { //if the number of events for that specific day is > 3
                              viewMore(); //toggle the view more button ON
                              dayCell.innerHTML += `<a href="/weekly_schedule/" className="moreButton" id="vmButton">View More</a>`

                          }
                          //if no, keep the view more button toggled OFF


                      }
                      //if no, take the next event in the database and check again

                   }
                   numOfEvents = 0; //reset the event counter for the next day
               }









           },
           error: function (response){
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

function viewMore() {
    var button = document.getElementById("vmButton");
    button.style.display = "block";
    //button.style.display = "none";
}