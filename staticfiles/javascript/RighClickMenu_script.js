const day_1Event_Display = document.querySelectorAll(".eventBoxes");
const Event_Right_Click_Menu = document.querySelector(".EventRightClickMenu")

for (let i = 0; i < day_1Event_Display.length; i++) {
    //Adds event listener to each  Event being displayed


    day_1Event_Display[i].addEventListener("contextmenu", (event) => {
        console.log(" Start i: ", i)

        event.preventDefault();//prevents regular right click menu from appearing
        event.stopPropagation(); //important!!

        console.log("before active i: ", i)

        Event_Right_Click_Menu.classList.add("active")
        console.log("after active i: ", i)
        //Position of the menu
        let topPosition = event.clientY;
        let leftPosition = event.clientX;

        Event_Right_Click_Menu.style.top = topPosition + "px";
        Event_Right_Click_Menu.style.left = leftPosition + "px";
    });
}


//Closes window when you click somewhere else
window.addEventListener("click", () => {
    Event_Right_Click_Menu.classList.remove("active");
})