var equipamentoSim = document.getElementsByClassName("equipamento-sim")[0];
var equipamentoNao = document.getElementsByClassName("equipamento-nao")[0];
const opcoesequipamento = document.getElementById("equipamento-opcoes");

equipamentoSim.addEventListener('click', function() {
  if (this.checked) {
    equipamentoNao.checked = false;
    opcoesequipamento.style.display = "block";
  } else {
    opcoesequipamento.style.display = "none";
  }
});

equipamentoNao.addEventListener('click', function() {
  if (this.checked) {
    equipamentoSim.checked = false;
    opcoesequipamento.style.display = "none";
  }
});

