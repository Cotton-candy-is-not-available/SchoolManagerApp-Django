document.addEventListener("DOMContentLoaded", function() {

    //get all current date, month, and year from the user's device
    const currentDate = new Date();
    const month = currentDate.getMonth();  // 0-11 (January = 0)
    const year = currentDate.getFullYear();

    //get the starting day of the month (0 = Sunday, 1 = Monday, etc.)
    const firstDayOfMonth = new Date(year, month, 1).getDay();
    //total number of days in the month
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    //all possible months to be displayed
    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    //document.getElementById("month_name").innerText = months[month]; //sets to the correct month
    document.getElementById("month_name").querySelector("h2").innerText = months[month];
    const calendarGrid = document.getElementById("calendar_grid");

    for (let i = 0; i < firstDayOfMonth; i++) {
        const emptyCell = document.createElement("p");
        calendarGrid.appendChild(emptyCell);  //add empty cell before the 1st day
    }

    //add the rest of the days of the month to the grid
    for (let day = 1; day <= daysInMonth; day++) {
        const dayCell = document.createElement("div");
        dayCell.className = 'day';
        dayCell.innerText = day.toString();
        calendarGrid.appendChild(dayCell);

        if (day == currentDate.getDate()) {
            dayCell.classList.add('highlight'); //highlights the current day
        }
    }

});


