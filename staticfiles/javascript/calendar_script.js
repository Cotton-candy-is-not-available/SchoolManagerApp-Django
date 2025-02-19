let currentDate = new Date; //start from current user's device date

function generateCalendar(newDate) {
    //retrieve all events and their information passed from views json dump
    //const events = JSON.parse('{{ events_json|escapejs }}');

    //retrieve the current newDate and calculate/retrieve all of its information for the calendar
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

        if (day === newDate.getDate()) {
            dayCell.classList.add('highlight'); //highlights the current day
        }

       /*
       events.forEach(event => {
            //extract the day from the event's date_of_event string
            const eventDate = new Date(event.day_of_event);
            const eventDay = eventDate.getDate();
            if (eventDay === day) {
             // display
            }
        })
        */

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