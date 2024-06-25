#!/bin/bash

# Para que este script funcione:

# sudo wget https://github.com/efraim-lima/fatec/tree/bdff8707db839deede8575e0856ec31d96c47f4d/2024/REDES/GNS3/init.sh -O /tmp/init.sh
# sudo chmod +x /tmp/init.sh
# sudo /tmp/init.sh

sudo apt update
sudo apt install -qq --show-progress bind9 dnsutils apache2 postfix dovecot-imapd dovecot-pop3d -y 

sudo cp /etc/bind/db.local /etc/bind/db.pastel.com
sudo cp /etc/bind/db.127 /etc/bind/db.20.0.0

# Caminho do arquivo de configuração
IP=20.0.0.2
IPR=0.0.20
DNS1=20.0.0.2
DNS2=20.0.0.3
DOMINIO="pastel.com"
HOSTNAME="mail.example.com"
MAILNAME=$DOMINIO
ZONAS_IP="/etc/bind/db.20.0.0"
ZONAS_DOMINIO="/etc/bind/db.pastel.com"
NETPLAN=$(find /etc/netplan/ -type f -name "*.yaml" | head -n 1)

#usuários de email
MAIL_USER="postfix_user"
MAIL_PASSWORD="password"

# Verifica se o diretório existe, senão cria
DIR=$(dirname "$ZONAS_IP")
if [ ! -d "$DIR" ]; then
    sudo mkdir -p "$DIR"
fi

# Cria o arquivo de configuração do BIND com o conteúdo especificado
sudo bash -c "cat > $ZONAS_IP << 'EOT'
; BIND reverso para rede do IP local
;
\$TTL    604800
@	IN	SOA	ns.pastel.com.	root.pastel.com. (
			2		; Serial
			604800		; Refresh
			86400		; Retry
			2419200		; Expire
			604800 )	; Negative Cache TTL
;
@	IN	NS	ns1.pastel.com.
@	IN	NS	ns2.pastel.com.
;
2	IN	MX	mail.pastel.com.
3	IN	MX	mail.pastel.com.
2	IN	NS	ns1.pastel.com.
2	IN	PTR	www.pastel.com.
3	IN	NS	ns2.pastel.com.
3	IN	PTR	www.pastel.com.
;
EOT"

DIR=$(dirname "$ZONAS_DOMINIO")
if [ ! -d "$DIR" ]; then
    sudo mkdir -p "$DIR"
fi

# Cria o arquivo de configuração do BIND com o conteúdo especificado
sudo bash -c "cat > $ZONAS_DOMINIO << 'EOT'
; BIND reverso para rede do IP local
;
\$TTL    604800
@	IN	SOA	ns.pastel.com.	root.pastel.com. (
			2		; Serial
			604800		; Refresh
			86400		; Retry
			2419200		; Expire
			604800 )	; Negative Cache TTL
;
@	IN	NS	ns1.pastel.com.
@	IN	NS	ns2.pastel.com.
;
2	IN	MX	mail.pastel.com.
3	IN	MX	mail.pastel.com.
2	IN	NS	ns1.pastel.com.
2	IN	PTR	www.pastel.com.
3	IN	NS	ns2.pastel.com.
3	IN	PTR	www.pastel.com.
;
EOT"

sudo bash -c "cat > << 'EOT'
zone $DOMINIO {
    type master;
    file $ZONAS_DOMINIO;
    allow-transfer { $DNS1; };
};    
zone "$IPR.in-addr.arpa" {
    type master;
    file $ZONAS_IP;
    allow-transfer { $DNS1; };
};
EOT"

# Verifica se um arquivo foi encontrado
if [ -z "$NETPLAN" ]; then
    echo "Nenhum arquivo .yaml encontrado na pasta /etc/netplan/"
    exit 1
fi

# Faz backup do arquivo original
sudo cp "$NETPLAN" "${NETPLAN}.bak"

# Usa 'sed' para alterar a linha 'dhcp4' e adicionar 'routes' e 'nameservers'
sudo sed -i '/dhcp4: true/c\         dhcp4: false' "$NETPLAN"

# Adiciona as linhas após 'dhcp4: false'
sudo sed -i '/dhcp4: false/a\         routes:\n         - to: default\n           via: 20.0.0.1\n         nameservers:\n           addresses:\n             - 20.0.0.2\n             - 20.0.0.3' "$NETPLAN"

# Mostra o conteúdo do arquivo modificado
sudo cat "$NETPLAN"

echo "Configurações de rede atualizadas no arquivo $NETPLAN."

sudo netplan apply

###################################################################################################################################
############################################################## MAIL ###############################################################
###################################################################################################################################

#sudo dpkg-reconfigure postfix

#Marcar:
#"
#Internet Site
#mail.pastel.com
#steve
#mail.pastel.com, localhost.localdomain, localhost
#No
#127.0.0.0/8 \[::ffff:127.0.0.0\]/104 \[::1\]/128 20.0.0.0/24
#0
#+
#all
#"

# Função para configurar o Postfix
configure_postfix() {
    echo "Configurando o Postfix..."
    sudo postconf -e "myhostname = $HOSTNAME"
    sudo postconf -e "mydomain = $DOMINIO"
    sudo postconf -e "myorigin = /etc/mailname"
    sudo postconf -e "relayhost ="
    sudo postconf -e "mynetworks = 127.0.0.0/8"
    sudo postconf -e "mailbox_size_limit = 0"
    sudo postconf -e "recipient_delimiter = +"
    sudo postconf -e "inet_interfaces = all"
    sudo postconf -e "inet_protocols = ipv4"
    
    # Atualiza o arquivo /etc/mailname
    echo "$MAILNAME" | sudo tee /etc/mailname
    
    # Configura a autenticação SMTP (opcional)
    sudo postconf -e "smtpd_sasl_auth_enable = yes"
    sudo postconf -e "smtpd_tls_cert_file = /etc/ssl/certs/ssl-cert-snakeoil.pem"
    sudo postconf -e "smtpd_tls_key_file = /etc/ssl/private/ssl-cert-snakeoil.key"
    sudo postconf -e "smtpd_use_tls = yes"
    sudo postconf -e "smtpd_sasl_security_options = noanonymous"
    sudo postconf -e "smtpd_sasl_local_domain = $DOMINIO"
    sudo postconf -e "broken_sasl_auth_clients = yes"
    sudo postconf -e "smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination"
    sudo postconf -e "mydestination = $MAILNAME, $HOSTNAME, localhost.$DOMINIO, localhost"
}

# Função para adicionar usuário de e-mail (opcional)
add_mail_user() {
    echo "Adicionando usuário de e-mail..."
    sudo useradd $MAIL_USER
    echo "$MAIL_USER:$MAIL_PASSWORD" | sudo chpasswd
    sudo mkdir -p /home/$MAIL_USER/Maildir
    sudo chown -R $MAIL_USER:$MAIL_USER /home/$MAIL_USER/Maildir
    sudo postconf -e "home_mailbox = Maildir/"
}

configure_postfix
add_mail_user

sudo systemctl restart bind9
sudo systemctl restart apache2
sudo systemctl restart postfix.service
sudo systemctl restart dovecot.service

#telnet localhost pop3
