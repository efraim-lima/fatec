========================
Administração de Sistemas Operacionais
========================

Informações sobre atividades e provas
-----------------------

A N1 é prova normal valendo 7 e outra atividade valendo 3, na N2 teremos um laboratorio de SO contendo adm de SO, Ingles e Empreededorismo;
A N2 valerá 7 pontos e todos os grupos precisarão de ao menos uma pessoa cursando todas as materiais.

A ideia é fazer um projeto criando um servidor para uma empresa "real" onde faremos todo o deploy de maneira semi real criando um projeto multidisciplinar com o objetivo de se usar todas as materias compreendidas em apenas um trabalho.

O professor perguntou a todos se temos conhecimento de script DOS

Pentesting com SQLInjection
###############################

O primeiro passo é verificar se o form está validando os inputs no cliente.
Uma boa maneira de se validar se o cliente está validando é inserindo um comando simples nos forms como ``\ 'or 1=1' --``, assim saberemos se existe validação no cliente, caso não haja podemos tentar montar uma query ao estilo:

.. code-block:: SQL

   -- textcode "and password=" .txtsenha

Caso esteja basta fazer o download do código fonte baixando seu HTML e buscar pelos form-actions de maneira a compreender os campos do form e o que cada um compreende.

Em posse deste conhecmento conseguimos elaborar uma query coerente com a organização deste form especificamente usando o REQBIN, dessa forma as queries redirecionarão diretamente para o banco de dados atraavés de uma requisição.

Muitas vezes os desenvolvedores acham que usar um simples captcha impossibilita uma série de ataques, mas isso é uma falácia pois esses sistemas podem ser bypassados com facilidade apenas enviando requests direto para o servidor.
