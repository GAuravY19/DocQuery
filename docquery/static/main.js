// document.addEventListener("DOMContentLoaded", function () {
//     const welcomeModal = new bootstrap.Modal(
//         document.getElementById("welcomeModal")
//     );
//     welcomeModal.show();
// });


document.addEventListener("DOMContentLoaded", function () {
    const modalElement = document.getElementById("welcomeModal");

    if (modalElement) {
        const welcomeModal = new bootstrap.Modal(modalElement);
        welcomeModal.show();
    }
});
