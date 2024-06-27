#!/bin/bash

# Para que este script funcione:

# sudo curl -L https://raw.githubusercontent.com/efraim-lima/fatec/main/2024/REDES/GNS3/init.sh -o /tmp/init.sh && sudo chmod +x /tmp/init.sh && sudo bash -x /tmp/init.sh

# VARIÁVEIS
IP=20.0.0.2
IPR=0.0.20
DNSA=$IP
DNS1=20.0.0.2
DNS2=20.0.0.3
GATEWAY=20.0.0.1
DOMINIO="pastel.com"
HOSTNAME="mail.$DOMINIO"
MAILNAME=$DOMINIO
ZONAS_IP="/etc/bind/db.$IPR"
ZONAS_DOMINIO="/etc/bind/db.pastel.com"
NETPLAN=$(find /etc/netplan/ -type f -name "*.yaml" | head -n 1)
MAIL_USER="efraim" #usuário de email
MAIL_PASSWORD="12345" #senha de email

sudo apt update
sudo apt install -qq --show-progress bind9 dnsutils apache2 postfix dovecot-core dovecot-imapd dovecot-pop3d dovecot-lmtpd -y 

debconf-set-selections <<< "postfix postfix/mailname string $DOMINIO"
debconf-set-selections <<< "postfix postfix/main_mailer_type string 'Internet Site'"

sudo cp /etc/bind/db.local /etc/bind/db.pastel.com
sudo cp /etc/bind/db.127 /etc/bind/db.20.0.0


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
@       IN      NS      ns1.pastel.com.
@       IN      NS      ns2.pastel.com.
2       IN      PTR     pastel.com.
2       IN      PTR     www.pastel.com.
2       IN      PTR     ns1.pastel.com.
3       IN      PTR     ns2.pastel.com.
2       IN      PTR     mail.pastel.com.
3       IN      PTR     mail.pastel.com.
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
$TTL    604800
@       IN      SOA     ns1.pastel.com. root.pastel.com. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL

@       IN      NS      ns1.pastel.com.
@       IN      NS      ns2.pastel.com.
@       IN      MX      10 mail.pastel.com.
@       IN      A       $IP
www     IN      A       $IP
ns1     IN      A       20.0.0.2
ns2     IN      A       20.0.0.3
mail    IN      A       20.0.0.2
mail    IN      A       20.0.0.3
;
EOT"

sudo bash -c "cat > /etc/bind/named.conf.local << 'EOT'
zone "$DOMINIO" {
    type master;
    file "$ZONAS_DOMINIO";
    allow-transfer { $DNSA; };
};    
zone "$IPR.in-addr.arpa" {
    type master;
    file "$ZONAS_IP";
    allow-transfer { $DNSA; };
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
sudo sed -i '/dhcp4: false/a\         addresses:\n	- '$IP'/24	routes:\n         - to: default\n           via: '$GATEWAY'\n         nameservers:\n           addresses:\n             - '$DNS1'\n             - '$DNS2'' "$NETPLAN"

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

# Configurar o Dovecot
echo "protocols = imap pop3 lmtp" >> /etc/dovecot/dovecot.conf

sudo cat << EOL >> /etc/dovecot/conf.d/10-mail.conf
mail_location = maildir:~/Maildir
disable_plaintext_auth = no
auth_mechanisms = plain login
EOL

sudo cat << EOL >> /etc/dovecot/conf.d/10-ssl.conf 
ssl = no
EOL

DIR=$(dirname "$ZONAS_DOMINIO")
if [ ! -d "$DIR" ]; then
    sudo mkdir -p "$DIR"
fi

PATHDOVECOT="/etc/dovecot/conf.d/10-master.conf"
cat << EOL >> $PATHDOVECOT
service imap-login {
  inet_listener imap {
    port = 143
  }
}

service pop3-login {
  inet_listener pop3 {
    port = 110
  }
}
EOL

configure_postfix
add_mail_user

sudo systemctl restart bind9.service
sudo systemctl restart apache2.service
sudo systemctl restart postfix.service
sudo systemctl restart dovecot.service

#telnet localhost pop3
