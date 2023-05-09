var intercorrenciaSim = document.getElementsByClassName("intercorrencia-sim")[0];
var intercorrenciaNao = document.getElementsByClassName("intercorrencia-nao")[0];
const opcoesintercorrencia = document.getElementById("intercorrencia-opcoes");

intercorrenciaSim.addEventListener('click', function() {
  if (this.checked) {
    intercorrenciaNao.checked = false;
    opcoesintercorrencia.style.display = "block";
  } else {
    opcoesintercorrencia.style.display = "none";
  }
});

intercorrenciaNao.addEventListener('click', function() {
  if (this.checked) {
    intercorrenciaSim.checked = false;
    opcoesintercorrencia.style.display = "none";
  }
});

