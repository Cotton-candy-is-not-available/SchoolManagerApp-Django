let day_1Event_Display = document.querySelectorAll(".eventBoxes");
let Event_Right_Click_Menu = document.querySelectorAll(".EventRightClickMenu")

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


for (let i = 0; i < day_1Event_Display.length; i++) {

    //Adds event listener to each  Event being displayed
    day_1Event_Display[i].addEventListener("contextmenu", (event) => {

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

