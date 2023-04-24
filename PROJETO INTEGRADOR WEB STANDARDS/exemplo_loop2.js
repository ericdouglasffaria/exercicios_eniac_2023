//-- for (inicio; condição, incremento){comando}; --//
let inicio = prompt('Digita um valor Inicial?');
let final = prompt('Digita o valor Final');

inicio = eval(inicio);
final = eval(final);

for (let cont = inicio; cont <= final; cont++) {
  document.write(cont + '<br>');
}
