let WeeklyEvents = document.querySelectorAll(".eventBoxes");
let CalendarEvents = document.querySelectorAll(".weekDay");
let Event_Right_Click_Menu = document.querySelectorAll(".EventRightClickMenu")
let Event_Right_Click_Menu2 = document.querySelectorAll(".EventRightClickMenu2")

function Menu(i, topPosition, leftPosition){
            console.log(" 1 event: ", Event_Right_Click_Menu[i])
        //Turns on context menu
        Event_Right_Click_Menu[i].classList.add("active")

    //Position
        Event_Right_Click_Menu[i].style.top = topPosition + "px";
        Event_Right_Click_Menu[i].style.left = leftPosition + "px";

//Closes window when you click somewhere else
        window.addEventListener("click", () => {
    Event_Right_Click_Menu[i].classList.remove("active");
})

}
console.log("Calendar", CalendarEvents)
console.log("Weekly", WeeklyEvents)



function Menu2(i){
            console.log(" Right click 2: ", Event_Right_Click_Menu2[i])
        //Turns on context menu
        Event_Right_Click_Menu2[i].classList.add("active")

    //Position
    //     Event_Right_Click_Menu2[i].style.top = topPosition + "px";
    //     Event_Right_Click_Menu2[i].style.left = leftPosition + "px";

//Closes window when you click somewhere else
        window.addEventListener("click", () => {
    Event_Right_Click_Menu2[i].classList.remove("active");
})

}



// ------------------- Weekly events addEvent listener ---------------------
for (let i = 0; i < WeeklyEvents.length; i++) {

    //Adds event listener to each  Event being displayed
    WeeklyEvents[i].addEventListener("contextmenu", (event) => {

        event.preventDefault();//prevents regular right click menu from appearing
        event.stopPropagation(); //important!!

        console.log("before active i: ", i)

        console.log("after active i: ", i)
        //Position of the menu
        let topPosition = event.clientY;
        let leftPosition = event.clientX;


        //Displays and closes context menu and positions it
        Menu(i, topPosition, leftPosition);

    });
}



// ------------------- Calendar events addEvent listener ---------------------


for (let i = 0; i < CalendarEvents.length; i++) {
console.log("Forloop running");        //Turns on context menu

    //Adds event listener to each  Event being displayed
    //addEventListenersToElements
    CalendarEvents[i].addEventListener("click", (event) => {

        event.preventDefault();//prevents regular right click menu from appearing
        event.stopPropagation(); //important!!

        console.log("Adding listener: ", i)

        console.log("after active i: ", i)
        //Position of the menu
        let topPosition = event.clientY;
        let leftPosition = event.clientX;


        //Displays and closes context menu and positions it
        Menu2(i, topPosition, leftPosition);

    });

}