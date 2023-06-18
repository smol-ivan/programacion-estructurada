[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)

# Proyecto

## Descripcion General del Proyecto {#descipcion-general}

El presente proyecto tiene como objetivo principal actualizar el sistema de renta y venta de un servicio de streaming. Se requiere desarrollar un programa que permita una interaccion eficiente y sencilla que permitan la manipulacion del catalogo de productos.

El sistema proporcionara una serie de menus que faciliten la manipulacion y gestion de los catalogos de produtos. Quien acceda al sistema podran acceder a algun catalogo, agregar/eliminar productos, realizar una busquedas y visualizar informacion detallada sobre los productos

Algunas de las funcionalidades del programa incluyen la carga inicial del catalogo que se encuentre almacenado en un archivo, capacidad de agregar o eliminar productos, busqueda por palabras clave del titulo, y la opcion de mostrar, guardar y cargar un catalogo

## Tabla de contenidos

- [Proyecto](#proyecto)
  - [Descripcion General del Proyecto](#descripcion-general-del-proyecto-descipcion-general)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Estructura del proyecto](#estructura-del-proyecto-estructura-proyecto)
  - [Funciones](#funciones-funciones)
  - [Consideraciones](#consideraciones)
  - [Intruciones de uso](#intruciones-de-uso)

## Estructura del proyecto 

![top-down diagrame de estructura](./img/diagrama.png)
<sub>_**click [aqui](https://www.figma.com/file/gGUbw0SLhhbP5NFplgt1iu/Untitled?type=whiteboard&node-id=0%3A1&t=IFf8Mpjt3Wv4rbxZ-1) para revisar el diagrama en mejor resolucion**_</sub>

## Funciones 

Click [aqui](./funciones.md) para ir a las funciones

## Consideraciones

- **_Busqueda de productos_**
    La busqueda de productos se basasa en palabras clave del titulo. La coincidenciia de las palabras clave puede no ser precisa, por lo que se podran no encontrar todos los productos si las palabras no coinciden exactamente con el titulo o si los prodcutos no estan bien escritos.
- **_Eliminacion de prodcutos_**
    El sistema no valida si hay productos duplicados y la eliminacion se hace cuando se encuentra un unico producto, por lo que existiria un problema con esta funcion si existen prodcutos duplicados.
- **_Escalabilidad_**
    El sistema trabaja con un catalgo y estrcutura especifica para todos los productos, si se deseara expandir el catalogo para incluir mas categorias, se tienen que hacer varias modificaciones adicionales para que se pueda escalar.

## Intruciones de uso

1. Para hacer uso del sistema de catalogos, solo basta con tener python instalado en el sistema, y tener descargados los archivos del repositorio
2. Para iniciar el programa basta con abrir la terminal en donde se encuentrar los archivos .py y escribir:

        ```cmd
        py catalogo.py
        ```
3. Una vez desplegado el menu principal, se tiene que cargar el archivo donde se encuentre el catalogo, esto escogiendo la opcion no.5 (El programa puede crear un achivo nuevo con un catalogo vacio si es que no se cuenta con un archivo previo).
4. Para hacer uso de la manipulacion y control del catalogo basta con escoger una opcion(agregar,eliminar, mostrar catalogo, buscar) para despues seguir las instrucciones que el sistema vaya pidiendo
5. Una vez terminada la manipulacion del catalogo, se tendran que guardar los cambios hechos seleccionando la opcion no.6 del menu principal.
