from pathlib import Path
import os
import subprocess

# BUSCAR NOME DA PASTA DE USUÁRIO
diretorio_home = Path.home()
# ENTRAR NA PASTA DE USUÁRIO
os.chdir(diretorio_home)

# VARIAVÉL PARA DIRETÓRIO PADRÃO DOS PROJETOS
diretorio_projetos = f'{diretorio_home}/Projetos'

# VERIFICA SE EXISTE O DIRETÓRIO PADRÃO CASO NÃO ELE O CRIA
if os.path.exists(diretorio_projetos) == False:
    os.mkdir(diretorio_projetos)

# ENTRA NO DIRETÓRIO PADRÃO
os.chdir(diretorio_projetos)

# SOLICITA AO USUÁRIO UM NOME PARA O PROJETO A SER CRIADO
dir_novo_projeto = input('Digite o nome do Projeto a ser criado: ')

# VARIÁVEL COM O CAMINHO COMPLETO DO PROJETO A SER CRIADO
path_full_novo_projeto = f'{diretorio_projetos}/{dir_novo_projeto}'

# CASO NÃO EXISTA O DIRETÓRIO CRIA
if os.path.exists(path_full_novo_projeto) == False:
    os.mkdir(path_full_novo_projeto)

# ENTRA NO DIRETÓRIO
os.chdir(path_full_novo_projeto)

# VERIFICA SE NA RAIZ DO PROJETO EXISTE UM ARQUIVO MAIN
# CASO NÃO ELE É CRIADO
if os.path.isfile(f'{path_full_novo_projeto}/main.py') == False:
    os.mknod('main.py')

# EXIBE O CAMINHO COMPLET DO NOVO PROJETO CRIADO
print(f'{path_full_novo_projeto}/main.py')

subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo apt install python3-pip''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo apt install python3-venv''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''python3 -m venv .venv''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''source .venv/bin/activate''', shell=True, check=True, executable='/bin/bash')
# ABRE O VS CODE NA PASTA DO PROJETO NOVO CRIADO
subprocess.run(f'''code {path_full_novo_projeto}''', shell=True, check=True, executable='/bin/bash')