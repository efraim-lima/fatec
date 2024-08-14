
Umaa boa maneira de compreender a máscara de rede representada por /XX é entender que este número é o referente à quantidade de bits ativos na máscara, um exemplo mais simples seria um endereço de máscara /4, que seria representado pelos bits: 11110000.00000000.00000000.00000000

Vamos compreender por qual motivo um IP 172.16.2.99 não consegue pingar um servidor 172.16.0.2/23.

Para isso vamos compreender primeiro como o range de endereços IP no servidor se comportam de forma física e lógica

.. code-block:: bash

        IP              172.16.0.0
        Máscara         255.255.254.0
        Bin             11111111.11111111.11111110.00000000

Compreendemos o processo de conversão das máscaras de IP, agora vamos compreender como ler a quantidade de hosts disponíveis neste range, para isso precisamos analisar quantos espaços lógicos estão disponíveis para uso, para isso invertemos os 0 e os 1 da máscara de rede, com isso teremos:

.. code-block:: bash

        REDE
        ID              172.16.0.0
        Máscara         255.255.254.0
        Bin             11111111.11111111.11111110.00000000
        Hosts Bin       00000000.00000000.00000001.11111111
        Hosts Dec       0.0.1.255
        Limite IP       172.16.1.255

Com isso podemos entender que poderemos usar IPs até o limite do faixa que seria 172.16.1.255, assim conseguimos alinhar 

VLAN são usadas para segurança, desempenho e organização da rede

Quando precisamos fazer com que elementos de redes lógicas diferentes, mas presentes na mesma rede fisica se comuniquem precisamos usar o função router sendo de switches ou outros equipamentos.
