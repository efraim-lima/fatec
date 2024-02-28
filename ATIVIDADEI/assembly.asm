section .data
    msg: db "Hello World", 0xA   ; aqui estamos criando uma constante e 0xA (valor 10) é o caractere de nova linha.
    tam: equ $- msg              ; $- é uma forma de ler o tamanho automaticamente

section .text
    global _start

_start:
    ; Lembrar da sintaxe: destino, origem
    ; Lembrar que os números precisam ser na base hexadecimal:
    ; 0 1 2 3 4 5 6 7 8 9 A B C D E F
   
    mov RAX, 0x4 ; Aqui estamos informando que vamos usar a função printString do kernel
    mov RBX, 0x1 ; Aqui estamos informando o sistema que usaremos a saída padrão
    mov RCX, msg ; Aqui estamos passando o elemento PAI (pai direto) para a função write
    mov RDX, tam ; Aqui estamos passando o elemento FILHO (filho direto), ou seja, o comprimento da string
    int 0x80     ; Chamada a sistema para finalizar o processo


    mov RAX, 0x1 ; Aqmsgestamos informando o SO que estamos terminando o programa
    mov RBX, 0x0 ; Aqui estamos informando o SO que o retorno é 0, ou seja, concluiu sem erros
    int 0x80     ; Chamada a sistema para finalizar o processo

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