# Juego del ahorcado

Juego en consola desarrollado en Python. El jugador debe descubrir
una palabra o frase seleccionada al azar desde `wordlist.txt`.

## Requisitos

- Python 3.8 o superior.
- No requiere instalar bibliotecas externas.

## Cómo ejecutar

Desde la raíz del repositorio:

```bash
cd hangman_project
python3 main.py
```

## Reglas

- Ingresá una letra por turno.
- Se aceptan letras mayúsculas y minúsculas.
- Las entradas vacías, los números, los símbolos y las entradas de
  varios caracteres se rechazan sin consumir intentos.
- Las letras ya intentadas se rechazan, tanto si fueron correctas
  como incorrectas.
- Cada letra incorrecta nueva suma un error.
- Los espacios y los signos de puntuación se muestran automáticamente.
- Ganás al descubrir todas las letras.
- Perdés al acumular 6 errores.

Después de cada intento válido, se muestran las letras intentadas,
el progreso y los intentos restantes.

## Archivos

| Archivo | Descripción |
| --- | --- |
| `main.py` | Inicia el juego, valida la entrada y controla los turnos. |
| `game.py` | Define la clase `HangmanGame` y la lógica del juego. |
| `utils.py` | Selecciona y devuelve una palabra o frase al azar. |
| `wordlist.txt` | Contiene las palabras o frases, una por línea. |
| `README.md` | Explica cómo ejecutar y jugar. |

## Lista de palabras

Podés modificar `wordlist.txt` para agregar palabras o frases.
El archivo debe contener al menos una entrada y no tener líneas vacías.
