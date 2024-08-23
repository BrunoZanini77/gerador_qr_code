from pathlib import Path
import os


diretorio_home = Path.home()

os.chdir(diretorio_home)
diretorio_projetos = f'{diretorio_home}/Projetos'
if os.path.exists(diretorio_projetos) == False:
    os.mkdir(diretorio_projetos)              
os.chdir(diretorio_projetos)

dir_novo_projeto = input('Digite o nome do Projeto a ser Criado:')
path_full_novo_projeto = f'{diretorio_projetos}/{dir_novo_projeto}'
if os.path.exists(path_full_novo_projeto) == False:
    os.mkdir(path_full_novo_projeto)
os.chdir(path_full_novo_projeto)

if os.path.isfile(f'{path_full_novo_projeto}/main.py') == False:
    os.mknod('main.py')
print(os.listdir())    
