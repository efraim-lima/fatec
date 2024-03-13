%include "lib.inc"

section .text
  global _start

  _start:
  ; ---> Load Effective Address => ele associa um registro de memória no dss no registrador   
  lea esi, [BUFFER]; Estamos lincando o Buffer ao esi, ou seja, sempre que enviarmos algo para esi estaremos enviando para o BUFFER
  add esi, 0x9 ; Estamos vinculando o valor 0x9 ao esi, 0x9 é o começo de uma string em hexa
  mov byte[esi], 0xA
  ; => tudo acima significa  que temos nada e '\n' em esi, precisamos conseguir inserir a letra à esquerda de 0xA
  dec esi ; movimenta esi um registrador para trás 
  mov dl, 0x11 ; caractere 'A' em hexa, pois em assembly não existem caracteres para entradas e saídas muito embora sejam estritamente strings
  add dl, '0' ; estamos transformando 0x11 presente em dl em um caractere
  mov [esi], dl ; agora movimentamos dl para esi

  call saidaResultado ; estamos especificando a saida da movimentação saidaResultado em lin.inc

  mov EAX, 0x1 
  mov EBX, 0x0 
  int 0x80
