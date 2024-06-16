const button = document.getElementById('myButton');
const contextMenu = document.getElementById('contextMenu');

button.addEventListener('click', () => {
  contextMenu.classList.toggle('show');
});