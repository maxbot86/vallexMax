# vallexMax

Este codigo es una extencion del codigo VALL-E-X , agregaando dos funciones para la creacion y entramiento de modelos de voces.
Luego de clonar el repositorio lo primero que hay que hacer es, instalar todas las librerias necesarias con pip:

pip install -r requirements.txt

El archivo esta ubicado en el directorio raiz del proyecto.

Luego se puede utilizar el archivo main.py para la creacion y entrenar los modelos de voces segun lo que necesitamos. 
Solo soporta de entrada y salidaa archivos en formato WAV.

Para el entrenamiento se puede o no pasar como parametro la transcripcion del texto que contiene el audio.

La  ruta de los modelos es ./customs  y poseen la extension ".npz".

Posterior a eso podemos recien comenzar a utilizar la generacion de audios con textos nuevos. 

Por ahora solo soporta idiomas en EN y JP.
