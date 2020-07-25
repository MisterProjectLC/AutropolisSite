
var button = document.querySelector(".toggle")
button.addEventListener('click', toggleLore);


function toggleLore() {
  var italics = document.querySelectorAll("i");
  italics.forEach((item, i) => {
    if (item.style.display === "none") {
      item.style.display = "inline";
      button.textContent = "Esconder Lore";
    } else {
      item.style.display = "none";
      button.textContent = "Mostrar Lore";
    }
  });
}
