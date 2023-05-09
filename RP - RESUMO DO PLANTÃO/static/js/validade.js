var validateSim = document.getElementsByClassName("validate-sim")[0];
var validateNao = document.getElementsByClassName("validate-nao")[0];

validateSim.addEventListener('click', function() {
  if (this.checked) {
    validateNao.checked = false;
  }
});

validateNao.addEventListener('click', function() {
  if (this.checked) {
    validateSim.checked = false;
  }
});
