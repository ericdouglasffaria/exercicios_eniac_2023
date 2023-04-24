function verificar() {
  var enviar = true;
  var n = document.form1.txtNome.value;
  if (n.length == 0) {
    enviar = false;
    document.querySelector('#erroNome').textContent =
      'Preencher o Campo com nome?';
  }
  if (enviar) {
    document.form1.submit();
  }
}
