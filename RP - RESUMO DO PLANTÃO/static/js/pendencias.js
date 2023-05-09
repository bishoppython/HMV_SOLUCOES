var pendenciaSim = document.getElementsByClassName("pendencias-sim")[0];
var pendenciaNao = document.getElementsByClassName("pendencias-nao")[0];
const opcoespendencias = document.getElementById("pendencias-opcoes");

pendenciaSim.addEventListener('click', function() {
  if (this.checked) {
    pendenciaNao.checked = false;
    opcoespendencias.style.display = "block";
  } else {
    opcoespendencias.style.display = "none";
  }
});

pendenciaNao.addEventListener('click', function() {
  if (this.checked) {
    pendenciaSim.checked = false;
    opcoespendencias.style.display = "none";
  }
});