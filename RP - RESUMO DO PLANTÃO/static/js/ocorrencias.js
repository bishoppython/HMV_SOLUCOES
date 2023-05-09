var ocorrenciasSim = document.getElementsByClassName("ocorrencias-sim")[0];
var ocorrenciasNao = document.getElementsByClassName("ocorrencias-nao")[0];
const opcoesocorrencias = document.getElementById("ocorrencias-opcoes");

ocorrenciasSim.addEventListener('click', function() {
  if (this.checked) {
    ocorrenciasNao.checked = false;
    opcoesocorrencias.style.display = "block";
  } else {
    opcoesocorrencias.style.display = "none";
  }
});

ocorrenciasNao.addEventListener('click', function() {
  if (this.checked) {
    ocorrenciasSim.checked = false;
    opcoesocorrencias.style.display = "none";
  }
});

