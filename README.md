
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

    - La demo `Manual` que representa un ascensor a tiempo real utilizando `Pygame` para la visualización y el módulo `console_manager` para el control desde una ventana de consola estándar.

<br>

---

<!-- ===== TABLA DE CONTENIDOS ================================================== -->

<br>

## **Tabla de contenidos**

- [**Descripción**](#DESC)

- [**Características principales**](#CAPR)

- [**Tecnologías usadas**](#TEUS)

- [**Motivación**](#MOTI)

- [**Funcionamiento**](#OOOO)

- [**Sobre mí**](#OOOO)

<br>

---

<!-- ===== CARACTERÍSTICAS PRINCIPALES ================================================== -->

<br>

## **Características principales** <a name="CAPR"></a>

- Módulo `elevator_backend`:

    - Representación lógica de un ascensor
    - Función `add_target(target, source)` para simular:
        - el llamamiento al ascensor desde cualquier piso
        - la pulsación de un botón dentro del ascensor
    - Función `next_step()` que avanza un paso en la simulación del ascensor

- Módulo `console_manager`:

    - Formado por 2 clases:
        - La clase `Command` que describe la estructura de un comando
        - La clase `ConsoleManager` que permite:
            - Añadir comandos de tipo `Command` al gestor con la función `addCommand(command)`
            - Pedir al usuario la introducción de comandos y gestionarlos con la función `consoleManager()` hasta que la aplicación se cierre
            - Visualizar con el comando `help` todos los comandos, su descripción y su sintaxis en una tabla 

- Demo `Manual`:

    - Cálculo del máximo número de pisos para el ascensor en base a la resolución vertical de la pantalla
    - Número de pisos introducido por el usuario
    - Representación visual en una ventada de `Pygame`
    - Control a través de la introducción de comandos en una consola, gestionados por el módulo `console_manager`
    - Uso de `hilos` para separar la visualización del control
    - Diferenciación por colores de los distintos tipos de mensajes en la consola

<br>

---

<!-- ===== TECNOLOGÍAS USADAS ================================================== -->

<br>

## **Tecnologías usadas** <a name="TEUS"></a>

- Lenguaje: `Python`

- Módulo `console_manager`:

    - Módulos de terceros:
        - `colorama` para imprimir en la consola en color
        - `terminaltables` para mostrar los comandos disponibles en una tabla 

- Demo `Manual`:

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

<!-- ===== MOTIVACIÓN ================================================== -->

<br>

## **Motivación** <a name="MOTI"></a>

<br>

---

<!-- ===== BASE ================================================== -->

<br>

## **BASE** <a name="OOOO"></a>

<br>

---

<!-- ===== ===== ================================================== -->