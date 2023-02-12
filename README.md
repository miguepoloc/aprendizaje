# Entorno de pruebas y aprendizaje de Miguel Polo

Este repositorio enmarca las pruebas que desarrollo en mis momentos de aprendizaje

## Instalación Python

En los entornos de trabajo con python, debe crear un entorno virtual

```bash
python -m venv venv
```

Para instalar los requerimientos utilizando [pip](https://pip.pypa.io/en/stable/).

```bash
pip install -r requirements.txt
```

En caso tal de que se instalen nuevas librerías se debe ejecutar el siguiente comando para actualizar las librerías

```bash
pip freeze > requirements.txt
```

## Instalación Node

En los entornos de trabajo con Node (React), primeramente debe ejecutar el comando

```bash
npm install
```

En algunos casos, si falla por versión de las librerías debe colocar

```bash
npm install --legacy-peer-deps
```

## Contacto

miguelpoloac@unimagdalena.edu.co

miguepoloc@gmail.com