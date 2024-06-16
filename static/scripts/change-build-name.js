document.addEventListener('DOMContentLoaded', function() {
    console.log("Скрипт для изменения имени сборки загружен.");

    // Проверяем, загружен ли DOM
    console.log("DOM загружен.");

    // Получаем кнопку "Сохранить имя сборки"
    var saveNameBtn = document.getElementById("save-build-name-btn");
    console.log(saveNameBtn); // Добавим эту строку для отладки

    // Получаем поле ввода для имени сборки
    var buildNameInput = document.getElementById('build-name-input');
    console.log(buildNameInput); // Добавим эту строку для отладки

    // Обработчик клика на кнопке "Сохранить имя сборки"
    if (saveNameBtn && buildNameInput) {
        console.log("Кнопка сохранения имени сборки найдена.");
        saveNameBtn.addEventListener('click', function() {
            console.log("Кнопка сохранения имени сборки нажата");

            // Получаем новое имя сборки из поля ввода
            var newName = buildNameInput.value;
            if (newName.trim() === "") {
                alert("Пожалуйста, введите новое имя сборки.");
                return;
            }

            // Получаем ID сборки из скрытого поля
            var buildId = document.getElementById('build-id').value;

            // Отправляем запрос на сервер для изменения имени сборки
            fetch('/change_build_name/' + buildId, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ new_name: newName })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data); // Посмотрите данные ответа в консоли для отладки
                alert('Имя сборки успешно изменено!');
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert('Ошибка при изменении имени сборки.');
            });
        });
    } else {
        console.error("Кнопка сохранения имени сборки не найдена или отсутствует поле ввода");
    }
});
