sudo apt update
sudo apt install bind9 dnsutils apache2 postfix dovecot-imapd dovecot-pop3d -y

touch /etc/bind/db.<site>.com
sudo cp /etc/bind/db.local /etc/bind/db.<site>.com
vi /etc/bind/db.<site>.com

sudo cp /etc/bind/db.127 /etc/bind/db.20.0.0
sudo vi /etc/bind/db.20.0.0

";
; BIND reverse data file for local 192.168.1.XXX net
;
$TTL    604800
@       IN      SOA     ns.example.com. root.example.com. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns.
10      IN      PTR     ns.example.com."


sudo vi /etc/bind/named.conf.local

"zone "example.com" {
    type master;
    file "/etc/bind/db.example.com";
    allow-transfer { 192.168.1.11; };
};
    
zone "1.168.192.in-addr.arpa" {
    type master;
    file "/etc/bind/db.192";
    allow-transfer { 192.168.1.11; };
};"

vi /etc/netplan/<arqivo>

network:
   version: 2
   ethernets:
      eth0:
         addresses:
         - 20.0.0.3/24
         dhcp4: false
         routes: 
         - to: default
           via: 20.0.0.1
	 nameservers:
	   addresses:
	     - 20.0.0.2
	     - 20.0.0.3

sudo netplan try

sudo sustemctl restart bind9.service
sudo systemctl restart apache2


################################################################################################################################################################################################################################################################################################################################################################################################################


MAIL
sudo dpkg-reconfigure postfix

Marcar:
"
Internet Site
mail.pastel.com
steve
mail.pastel.com, localhost.localdomain, localhost
No
127.0.0.0/8 \[::ffff:127.0.0.0\]/104 \[::1\]/128 20.0.0.0/24
0
+
all
"

sudo vi /etc/postfix/main.cf

sudo vi /etc/dovecot/dovecot.conf
sudo vi /etc/dovecot/conf.d/

sudo systemctl restart postfix.service
sudo systemctl restart dovecot.service

telnet localhost pop3


