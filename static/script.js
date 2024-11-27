document.addEventListener("DOMContentLoaded", () => {
  // constavel, para selecionar a classe sub_btn
  const subButtons = document.querySelectorAll(".sub_btn");


// criando intereção
  subButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const submenu = button.nextElementSibling;

      // Verifica 
      const isActive = submenu.classList.contains("active");

      // Fecha 
      document.querySelectorAll(".sub_menu").forEach((menu) => {
        menu.classList.remove("active");
      });

      // Abre 
      if (!isActive) {
        submenu.classList.add("active");
      }
    });
  });
});