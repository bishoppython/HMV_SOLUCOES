var consideraSim = document.getElementsByClassName("consideracoes-sim")[0];
var consideraNao = document.getElementsByClassName("consideracoes-nao")[0];
const opcoesconsideracoes = document.getElementById("consideracoes-opcoes");

consideraSim.addEventListener('click', function() {
  if (this.checked) {
    consideraNao.checked = false;
    opcoesconsideracoes.style.display = "block";
  } else {
    opcoesconsideracoes.style.display = "none";
  }
});

consideraNao.addEventListener('click', function() {
  if (this.checked) {
    consideraSim.checked = false;
    opcoesconsideracoes.style.display = "none";
  }
});
