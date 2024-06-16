document.addEventListener('DOMContentLoaded', function() {
    console.log("Скрипт modal.js загружен.");

    // Получаем кнопку "Открыть модальное окно"
    var openModalBtn = document.getElementById("open-modal-btn");

    // Проверяем, найдена ли кнопка
    if (openModalBtn) {
        console.log("Кнопка открытия модального окна найдена.");
        openModalBtn.onclick = function() {
            console.log("Кнопка открытия модального окна нажата");
            // Здесь добавьте ваш код для открытия модального окна
        };
    } else {
        console.error("Кнопка открытия модального окна не найдена");
    }
});
