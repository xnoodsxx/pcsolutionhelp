// fetch('/save_build', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//       build_name: 'My Gaming PC1', // Добавляем имя сборки
//       processor: 'Intel Core i9-11900K',
//       videocard: 'NVIDIA GeForce RTX 3080',
//       ram: 'Corsair Vengeance LPX',
//       motherboard: 'ASUS ROG Strix B550-F Gaming',
//       psu: 'EVGA SuperNOVA 750 G3',
//       harddrive: 'Samsung 970 EVO Plus',
//       case: 'NZXT H510',
//       keyboard: 'Razer BlackWidow Elite',
//       mouse: 'Logitech G Pro Wireless',
//       monitor: 'Dell S2721DGF',
//       coolingsystem: 'Noctua NH-D15',
//       total_price: 2790,
//       user_id: 1 // Замените на реальный user_id
//     })
//   })
//   .then(response => {
//       console.log(response); // Вывести весь объект ответа
//       return response.json();
//   })
//   .then(data => {
//     console.log(data);
//   })
//   .catch(error => {
//     console.error('Error:', error);
//   });
