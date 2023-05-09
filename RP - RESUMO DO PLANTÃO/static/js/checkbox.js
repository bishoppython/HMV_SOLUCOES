// Seleciona todos os elementos com a classe "validate-checkbox"
var checkboxes = document.getElementsByClassName("validate-checkbox");

// Percorre todos os elementos
for (var i = 0; i < checkboxes.length; i++) {
  checkboxes[i].onclick = function() {
    // Desmarca todos os outros checkbox com a mesma classe
    for (var j = 0; j < checkboxes.length; j++) {
      if (checkboxes[j] != this) {
        checkboxes[j].checked = false;
      }
    }
  };
}
