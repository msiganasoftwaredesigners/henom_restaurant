// // menu/static/menu/menu_admin.js
// document.addEventListener('DOMContentLoaded', function () {
//     const menuTypeField = document.querySelector('#id_menu_type');
//     const menuGroupField = document.querySelector('#id_menu_group');

//     function updateMenuGroups() {
//         const menuTypeId = menuTypeField.value;
//         menuGroupField.innerHTML = '<option value="">---------</option>'; // Reset options

//         if (menuTypeId) {
//             fetch(`/admin/get-menu-groups/?menu_type_id=${menuTypeId}`)
//             .then(response => {
//                 console.log("Response status:", response.status);
//                 return response.text();  // Read as text first
//             })
//             .then(text => {
//                 console.log("Response text:", text);  // Log the response content
//                 return JSON.parse(text);  // Now parse JSON
//             })
//             .then(data => {
//                 console.log("Parsed JSON:", data);
//                 data.forEach(group => {
//                     const option = document.createElement('option');
//                     option.value = group.id;
//                     option.textContent = group.name;
//                     menuGroupField.appendChild(option);
//                 });
//             })
//             .catch(error => console.error("Error fetching menu groups:", error));
        
//         }
//     }

//     if (menuTypeField) {
//         menuTypeField.addEventListener('change', updateMenuGroups);
//         updateMenuGroups(); // Ensure correct options are set when loading an edit form
//     }
// });
