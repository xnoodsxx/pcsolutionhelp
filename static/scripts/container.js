// document.addEventListener('DOMContentLoaded', function() {
//     const compatibilityItems = document.querySelectorAll('.compatibility-item');

//     compatibilityItems.forEach(function(item) {
//         item.addEventListener('click', function() {
//             // Получаем список атрибутов из data-атрибутов элемента
//             const id = item.dataset.id;
//             const name = item.dataset.name;
//             const description = item.dataset.description;
//             const brand = item.dataset.brand;
//             const price = item.dataset.price;

//             // Создаем HTML-разметку для списка комплектующих
//             const itemListHTML = `
//                 <ul>
//                     <li>ID: ${id}</li>
//                     <li>Название: ${name}</li>
//                     <li>Описание: ${description}</li>
//                     <li>Бренд: ${brand}</li>
//                     <li>Цена: ${price}</li>
//                 </ul>
//             `;

//             // Создаем элемент списка и добавляем его в DOM
//             const itemListElement = document.createElement('div');
//             itemListElement.classList.add('item-list');
//             itemListElement.innerHTML = itemListHTML;
//             item.appendChild(itemListElement);

//             // Добавляем обработчик клика для закрытия списка при повторном нажатии
//             item.addEventListener('click', closeItemList);

//             // Предотвращаем дальнейшие события (например, переход по ссылке)
//             event.stopPropagation();
//         });
//     });

//     // Функция для закрытия списка комплектующих
//     function closeItemList(event) {
//         const item = event.currentTarget;
//         const itemList = item.querySelector('.item-list');
//         if (itemList) {
//             itemList.remove();
//             // Удаляем обработчик клика для закрытия списка
//             item.removeEventListener('click', closeItemList);
//         }
//     }

//     // Закрываем список при клике вне элемента
//     document.addEventListener('click', function(event) {
//         const itemList = document.querySelector('.item-list');
//         if (itemList && !event.target.closest('.compatibility-item')) {
//             itemList.remove();
//         }
//     });
// });
