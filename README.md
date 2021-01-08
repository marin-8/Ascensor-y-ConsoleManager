
<!-- ===== REFERENCIAS ================================================== -->

<!-- ##### -->

<!-- ===== TÍTULO ================================================== -->

---
# **Ascensor** y **Console Manager**
---

<!-- ===== IMAGEN CABECERA ================================================== -->

<!-- ##### -->

<!-- ===== DESCRIPCIÓN ================================================== -->

<br>

## **Descripción** <a name="DESC"></a>

_Ascensor y Console Manager_ es un proyecto formado por 3 componentes principales:

- El módulo `elevator_backend` que describe el funcionamiento de un ascensor.

- El módulo `console_manager` que permite gestionar el control por comandos de cualquier aplicación Python.

- Las `Demos` que implementen cualquiera de los 2 componentes anteriores:

    - La Demo `Manual` que representa un ascensor a tiempo real utilizando `pygame` para la visualización y el módulo `console_manager` para el control desde una ventana de consola estándar.

<br>

---

<!-- ===== TABLA DE CONTENIDOS ================================================== -->

<br>

## **Tabla de contenidos**

- [**Descripción**](#DESC)

- [**Características principales**](#CAPR)

    - [Módulo `elevator_backend`](#CAPR_EB)
    - [Módulo `console_manager`](#CAPR_CM)
    - [Demo `Manual`](#CAPR_D_M)

- [**Tecnologías usadas**](#TEUS)

    - [Lenguaje](#TEUS_L)
    - [Módulo `console_manager`](#TEUS_CM)
    - [Demo `Manual`](#TEUS_D_M)

- [**Funcionamiento**](#FUNC)

    - [Módulo `elevator_backend`](#FUNC_EB)
    - [Módulo `console_manager`](#FUNC_CM)
    - [Demo `Manual`](#FUNC_D_M)

<br>

---

<!-- ===== CARACTERÍSTICAS PRINCIPALES ================================================== -->

<br>

## **Características principales** <a name="CAPR"></a>

- Módulo `elevator_backend` : <a name="CAPR_EB"></a>

    - Representación lógica de un ascensor
    - Función `add_target(target, source)` para simular:
        - el llamamiento al ascensor desde cualquier piso
        - la pulsación de un botón dentro del ascensor
    - Función `next_step()` que avanza un paso en la simulación del ascensor

- Módulo `console_manager` : <a name="CAPR_CM"></a>

    - Clase `Command` que describe la estructura de un comando
    - Clase `ConsoleManager` que permite:
        - Añadir comandos de tipo `Command` al gestor con la función `addCommand(command)`
        - Pedir al usuario la introducción de comandos y gestionarlos con la función `consoleManager()` hasta que la aplicación se cierre
        - Visualizar con el comando `help` todos los comandos, su descripción y su sintaxis en una tabla 

- Demo `Manual` : <a name="CAPR_D_M"></a>

    - Representación visual de un ascensor en una ventada de `pygame`
    - Control a través de la introducción de comandos en una consola, gestionados por el módulo `console_manager`
    - Uso de `hilos` para separar la visualización del control
    - Cálculo del máximo número de pisos para el ascensor en base a la resolución vertical de la pantalla
    - Número de pisos introducido por el usuario
    - Diferenciación por colores de los distintos tipos de mensajes en la consola

<br>

---

<!-- ===== TECNOLOGÍAS USADAS ================================================== -->

<br>

## **Tecnologías usadas** <a name="TEUS"></a>

- Lenguaje: `Python` <a name="TEUS_L"></a>

- Módulo `console_manager` : <a name="TEUS_CM"></a>

    - Módulos de terceros:
        - `colorama` para imprimir en la consola en color
        - `terminaltables` para mostrar los comandos disponibles en una tabla 

- Demo `Manual` : <a name="TEUS_D_M"></a>

    - Módulos de Python:

        - `os.system` para:
            - modificar el tamaño inicial de la consola
            - borrar todo lo que contenga
        - `os.environ` para:
            - ocultar lo que pygame imprime en la consola al iniciarse
            - modificar la posición de la ventana de pygame
        - `threading` para ejecutar el control por comandos en un hilo distinto al principal
        - `win32api.GetSystemMetrics` para obtener la resolución de la pantalla

    - Módulos de terceros:
        - `pygame` para la representación visual del ascensor

<br>

---

<!-- ===== Funcionamiento ================================================== -->

<br>

## **Funcionamiento** <a name="FUNC"></a>

- Módulo `elevator_backend` : <a name="FUNC_EB"></a>

    - Función `add_target(target, source)` para añadir un objetivo para el ascensor
        - Parámetro `target` : número del piso objetivo
        - Parámetro `source` : fuente de la llamada, que puede ser:
            - `floor` : simulando la llamada al ascensor desde un rellano
            - `elevator` : simulando la pulsación de uno de los botones dentro del ascensor
    - Función `next_step()` para avanzar un paso en la simulación del ascensor

- Módulo `console_manager` : <a name="FUNC_CM"></a>

    - Clase `Command` que describe la estructura de un comando
        - Parámetros del constructor:
            - `name` : nombre del comando
            - `short` : abreviación del comando
            - `action` : función a ejecutar cuando se llame al comando
            - `syntax` : sintaxis del comando
            - `description` : descripción del comando
        - Función `execute(arguments)` que ejecuta la acción del comando en base a unos argumentos (vacíos si innecesarios)

    - Clase `ConsoleManager` para la gestión de los comandos que se le introduzcan
        - Función `addCommand(command)` que añade un comando de tipo `Command` al gestor
        - Función `consoleManager()` que está constantemente pidiendo al usuario la introducción comandos para ejecutar

- Demo `Manual` : <a name="FUNC_D_M"></a>

    - Descripción del funcionamiento no disponible por el momento
    - Prueba la Damo tú mismo ejecutando el programa `Demos/Manual/Manual.exe`

<br>

---

<!-- ===== BASE ================================================== -->
<!--
<br>

## **BASE** <a name="OOOO"></a>

<br>

---
-->
<!-- ===== ===== ================================================== -->