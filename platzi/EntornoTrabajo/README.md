# Para crear un nuevo proyecto con esta plantilla

Primero necesitas instalar cookiecutter usando pip

```bash
$ pip install cookiecutter
```

Luego ejecutar en la terminal

```bash
cookiecutter https://github.com/miguepoloc/aprendizaje/tree/main/platzi/EntornoTrabajo
```

## El proyecto creado contiene los siguientes archivos:

```
│   .gitignore
│   README.md
│   requirements.txt
│
├───data
│       .gitkeep
│
└───notebooks
        .gitkeep
```

## Para poder crear el archivo `requirements.txt` se debe ejecutar el siguiente comando:

```bash
pip freeze | Out-File -Encoding utf8 -FilePath requirements.txt
```
