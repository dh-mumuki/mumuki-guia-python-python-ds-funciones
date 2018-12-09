En Python para definir una función es necesario asignarle un nombre, el que querramos, y opcionalmente los argumentos. Una función puede devolver uno o mas valores que pueden ser asignados a una variable.

Para utilizar una función, ésta debe ser llamada desde el programa, con el nombre asignado en la definición y en el caso de tener argumentos, le deben ser dados entre paréntesis.

La primera línea de la definición de una función contiene:

* la palabra reservada `def`
* el nombre de la función (la guía de estilo de Python recomienda escribir todos los caracteres en minúsculas separando las palabras por guiones bajos)
* paréntesis (que pueden incluir los argumentos de la función, como se explica más adelante)
* Terminando con `:`


Por comodidad, se puede indicar el final de la función con la palabra reservada `return` (más adelante se explica el uso de esta palabra reservada), aunque no es obligatorio.

Con las funciones, podemos hacer infinidad de cosas, pero vamos a empezar por algo fácil. Acá escribimos la función que dobla el valor del número que le pasemos.

```python
def doble(numero) :
   return 2 * numero
```

Como podemos ver, arriba declaramos una función con la palabra reservada **def** y el nombre _doble_ Entre los paréntesis, pusimos el **argumento** _numero_ el cual va a estar reemplazado por el número que le demos cuando lo llamemos. Para terminar, con la palabra **return** le decimos que lo que queremos es que devuelva 2 veces el _número_ que le dimos.

Para ejecutar la función y que haga lo que queremos, hay que llamarla por el nombre y entre paréntesis ingresar el número que queremos que utilice.

```python
doble(5)   # Esto nos va a devolver 10
doble(1.5) # Y éste nos devolverá 3
```

