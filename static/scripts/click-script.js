document.addEventListener('DOMContentLoaded', function() {
  // Обработчик клика на заголовках категорий
  const categories = document.querySelectorAll('.compatibility-category h2');
  categories.forEach(category => {
      category.addEventListener('click', function() {
          const items = this.nextElementSibling;
          if (items.classList.contains('active')) {
              items.classList.remove('active');
          } else {
              items.classList.add('active');
          }
      });
  });

  // Обработчик клика на элементах комплектующих
  const items = document.querySelectorAll('.compatibility-item');
  items.forEach(item => {
      item.addEventListener('click', function() {
          const details = this.querySelector('.item-details');
          if (details) {
              details.remove(); // Если детали уже существуют, удаляем их
          } else {
              // Если деталей еще нет, то создаем и добавляем их
              const id = this.getAttribute('data-id');
              const name = this.getAttribute('data-name');
              const description = this.getAttribute('data-description');
              const brand = this.getAttribute('data-brand');
              const extraAttributes = [];

              // Собираем все атрибуты data-*, кроме id, name, description и brand
              this.getAttributeNames().forEach(attr => {
                  if (attr.startsWith('data-') && !['data-id', 'data-name', 'data-description', 'data-brand'].includes(attr)) {
                      extraAttributes.push({ name: attr.replace('data-', ''), value: this.getAttribute(attr) });
                  }
              });

              let detailsHtml = `
                  <div class="item-details">
              `;

              extraAttributes.forEach(attr => {
                  detailsHtml += `<p>${attr.name}: ${attr.value}</p>`;
              });

              detailsHtml += '</div>';

              // Добавляем детали внутрь элемента комплектующего
              this.insertAdjacentHTML('beforeend', detailsHtml);
          }
      });
  });

  // Обработчик клика на кнопках выбора
  const selectButtons = document.querySelectorAll('.select-item');
  selectButtons.forEach(button => {
      button.addEventListener('click', function(event) {
          event.stopPropagation(); // Останавливаем всплытие события

          const currentItem = this.closest('.compatibility-item');
          const category = currentItem.closest('.compatibility-category');

          // Убираем выделение с других элементов в той же категории
          const selectedItems = category.querySelectorAll('.compatibility-item.selected');
          selectedItems.forEach(item => {
              item.classList.remove('selected');
          });

          // Добавляем выделение текущему элементу
          currentItem.classList.add('selected');
      });
  });
});
