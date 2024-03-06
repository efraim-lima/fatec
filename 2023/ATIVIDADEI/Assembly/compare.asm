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
  RET_EXIT  equ 0x0 ; return 0
  STD_IN    equ 0x0 ; Mesmo tendo a saída como retorno de operação coloca-se para que redundância na entrada padrâorigem
  STD_OUT   equ 0x1 ; Saída padrão

; Antes de compararmos algo em Assembly, precisamos conseguir compreender como funcionam as estruturas de dados na ferramenta e depois como funcionam as comparações entre dados na ferramenta. Aqui na seção .data trabalharemos com alguns recursos e vamos lidar com eles a partir de agora.

; Estruturas de Dados:
; db = 1B = define byte
; dw = 2B = define word, seria equivalente ao 'char' em outras linguagens
; dd = 4B = define double word, equivalente ao 'short'/'int' em outras linguagens
; dq = 8B = define quad words 
; dt = 10B = define ten words

section .data ; usado para dados que não se modificam ao decorrer do programa, como se fossem ass constantes
  x dd 50
  y dd 10
  msg1 db "X é maior que Y", 0xA, 0xD ; constante msg1 e passamos o equivalente a Line Feed junto ao Null na mensagem
  tam equ $- msg1 ; determinando o tamanho de msg1, isso sempre precisa ser feito na linha em seguida à db
  msg2 db "Y eh maior que X", 0xA, 0xD ; constante msg2 e passamos equivalente ao Line Feed junto ao Null na mensagem
  tam2 equ $- msg2 ; determinando o tamanho de msg2, novamente feito logo abaixo de setar msg2 db

section .text
  global _start

_start:
; Para tratarmos dados presentes na seção .data em outra seção do código precisamos pegar os dados provenientes de .data e inserir eles em registradores OBRIGATÓRIAMENTE, ou seja, todo processamento ocorre unicamente dentro dos registradores e por isso precisamos importar nossos dados de .data. Sem isso não conseguimos analisar valores no código.
; Portanto usamos um ponteiro chamado DWORD[], onde podemos passar constantes pra dentro dele.

  mov EAX, DWORD[x]
  mov EBX, DWORD[y]

; Comparações
; Em Assembly não temos if(), para compararmos valores precisamos usar lógicas de compare e jump, mas em Assembly temos jumps que não são mais usados (foram banidos) em outras linguagens, um exemplo é o "Go To' do Java que está na sintaxe mass é uma palavra reservada cujo não podemos usar.

  cmp EAX, EBX ; cmp == compare; estamos comparando os valores presentes nos registradores EAX e EBX, mas aqui estamos apenas colocando os registradores na fila e olhando para os dois, ainda não estamos comparando nada, para isso precisamos dos comparadores condicionais.

;  Comparação Condicional
; je  = ==  jump equal
; jg  = >   jump greater
; jge = >=  jump greater equal
; jl  = <   jump lower
; jle = <=  jump lower equal
; jne = !=  jump not equal

; Comparação incondicional
; relembrando que o uso de alguns dos jumps de Assembly não são mais permitidos e/ou presentes em outras lingagens
; jmp = "go to" do Java

 ; cmp seguido de j** é semelhante ao if(j**), ele vai saltar para a condição setada em seguida, no caso aqui seria maior.
  ; repare que ainda não setamos o que é 'maior', mas aqui ja seria o que satisfaz a condição
  jge maior ; seria o equivalente a if(EAX >= EBX)
  ; Aqui nesta parte seria o famoso 'else', ou seja, o que é feito quando a condição anterior não foi atendida
  mov ECX, msg2
  mov EDX, tam2
  jmp final ; esta condição é criada para evitar de as instruções abaixo, ou seja, 'maior', sejam atendidas pelo processador, pois não não neccessárias

  ; aqui sim estamos considerando o que seria 'maior' na seção j** e o que ocorre quando a condição foi atendida em j**
maior:
  mov ECX, msg1
  mov EDX, msg1

final:
  mov EAX, 0x4 ; equivalente ao SYS_WRITE, ou seja, direcionamento para saída padrão do sistema
  mov EBX, 0x0 ; equivalente ao STD_OUT ou saída padrão
  int 0x80 ; equivalente ao SYS_CALL, informando a execução do bloco


; Para a execução final do código vamos aprender um pouco mais sobre comparadores.
; Em assembly temos comparadores and, or e xor
; and = movimentação de comparação de bits, entendendo:

; Tomando os numeros 7 e 5 como exemplo teremos seus binários 0111 e 0101 respectivamente
; abaixo segue uma tabela informativa de como funciona o and, or e xor


;     and   or    xor
; 7   0111  0111  0111
; 5   0101  0101  0101
; tv  0101  0111  0010
; dc    5     7     2
  

; tv => tabela verdade comparativa (bits ligados e desligados)

; and   - bit liga quando ambos os bits estão ligados
; or    - bit liga quando AO MENOS um bit está ligado
; xor   - bit liga apenas quando APENAS um bit está ligado


  mov EAX, 0x1 ; equivalente ao SYS_EXIT, ou seja, a chamada para finalizar
;  mov EBX, 0x0 ; equivalente ao RET_EXIT, ou seja, return 0
  xor EBX, EBX ; super importante esta notação, ela indica  que EBX retornou um valor 0 e substitui o comando anterior
  int 0x80 ; equivalente ao SYS_CALL, informando a execução do comando

