
/* sideNav extension */
window.addEventListener('load', adjustHeight);
window.addEventListener('resize', adjustHeight);


function adjustSideNavHeight() {
  const sideNav = document.querySelector('.sideNav');
  const mainContent = document.querySelector('.main-content');

  const contentHeight = mainContent.scrollHeight;

  sideNav.style.height = `${Math.max(contentHeight, window.innerHeight)}px`;
}