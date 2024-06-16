// Получаем все элементы compatibility-category
var categories = document.querySelectorAll('.compatibility-category');

// Добавляем обработчик событий для каждой категории
categories.forEach(function(category) {
    category.addEventListener('click', function() {
        // Получаем значение атрибута data-list
        var listName = this.getAttribute('data-list');
        
        // Получаем соответствующий элемент compatibility-items
        var items = document.querySelector('.' + listName);
        
        // Добавляем или удаляем класс active в зависимости от текущего состояния
        items.classList.toggle('active');
    });
});
