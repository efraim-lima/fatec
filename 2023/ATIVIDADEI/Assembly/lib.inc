segment .data ; é apenas uma parte da sessão, para ficar isolado da sessâorigem

  LF        equ 0xA /* Line Feed, para trocar o final de cada string de 0xA para LF*/
  RET_EXIT  equ 0x0 /*; Chamada de operação realizada com sucesso*/
  SYS_CALL  equ 0x80 /*; Para enviar informação para 0x80*/
  NULL      equ 0xD /*;  toda string recebe este ponteiro /null como default para para p final da cadeia de caracteres*/

  /*; Chamadas armazenadas em EAX*/
  SYS_EXIT  equ 0x1 /*; Chamada para finalizar*/
  SYS_READ  equ 0x3 /*; Chamada para operação referente à leitura de input padrão do sistema*/
  SYS_WRITE equ 0x4 /*; Chamada para operação referente à saida padrão do sistema*/

/*  ; Chamadas com valores de retorno em EBX*/
  RET_EXIT  equ 0x0 /*; return 0*/
  STD_IN    equ 0x0 /*; Mesmo tendo a saída como retorno de operação coloca-se para que redundância na entrada padrâorigem*/
  STD_OUT   equ 0x1 /*; Saída padrão */
  BUFFER_SIZE equ 0xA

segment .bss
  BUFFER resb 0x1

/* ; Assembly não possui funções, possui saltos, ou seja, ele vai de um ponto para outro, por isso o nome correto é marcador. */
segment .text
  saidaResultado:
  /*  jmp -> GOTO para um ponto do código e de lá ele não volta
      call -> GOSUB, vai para um ponto e, ao encontrar ret (return), volta para o ponto de call

  *por isso chamamos 'saidaResultado' de "função", mas é apenas um return */
  mov EAX, 0x4
  mov EBX, 0x1 /* se mantivermos apenas estas duas instruções precisariamos popular ECX e EDX com a mensagem e seu tamanho*/
  mov ECX, BUFFER
  mov EDC, BUFFER_SIZE
  ret 
