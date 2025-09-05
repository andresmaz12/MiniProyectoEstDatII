# MiniProyectoEstDatII

Proyecto  tablas hash simulador de un router

## Integrantes
### Andre Velasco - 1546124
### Andres Mazariegos - 1535724
### Jordin Garcia - 2427124
### Rocio Elizabeth Cojulum -

## Descripción del proyecto
### Obejtivos:
+ Desarollar habilidades para el trabajo en equipo
+ Reforzar el conocimiento de estrucutras de datos
+ Desorallar las habilidades para implementar tablas hash
+ Desarollar la habilidad para crear algoritmos 
+ Desarollar habilidades para encriptar y desencriptar datos
### Herramientas utilizadas:
+ Lenguaje de programación: Python 
+ Herramienta para el trabajo remoto y control de versiones: Github
+ Librerias externas: Operative System
### Distribución del trabajo: 
+ Tabla hash y metodo de desencriptamiento: Jordin Garica
+ Metodo main y menu principal: André Velzaco
+ Read me y control del repositorio: Andrés Mazariegos
+ Solución de errores y testeo del programa: Rocio Coujum

## Especificaciones tecnicas
### router_hash.py
En este archivo se encuentra la tabla hash y el desencriptador de dirección IP.
A nivel tecnico, tabla hash es de nivel 5, y el algoritmo usado es (IP encriptado) mod 5.
Para el manejo de colisiones, se utiliza sondeo lineal lo que garantiza que la tabla pueda almacenar datos cuyo valor sea el mismo sin necesidad de aumentar su nivel.
### main.py 
Este archivo contien el menú principal del progrma. En este se declara el nivel de la tabla hash, por lo que en caso de necesitarse es posible modificarlo.

