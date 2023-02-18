import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

# Iniciar ambiente virtual
print(f"{MESSAGE_COLOR}Creando el ambiente virtual{RESET_ALL}")
subprocess.call(['python', '-m', 'venv', 'venv'])

# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
python_venv = os.getcwd()+"\\venv\\Scripts\\python.exe"

print(f"{MESSAGE_COLOR}Instalando los requerimientos{RESET_ALL}")

subprocess.call([python_venv, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.call([python_venv, '-m', 'pip',
                'install', '-r', 'requirements.txt'])


# Configurar el ambiente para recibir notebooks.
if '{{ cookiecutter.project_packages }}' == 'All':
    subprocess.call([python_venv, '-m', 'ipykernel',
                    'install', '--user', '--name', 'venv'])

print(f"{MESSAGE_COLOR}Casi listo!")
print(f"Inicializando un respositorio en git...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', ':tada: Initial commit'])

print(f"{MESSAGE_COLOR}Todo listo para empezar a trabajar!{RESET_ALL}")