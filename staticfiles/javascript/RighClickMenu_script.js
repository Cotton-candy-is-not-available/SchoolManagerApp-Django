const day_1Event_Display = document.querySelector(".day1EventDisplay");
const Event_Right_Click_Menu = document.querySelector(".EventRightClickMenu")

day_1Event_Display.addEventListener("contextmenu", (event) => {
   event.preventDefault();
    Event_Right_Click_Menu.classList.add("active")
//Position of the menu
    let topPosition = event.clientY;
    let leftPosition = event.clientX;

    Event_Right_Click_Menu.style.top = topPosition + "px";
    Event_Right_Click_Menu.style.left = leftPosition + "px";
});

window.addEventListener("click", () => {
    Event_Right_Click_Menu.classList.remove("active");
})