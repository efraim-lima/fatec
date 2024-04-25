#!/bin/bash

source .env

# Verifica se o script foi desabilitado com chmod -x
if [ ! -x "$0" ]; then
  echo "Habilitando script"  
  chmod +x "$0"
fi

# Verifica se o script já é um serviço
if [ sudo -f /etc/systemd/system/opening.service ]; then
    echo "Service running"
else
    echo "Criando o serviço..."
    sudo touch /etc/systemd/system/opening.service
    sudo cat <<EOF > /etc/systemd/system/opening.service
[Unit]
Description=Inicializando terminais e navegador
After=network.target

[Service]
Type=simple
User=$USER
ExecStart=sudo bash -c 'echo "$PWD/opening.sh" > /dev/pts/0'
Restart=always

[Install]
WantedBy=multi-user.target
EOF

    sudo systemctl daemon-reload
    sudo systemctl unmask opening.service
    sudo systemctl enable opening.service
    sudo systemctl start opening.service
fi

# Restante do script
# Abre 3 terminais
gnome-terminal --geometry=60x24-0+0 &&
gnome-terminal --geometry=60x24-0+0 &&
gnome-terminal --geometry=60x100+0-0 -- bash -c 'echo "cd ~/Documents/GitHub/fatec/2024/" > /dev/pts/0'&

# Aguarda um curto período para garantir que os terminais estejam abertos
sleep 1

firefox &
