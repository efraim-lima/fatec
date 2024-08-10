**CRIPTOGRAFIA**

====================
AULA INAUGURAL
====================

Notas gerais 
####################

O curso de criptografia possuirá apresentações de seminários antes das provas contendo coteúdos especificos que abordem a matéria como um todo, por exemplo:

        Forense Computacional, Vulnerabilidades de Criptografia, Formas de Criptografia, CTF, Web Hacking, Engenharia Social, Desenvolvimento de Exploits, Aplicações de Seurança com Python, Segurança na Nuvem, Wifi Hacking, Aplicações com Criptografia usando CTF.

As apressentações terão critérios para a apresentação, sendo um tempo de 20 a 30 minutos e contendo uma apresentação PowerPoint


Conteúdo
###################

A segurança da informação possui não apenas o CID, mas também o cubo da seguraça da informçáo, que consiste de:

* **1ª face** - Pincipios de Segurança: Confidencialidade, Integridade, Disponibilidde
* **2ª face** - Estado dos Dados: Peocessamento armazenamento (em repouso) trasmissão
* **3ª face** - Contramedidas ou Tecnologias: Tecnlogia, Politicas e processos, Pessoas

Na parte de estados dos dados teremos um processo de criptografia para cada etapa;

https://threatmap.checkpoint.com
https://threatmap.fortiguard.com
https://cvedetails.com
https://exploit-db.com

Algo que pode ser util em conceito de processos é: primeiro fazer uma leitura de serviços presentes na rede usando o nmap e, a partir do levantmento dos serviços basta usar o https://exploit-db.com para levantar se aquele serviço e aquela versão possuem alguma vulnerabilidade

Algo que pode ser util em conceito de processos é: primeiro fazer uma leitura de serviços presentes na rede usando o nmap e, a partir do levantmento dos serviços basta usar o exploit-db.com para levantar se aquele serviço e aquela versão possuem alguma vulnerabilidade.

cert.br apresenta estatistica de riscos na internet compilado em forma de dados.

Publicações de segurança com repercussão na midia podem ser encontrados nos sites da Security Report e IBRASPD

Pesquisar sobre os 10 mandamentos da ética profissional e de computadores

Uma boa ferramenta para fazermos testes e laboratórios de pentesting seja em rede, seja em web e muitos outros recursos é acessando o os laboratórios da Wargames através do website: https://overthewire.org/wargames/

TEORICO
##################

A primeira forma de cifra da história foi através dos sistemas monoalfabeticos, hot13, cifra de caesar

Análise da cifra de caesar:
**Para encriptar** l' = (l+ch)mod26
**Para decriptar** l = (l'-ch)mod26

l = letra
ch = caracteres
mod26 = modulado pelas 26 letras do alfabeto

Depois craram-se os modos de criptografia em modos polialfabeticos (vigenère), que pode ser representado por um calculo, mas é mais fácil termos uma visão em tabela do mesmo, pois esssa criptografia consiste em criar multiplos alfabetos diferentes deslocando sempre uma letra para frennte no próximo, assim conseguimos determinar como seria a mensagem a partir da posição pré-determinada; um exemplo de como seria o alfabeto:

abcdefghijklmnoprst
bcdefghijklmnopqstu
cdefghijklmnopqrtuv
defghijklmnopqrsuvx
efghijklmnopqrstvxw
fghijklmnopqrstuxwy
ghijklmnopqrstuvwyz
.
.
.

Posteriormente começaram a criar dispositivos criptograficos como a maquina enigma durante a segunda guerra mundial, onde Allan Touring conseguiu desenvolver uma maquina que resolvesse a enigma e o considerado primeiro computador criado.

Um processo de criptoanalise é através de métodos estatísticos que determinam a ocorrencia de cada letra em um determinado idioma de forma a se estabelecer padrões em alguns idiomas.

Desenvolveram em 1920 o teste kappa e teste phi, que podem ser utilizados para decriptar textos; o teste kappa determina a probabilidade de cada letra aparecer em um evento único (ou seja, 1/26 ou 0.0385), já o teste phi analisa a incidencia de cada caracter em um dado idioma, o tamanho da mensagem, um phi randomico e a partir disso determiinar se o texto é transposto ou substituido.

* **estudar teste phi**

Existem ferramentas de decriptografia de cifra de caesar.

Existe uma formma de codificação nomeada base64 que basea-se nos bytes, mas como em base64 as letras necessitam apenas de 6 bits, com isso a outra letra subsequente já se iniciaria no 2 ultimos bits do mesmo byte, fazendo com que a resposta seja sempre menor do que a pergunta, com isso sempre podem acabar sobrando alguns bits no final da mensagem que frequentemente precisam ser completados por "==", caracterizando claramente uma cifra em base64.

Podemos fazer um teste disso no linux através do comando: ``echo -n "Texto a ser encriptado" | base64``
