# INSTALAÇÃO e USO NO UBUNTU

# 1. criar ambiente virtual
# python3 -m venv venv

# 2. ativar o ambiente virtual
# source venv/bin/activate

# On macOS and Linux, you need to run python3:
# pip install pyautogui

# On Linux, additionally you need to install the scrot application, as well as Tkinter:

# sudo apt-get install scrot
# sudo apt-get install python3-tk
# sudo apt-get install python3-dev

# para pegar as coordenadas do mouse, usamos o mouseinfo

# pip install mouseinfo
# no terminal python (para acessar ele, digite python no terminal)

# from mouseinfo import mouseInfo
# mouseInfo()
# - vai abrir uma janela com várias opções
# - desmarque a opção 3 Sec. Button Delay
# - clique em Log XY(F6)
# pra usar vc vai até o ponto que quer com o mouse e aperta F6 no teclado
# isso vai gravas as coordenadas XY do mouse

# desafio:
# Encontre as coordenadas até o botão de fechar do navegador: 
# minhas coordenadas: 2619,45
