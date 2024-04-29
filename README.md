# python-web

pip install virtualenv

## Dentro del ambiente virtual

    pip install reflex

# Si estas en Windows:

    - Para crear el enviroment se usa: python -m venv venv
        ó: py -m venv venv dentro de la carpeta del proyecto. Esto creara carpetas con las dependencias.
    - Luego hacer:
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
      Permitira que se puedan correr scripts en la computadora.
    - Y por ultimo, para levantar el ambiente, se utiliza:
      venv\Scripts\activate
      Para bajar el ambiente, se utiliza:
      desactivate

      Para correr la app Reflex:
        reflex run
      Para detener la app:
        Ctrl + c en el bash

# Si estas usando Linux:

    -Es todo lo mismo que con Windows y no hay que hacer el paso de los permisos, pero a la hora de ejecutar cambia.

    - Para ejecutar el ambiente se debe estar dentro de la carpeta link_bio y colocar lo siguiente:
      . venv/Scripts/activate
