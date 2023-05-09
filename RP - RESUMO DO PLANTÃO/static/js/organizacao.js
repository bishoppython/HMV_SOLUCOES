var organizacaoSim = document.getElementsByClassName("organizacao-sim")[0];
var organizacaoNao = document.getElementsByClassName("organizacao-nao")[0];
const opcoesorganizacoes = document.getElementById("organizacao-opcoes");

organizacaoSim.addEventListener('click', function() {
  if (this.checked) {
    organizacaoNao.checked = false;
    opcoesorganizacoes.style.display = "block";
  } else {
    opcoesorganizacoes.style.display = "none";
  }
});

organizacaoNao.addEventListener('click', function() {
  if (this.checked) {
    organizacaoSim.checked = false;
    opcoesorganizacoes.style.display = "none";
  }
});