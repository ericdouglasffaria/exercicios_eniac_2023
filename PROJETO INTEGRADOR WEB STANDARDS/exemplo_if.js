var idade1 = prompt('Digite a idade 1');
var idade2 = prompt('Digite a idade 2');
var idade3 = prompt('Digite a idade 3');

idade1 = eval(idade1);
idade2 = eval(idade2);
idade3 = eval(idade3);

if (idade1 <= idade2 && idade1 <= idade3) {
  if (idade2 <= idade3) {
    document.write(idade1 + ' - ' + idade2 + ' - ' + idade3);
  } else {
    document.write(idade1 + ' - ' + idade3 + ' - ' + idade2);
  }
} else {
  if (idade2 <= idade1 && idade2 <= idade3) {
    if (idade1 <= idade3) {
      document.write(idade2 + ' - ' + idade1 + ' - ' + idade3);
    } else {
      document.write(idade2 + ' - ' + idade3 + ' - ' + idade1);
    }
  } else {
    if (idade1 <= idade2) {
      document.write(idade3 + ' - ' + idade1 + ' - ' + idade2);
    } else {
      document.write(idade3 + ' - ' + idade2 + ' - ' + idade1);
    }
  }
}
