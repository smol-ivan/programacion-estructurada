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
  - [Funciones {#funciones}](#funciones-funciones)
  - [Consideraciones](#consideraciones)
  - [Intruciones de uso](#intruciones-de-uso)

## Estructura del proyecto 

![top-down diagrame de estructura](./img/diagrama.png)
<sub>_**click [aqui](https://www.figma.com/file/gGUbw0SLhhbP5NFplgt1iu/Untitled?type=whiteboard&node-id=0%3A1&t=IFf8Mpjt3Wv4rbxZ-1) para revisar el diagrama en mejor resolucion**_</sub>

## Funciones 

- ### Modulo Utilidades del catalogo

  - **_crear_archivo_vacio_**

          Crea un catalogo vacio con un formato que maneja el sistema

      _Argumentos:_

          nombre_archivo: nombre del archivo a crear

      _Variables:_

          - estructura_catalogo: Estrcutura del catalogo predeterminada vacia

      _No retorna ningun valor._
  - **_cargar_catalogo_archivo_**

          Carga el catalogo desde un archivo existente.

          Se solicita el nombre de archivo sin extension .txt.
          Si el archivo existe, lo lee y evalua su contenido como catalogo. 
          Si no existe, intenta crear uno usando la funcion crear_archivo_vacio()
          Se muestrar mensajes informativos y de error en caso de existir alguno

      _Retorna el catalogo cargado_

      _Variables:_

          - nombre_archivo: Nombre del archivo a cargar (sin la extensión .txt)
          - nombre_archivo_completo: Nombre completo del archivo con la extensión .txt
          - contenido: Contenido del archivo leído como una cadena.
          - catalogo: Catálogo evaluado a partir del contenido del archivo.
  - **_guardar_catalogo_archivo_**

          Guarda el archivo existente.

          Se solicita el nombre del archivo donde se guardara el catalogo.
          Si el archivo existe y existen permisos de escritura, se sobreescribe el contenido.
          Se muestran mensajes informativos y de error en caso de existir alguno.

      _Argumentos:_

          catalogo: Catálogo a guardar

      _Variables:_

          - nombre_archivo: Nombre del archivo donde se guardará el catálogo (sin la extensión .txt)
          - nombre_archivo_completo: Nombre completo del archivo con la extensión .txt

      No retorna ningun valor.
  - **_obtener_claves_categoria_**

          Obtiene las claves de la categoria solicitada.

          Busca la categoria en una lista de diccionarios y retorna las claves correspondientes.

      _Argumentos:_

          categoria: Categoría para la cual se desean obtener las claves

      _Variables:_

          - lista: Lista de diccionarios con las categorías y sus claves.
          - categoria_dict: Diccionario de una categoría en la lista.

      Retorna una lista de claves
  - **_diccionario_agregar_producto_**

          Crea un diccionario de producto para una categoria especifica
          Utiliza las claves de la categoría obtenidas con la función obtener_claves_categoria().
          Solicita al usuario ingresar valores para cada clave y construye el diccionario de producto.`

      _Argumentos:_

          categoria: Categoría a la cual pertenece el producto

      _Variables:_

          - key_categoria: Lista de claves de la categoría
          - producto: Diccionario de producto.
          - caracteristica: Clave del producto a la que se le solicita un valor.
          - valor: Valor ingresado por el usuario para una clave del producto.

      Retorna el diccionario de producto creado.
  - **_agregar_diccionario_catalogo_**

          Agrega un diccionario de producto al catálogo en la categoría correspondiente.

          Busca la categoría en el catálogo y agrega el producto al diccionario de esa categoría.

      _Argumentos:_

          catalogo: Catálogo al cual se desea agregar el producto.
          categoria: Categoría del producto a agregar.
          producto: Diccionario de producto a agregar.

      _Variables:_

          - item: Diccionario de categoría en el catálogo.

      Retorna el catálogo modificado.
  - **_formato_impresion_producto_**

          Imprime el diccionario de un producto en un formato

      _Argumentos:_

          producto: Diccionario de producto a imprimir.

      No retorna ningun valor.
  - **_mostar_productos_**

          Muestra los productos del catálogo.

          Si se especifica una categoría, muestra solo los productos de esa categoría.
          Si no se especifica una categoría, muestra todos los productos del catálogo.

      _Argumentos:_

          catalogo: Catálogo a mostrar.
          categoria: Categoría de la cual se desean mostrar los productos (opcional).

      _Variables:_

          - item: Diccionario de categoría en el catálogo.
          - item_categoria: Nombre de la categoría en el diccionario.
          - productos: Lista de productos de una categoría.
          - producto: Diccionario de producto en la lista.

      No retorna ningun valor.
  - **_obtener_lista_produtos_**

          Obtiene una lista de todos los productos del catálogo.

      _Argumentos:_

          catalogo: Catálogo del cual se desea obtener la lista de productos

      _Variables:_

          - lista_productos: Lista que almacenará todos los productos del catálogo.
          - categoria: Diccionario de categoría en el catálogo.
          - productos: Lista de productos de una categoría.

      Retorna una lista de productos
  - **_buscar_y_eliminar_prodcuto_**

          Busca productos en la lista de productos utilizando palabras clave.

          Realiza una búsqueda recursiva con las palabras clave.
          Muestra los productos encontrados y ofrece la opción de eliminar un producto.

      _Argumentos:_

          lista_productos: Lista de productos en la cual se realizará la búsqueda.
          palabras_clave: Palabras clave para buscar productos.
          catalogo: Catálogo que contiene la lista de productos.

      _Variables:_

          - producto: Diccionario de producto en la lista de productos.
          - palabra_clave: Palabra clave para buscar en los productos.
          - coincidencias: Lista de productos que coinciden con las palabras clave.
          - opcion: Opción seleccionada por el usuario.

      No retorna ningun valor.
  - **_busqueda_producto_titulo_**

          Elimina un producto del catalogo.

          Solicita al usuario seleccionar un producto de la lista y lo elimina del catalogo

      _Argumentos:_

          productos: Lista de productos para seleccionar uno a eliminar.
          catalogo: Catálogo del cual se eliminará el producto.

      _Variables:_

          - opcion: Índice del producto seleccionado por el usuario.
          - producto: Producto seleccionado por el usuario.
          - item: Diccionario de categoría en el catálogo.

      No retorna ningun valor.

- ### Modulo del Menu

  - _**seleccion_opciones**_

          Solicita al usuario que seleccione una opción numérica y valida la entrada.

      _Argumentos:_

          opciones (list): Lista de opciones disponibles.

      _Variables:_

        - option (bool): Bandera para indicar si se ha seleccionado una opción válida.
        - selection (str): Entrada del usuario que representa la opción seleccionada.
        - selected_option (int): Opción numérica seleccionada.
        - opcion_seleccionada: (str): Valor correspondiente a la opción seleccionada.
        - opciones (list): Lista de opciones disponibles.

      Retorna la opcion seleccionada y su valor correspondiente
  - _**imprimir menu**_

          Imprime el menú en forma de clave y valor.

      _Argumentos:_

          menu (dict): Diccionario que representa el menú a imprimir.

      _Variables:_

          - key (str): Clave del menú.
          - value (str): Valor asociado a la clave del menú.

      No retorna ningun valor
  - _**plantilla_menu**_

          Imprime una plantilla de menú con un título y las opciones disponibles.

      _Argumentos:_

          titulo (str): Título del menú.
          opciones (dict, optional): Diccionario que representa las opciones del menú. Default to None.

      _Variables:_

          - titulo (str): Título del menú.
          - opciones (dict, opcional): Diccionario que representa las opciones del menú. Si no se proporciona, se asume None.

      No retorna ningun valor
  - _**opciones_menu**_

          Almacena y devuelve una lista de opciones correspondiente a la opción seleccionada

      _Argumentos:_

          opcion (int): Opción seleccionada.

      _Variables:_

          - lista (list): Lista de opciones correspondiente a la opción seleccionada.

      Regresa una lista de opciones
  - _**verificar_catalogo_cargado**_

          Verifica si el catálogo ha sido cargado previamente.
          Si el catalogo no ha sido cargado, lanza un aviso (exepcion)

      _Argumentos:_

          catalogo (list): Catálogo de productos.

      No regresa ningun valor
  - _**agregar_producto**_
  
          Agregar producto al catalogo

          Al ser un submenu, llama a la funcion _verificar_catalogo_cargado_. 
          Se despliega el menu y la opcion seleccionada entra como argumento para la funcion corresponiente en el modulo de utilidades

      _Argumentos:_

          catalogo (list): Catálogo de productos.

      _Variables:_

          - catalogo (list): Catálogo de productos.
          - opciones (list): Lista de opciones del menú "Agregar Producto".
          - seleccion (int): Opción numérica seleccionada por el usuario.
          - opcion_seleccionada (str): Valor correspondiente a la opción seleccionada.

      No regresa ningun valor.
  - _**eliminar_producto**_

          Elimina un producto del catálogo.

          Al ser un submenu, llama a la funcion _verificar_catalogo_cargado_. 
          Se despliega el menu y la opcion seleccionada entra como argumento para la funcion corresponiente en el modulo de utilidades

      _Argumentos:_

          catalogo (list): Catálogo de productos.

      _Variables:_

          - catalogo (list): Catálogo de productos.
          - palabras_clave (str): Palabras clave ingresadas por el usuario para buscar productos.

      No regresa ningun valor
  - _**buscar_producto**_

          Realiza una búsqueda de productos en el catálogo.

          Al ser una seleccion del menu, llama a la funcion _verificar_catalogo_cargado_.
          Se despliega el menu y se llama a la funcion correspondiente del modulo de utilidades.

      _Argumentos:_

          catalogo (list): Catálogo de productos.

      _Variables:_

          - catalogo (list): Catálogo de productos.

      No regresa ningun valor.
  - _**mostrar_catalogo**_

          Muestra el catálogo de productos dependiendo.

          Al ser un submenu, llama a la funcion _verificar_catalogo_cargado_. 
          Se despliega el menu y la opcion seleccionada entra como argumento para la funcion corresponiente en el modulo de utilidades

      _Argumentos:_

          catalogo (list): Catálogo de productos.

      _Variables:_

          - catalogo (list): Catálogo de productos.
          - opciones (list): Lista de opciones del menú "Mostrar Catálogo".
          - seleccion (int): Opción numérica seleccionada por el usuario.
          - categoria (str): Categoría seleccionada por el usuario.

      No regresa ningun valor.
  - _**cargar_catalogo**_

          Carga el catálogo almacenado en un archivo

          Al ser una opcion del menu principal se llama a la funcion correspondiente en el modulo de utilidades

      Regresa el catalogo almacenado en el archivo
  - _**guardar_catalogo**_

          Guarda el catalogo en un archivo

          Al ser una opcion del menu principal se llama a la funcion correspondiente en el modulo de utilidades

      _Argumentos:_

          .catalogo (list): Catálogo de productos.

      _Variables:_

          - catalogo (list): Catálogo de productos.

      No regresa ningun valor

- ### Catalogo

  Se inicia una variable catalogo en None

  - _**main**_

          La funcion main es con la que va a dar inicio a todo el programa.
          Y se establece la variable catalogo global, con ello se permite su manipulacion a lo largo de la ejecucion del programa.

      _Variables:_

         - catalogo: None

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
