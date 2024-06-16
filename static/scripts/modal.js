// document.addEventListener('DOMContentLoaded', function() {
//     console.log("Скрипт modal.js загружен.");

//     // Получаем кнопку "Открыть модальное окно"
//     var openModalBtn = document.getElementById("save-build");

//     // Получаем модальное окно
//     var modal = document.getElementById("myModal");

//     // Получаем элемент <span>, который закрывает модальное окно
//     var span = document.getElementsByClassName("close")[0];

//     // Проверяем, найдена ли кнопка
//     if (openModalBtn) {
//         console.log("Кнопка открытия модального окна найдена.");
//         openModalBtn.addEventListener('click', function() {
//             console.log("Кнопка открытия модального окна нажата");
//             // Открываем модальное окно
//             modal.style.display = "block";
//         });
//     } else {
//         console.error("Кнопка открытия модального окна не найдена");
//     }

//     // Когда пользователь кликает на <span> (x), закрываем модальное окно
//     if (span) {
//         span.onclick = function() {
//             modal.style.display = "none";
//         }
//     }

//     // Когда пользователь кликает в любом месте за пределами модального окна, закрываем его
//     window.onclick = function(event) {
//         if (event.target == modal) {
//             modal.style.display = "none";
//         }
//     }
// });


// // document.getElementById('save-build-btn').addEventListener('click', function() {
// //     const buildName = document.getElementById('build-name-input').value;
// //     const userId = document.getElementById('user_id').value;
// //     const totalPrice = calculateTotalPrice(); // Получаем общую сумму

// //     const buildData = {
// //         name: buildName,
// //         user_id: userId,
// //         components: []
// //     };

// //     document.querySelectorAll('.compatibility-item.selected').forEach(item => {
// //         buildData.components.push(item.getAttribute('data-name'));
// //     });

// //     fetch('/save_build', {
// //         method: 'POST',
// //         headers: {
// //             'Content-Type': 'application/json',
// //         },
// //         body: JSON.stringify(buildData),
// //     })
// //     .then(response => response.json())
// //     .then(data => {
// //         console.log('Success:', data);
// //         const modal = document.getElementById('myModal');
// //         modal.style.display = 'none';

// //         const totalPriceSpan = document.getElementById('total-price');
// //         totalPriceSpan.textContent = totalPrice;

// //         const totalPriceLabel = document.getElementById('total-price-label');
// //         totalPriceLabel.style.display = 'block';
// //         console.log('Total Price:', totalPrice);
// //     })
// //     .catch((error) => {
// //         console.error('Error:', error);
// //     });
// // });

// // // Функция для подсчёта общей стоимости
// // function calculateTotalPrice() {
// //     let totalPrice = 0;
// //     // Выбираем все выбранные компоненты
// //     document.querySelectorAll('.compatibility-item.selected').forEach(item => {
// //         // Получаем цену компонента и добавляем её к общей сумме
// //         const price = parseFloat(item.getAttribute('data-цена'));
// //         totalPrice += price;
// //     });
// //     return totalPrice;
// // }