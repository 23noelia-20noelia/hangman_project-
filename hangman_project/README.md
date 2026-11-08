# hangman_project-
Juego del ahorcado en Pyhton: Proyecto grupal
Descripción general del proyecto
En este proyecto, implementarás un juego del ahorcado basado en consola. El jugador adivinará letras de una palabra oculta (como un título de película) dentro de un número limitado de intentos incorrectos. Las palabras se cargarán aleatoriamente desde un archivo de texto simple.

Objetivos de aprendizaje
Al completar este proyecto, los estudiantes podrán:

Aplicar estructuras de control (condicionales y bucles) para gestionar el flujo del juego.
Usar funciones para encapsular y estructurar la lógica.
Utilizar estructuras de datos como cadenas, listas y diccionarios.
Implementar conceptos básicos de programación orientada a objetos (clases, objetos, herencia).
Usar módulos e imports para separar el código en varios archivos.
Manejar la entrada/salida de usuarios y archivos de texto.
Leer y validar la entrada del usuario desde la línea de comandos.
Practicar depuración básica y resolución de problemas mediante una tarea del mundo real.
Reglas del juego
El jugador tiene que adivinar la palabra oculta letra por letra.
Solo se aceptan letras como entrada válida.
Cada intento incorrecto aumenta el contador de errores.
El jugador pierde después de 6 intentos incorrectos.
El juego termina si el jugador adivina correctamente todas las letras antes de alcanzar el número máximo de errores.
Las letras ya adivinadas y el estado actual de la palabra se muestran después de cada intento.
Los caracteres que no son letras (como espacios o signos de puntuación) se revelan automáticamente.
Estructura de archivos
hangman_project/
│
├── main.py             # Bucle del juego
├── game.py             # Clase HangmanGame (lógica del juego)
├── utils.py            # Funciones auxiliares 
├── wordlist.txt    # Lista de frases (una por línea)
└── README.md           # Instrucciones y descripción del juego
