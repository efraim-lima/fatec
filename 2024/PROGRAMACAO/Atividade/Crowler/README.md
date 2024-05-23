Algumas ações que este home broker pode fazer:

broker
	apresentar dados atuais do mercado

Lógica para comprar:
	fazer um request pela api da bolsa
	salvar como uma nova table no banco de dados
	verificar saldo
	
Lógica para vender:
	checar se existe este ativo na bolsa
	checar se existe quantidade na carteira do cliente
		se existir vender
		se não existir alertar que será feita uma venda à seco (perigosa)
		verificar o saldo
		comparar com o preço do ativo
		vender
