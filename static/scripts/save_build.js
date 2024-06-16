document.addEventListener('DOMContentLoaded', function() {
    console.log("Скрипт save_build.js загружен.");

    var saveBtn = document.getElementById("save-build-btn");
    var modalOpenBtn = document.getElementById("save-build");

    if (saveBtn) {
        console.log("Кнопка сохранения найдена.");
        saveBtn.addEventListener('click', function() {
            console.log("Кнопка сохранения нажата");
            var buildName = document.getElementById('build-name-input').value;
            if (buildName.trim() === "") {
                alert("Пожалуйста, введите имя сборки.");
                return;
            }

            // Получаем сумму сборки
            var totalPriceElement = document.getElementById('total-price');
            var totalPrice = calculateTotalPrice();
            
            // Проверяем, если сумма корректно обновляется
            console.log("Total Price:", totalPrice);

            const selectedComponents = {
                processor: document.querySelector('.compatibility-category[data-list="processors-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                videocard: document.querySelector('.compatibility-category[data-list="videocards-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                ram: document.querySelector('.compatibility-category[data-list="ram-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                motherboard: document.querySelector('.compatibility-category[data-list="motherboards-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                psu: document.querySelector('.compatibility-category[data-list="psus-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                harddrive: document.querySelector('.compatibility-category[data-list="harddrives-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                case: document.querySelector('.compatibility-category[data-list="cases-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                keyboard: document.querySelector('.compatibility-category[data-list="keyboards-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                mouse: document.querySelector('.compatibility-category[data-list="mice-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                monitor: document.querySelector('.compatibility-category[data-list="monitors-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                coolingsystem: document.querySelector('.compatibility-category[data-list="coolingsystems-list"] .compatibility-item.selected')?.getAttribute('data-name') || null,
                user_id: document.getElementById('user_id').value,
                build_name: buildName,
                total_price: totalPrice
            };

            console.log('Selected components with total price:', selectedComponents);

            fetch('/save_build', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(selectedComponents)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                alert('Сборка сохранена успешно!');

                // Обновляем общую цену сборки в модальном окне
                var totalPriceModalElement = document.getElementById('total-price-modal');
                if (totalPriceModalElement) {
                    totalPriceModalElement.textContent = totalPrice.toFixed(2);
                } else {
                    console.error("Элемент для отображения суммы сборки в модальном окне не найден.");
                }

                // Дополнительно скрываем модальное окно после сохранения
                var modal = document.getElementById('myModal');
                modal.style.display = 'none';
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert('Ошибка при сохранении сборки.');
            });
        });
    } else {
        console.error("Кнопка сохранения не найдена");
    }

    if (modalOpenBtn) {
        modalOpenBtn.addEventListener('click', function() {
            // Обновляем общую цену сборки перед открытием модального окна
            var totalPriceElement = document.getElementById('total-price-modal');
            var totalPrice = parseFloat(document.getElementById('total-price').innerText);
            if (totalPriceElement) {
                totalPriceElement.textContent = totalPrice.toFixed(2);
            } else {
                console.error("Элемент для отображения суммы сборки в модальном окне не найден.");
            }
        });
    } else {
        console.error("Кнопка открытия модального окна не найдена");
    }

    // Функция для подсчёта общей стоимости
    function calculateTotalPrice() {
        let totalPrice = 0;
        // Выбираем все выбранные компоненты
        document.querySelectorAll('.compatibility-item.selected').forEach(item => {
            // Получаем цену компонента и добавляем её к общей сумме
            const price = parseFloat(item.getAttribute('data-цена'));
            totalPrice += price;
        });
        return totalPrice;
    }
});
