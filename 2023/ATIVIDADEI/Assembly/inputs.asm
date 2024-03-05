segment .data ; é apenas uma parte da sessão, para ficar isolado da sessâorigem

  LF        equ 0xA ; Line Feed, para trocar o final de cada string de 0xA para LF
  RET_EXIT  equ 0x0 ; Chamada de operação realizada com sucesso
  SYS_CALL  equ 0x80 ; Para enviar informação para 0x80
  NULL      equ 0xD ;  toda string recebe este ponteiro /null como default para para p final da cadeia de caracteres

  ; Chamadas armazenadas em EAX
  SYS_EXIT  equ 0x1 ; Chamada para finalizar
  SYS_READ  equ 0x3 ; Chamada para operação referente à leitura de input padrão do sistema
  SYS_WRITE equ 0x4 ; Chamada para operação referente à saida padrão do sistema

  ; Chamadas com valores de retorno em EBX
  RET_EXIT  equ 0x0 ; 
  STD_IN    equ 0x0 ; Mesmo tendo a saída como retorno de operação coloca-se para que redundância na entrada padrâorigem
  STD_OUT   equ 0x1 ; Saída padrão

section .data ; usado para dados que não se modificam ao decorrer do programa, como se fossem ass const
    ;msg: db "Hello World", 0xA   ; aqui tinhamos criado uma constante, mas agora podemos usar LF que foi criado no segment .data
    msg db "Entre com seu nome: ", LF, NULL ; LF criado em segment .data
    tam: equ $- msg              ; $- é uma forma de ler o tamanho automaticamente

section .bss ; usada para valores que podem se modificar durante o prograa, as 'variaveis'
  nom resb 1 ; aqui vamos armazenar o valor de byte em byte, resb indica que é 1 byte. Aqui 'criamos' a 'variavel' nome e faremos a entrada de byte em byte

section .text
  global _start

_start:
  mov EAX, SYS_WRITE ; indicando a saída do sistema
  mov EBX, STD_OUT
  mov ECX, msg
  mov EDX, tam
  int SYS_CALL

  mov EAX, SYS_READ ; indicando a entrada no sistema
  mov EBX, STD_IN
  mov ECX, msg
  mov EDX, 0xA ; etamos indicando a quantidade de caracteres que esperamos de input, caso coloquemos menos caracteres que o necessário está tudo tranquilo, caso coloquemos mais podemos ter erros (testar aqui depois)
  int SYS_CALL

  mov EAX, SYS_EXIT
  mov EBX, RET_EXIT
  int SYS_CALL


    ; Podemos criar um arquivo especial de forma obrigatória chamada makefile (acompanhar arquivo aqui no mesmo diretório)

    ; Para transformar o programa em linguegem de máquina precisamos aplicar o comando abaixo no terminal:
    ; nasm -f elf64 <programa>.asm 
    ; WINDOWS:
    ; nasm -f win64 <programa>.asm -o <programa>.o

    ; Aqui estamos linqueditando o programa:
    ; ld -s -o <programa> <programa>.o
    ; WINDOWS:
    ; ld <programa>.o -o <programa>.exe 
    
    ; Para rodar o programa no diretório  atual basta digitar:
    ; ./<nome_do_programa>

    ; repare que em elf64 estamos transformando o programa para linguagem de maquina na arquitetura 64bits
    ; se transformarmos em elf32 podemos ter problemas, então devemos sempre usar elf64
    ; Por exemplo: podemos usar os registradores RAX, RBX e afins para arquitetura 64bits,
    ; mas se compilarmos em 32bits não poderemos mudar os registradores
