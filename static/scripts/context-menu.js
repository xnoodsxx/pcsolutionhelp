function toggleContextMenu(event) {
  var contextMenu = document.getElementById("contextMenu");
  if (contextMenu.style.display === "block") {
    contextMenu.style.display = "none";
  } else {
    contextMenu.style.display = "block";
  }
}

document.addEventListener("click", function (event) {
  var contextMenu = document.getElementById("contextMenu");
  var button = document.getElementById("myButton");

  if (!contextMenu.contains(event.target) && event.target !== button) {
    contextMenu.style.display = "none";
  }
});

document.addEventListener('DOMContentLoaded', function () {
  var personalAccountLink = document.getElementById('personalAccountLink');
  if (personalAccountLink) {
    personalAccountLink.addEventListener('click', function (e) {
      // Предотвращение действия по умолчанию (например, переход по ссылке)
      e.preventDefault();
      // Перенаправление на окно регистрации
      redirectToRegistration();
      // Скрытие контекстного меню (если это необходимо)
      hideContextMenu();
    });
  }
});

// Определение функции для перенаправления на окно регистрации
function redirectToRegistration() {
  // Используй window.location.href для перенаправления на другую страницу
  window.location.href = "/login";
}

// Твой существующий код для скрытия контекстного меню
function hideContextMenu() {
  var contextMenu = document.getElementById("contextMenu");
  contextMenu.style.display = "none";
}

