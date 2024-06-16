// Функция для подсчета суммы выбранных комплектующих
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
