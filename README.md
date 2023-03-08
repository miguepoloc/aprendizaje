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

## Errores comunes con Docker

### docker: invalid reference format. See 'docker run --help'.

Hace referencia a que al usar el pwd con el comando docker run, no se encuentra el directorio. Para solucionar este error, debe ejecutar el siguiente comando de ejemplo

```bash
docker run --rm -p 3000:3000 -v ${pwd}/index.js:/usr/src/index.js platziapp
```

Teniendo en cuenta que la expresión `${pwd}` reemplazada el directorio donde se ejecuta el comando 

## Contacto

miguelpoloac@unimagdalena.edu.co

miguepoloc@gmail.com