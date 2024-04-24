# python-web

Si estas en Windows:
  - Para crear el enviroment se usa: python -m venv venv
    ó: py -m venv venv) dentro de la carpeta del proyecto. Esto creara carpetas con las dependencias.
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
