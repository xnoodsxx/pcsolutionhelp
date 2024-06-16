// change-build-name.js

// Предположим, что data содержит только один объект с новым именем сборки
// Если это не так, нужно проверить структуру получаемых данных

// Дождемся загрузки DOM
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM загружен.');

    const saveBtn = document.getElementById('save-build-name-btn');
    const nameInput = document.getElementById('build-name-input');
    
    console.log('Кнопка сохранения имени сборки найдена.');

    saveBtn.addEventListener('click', () => {
        const newName = nameInput.value.trim();

        // Проверяем, что новое имя не пустое
        if (newName !== '') {
            const buildId = buildId
            const url = `/change_build_name/${buildId}`;

            // Отправляем запрос на изменение имени сборки
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ new_name: newName }) // отправляем новое имя сборки
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.message); // Выводим сообщение об успешном изменении имени
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
        } else {
            console.log('Введите новое имя сборки.');
        }
    });
});
