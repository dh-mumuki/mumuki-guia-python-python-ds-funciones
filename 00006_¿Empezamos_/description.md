Supongamos que queremos calcular e imprimir el doble de un número cualquiera. Sabemos que una forma sencilla de hacerlo sería utilizando un código como el que sigue:

```pyhton
numero = 3
doble = numero * 2

print(doble)

ム
> 6
```

Ahora, ¿qué pasa si queremos hacer esto muchas veces? En vez de estar reescribiendo todas las líneas del código, podemos escribir una estructura genérica que contenga las instrucciones necesarias para obtener el resultado deseado. Esa estructura es lo que conocemos como **función**, y en Python se ve así:

```python
def duplicar(numero):
  n = numero
  doble = n * 2

  return print(doble)

duplicar(3)

ム
> 6
```

Habrás notado que aparecieron algunas palabras nuevas, como `def` y `return`. Veamos en cada línea qué es lo que hicimos:

```python
# 1      2     3    4
def duplicar(numero):
```

  * 1. Comenzamos con la llamada a `def`, que es una palabra reservada, justamente, para definir funciones.
  * 2. Luego, **duplicar** es el **nombre** que nosotros le asignamos a la función, para luego poder llamarla y ejecutarla. El nombre de una función es arbitario, pero es recomendable que haga referencia a la tarea que realiza. Por otra parte, es importante no usar palabras reservadas de Python (como `list`, `set`, o `True`), ni tampoco nombres de [otras funciones existentes](https://docs.python.org/3/library/functions.html#func-range) (`range()`, `len()`, `append()`).
  * 3. **Entre paréntesis** podemos incluir uno o más **argumentos** de nuestra función. Los argumentos son elementos que ingresan en la función, muchas veces en forma de variables, y determinan qué se va a hacer y cómo. En nuestro caso, le pasamos a la función un único argumento, **numero**, el cual será utilizando para hacer una multiplicación.
  * 4. Por último, antes de comenzar con el cuerpo de la función, siempre cerramos la línea con **dos puntos** (`:`). 

¿Va quedando claro? :wink:

```python
def duplicar(numero):
  n = numero # 5
  doble = n * 2 # 6
```
  * 5. Aquí comienza lo que llamamos el **cuerpo de la función**, es decir, todo el bloque de código que contiene las instrucciones que queremos darle a la computadora. Es muy importante señalar que, al igual que en los bucles `for` o en las estructuras condicionales, el cuerpo debe estar indentado (¿habías notado la sangría?). En nuestro ejemplo, la primera instrucción que damos es la definición de una variable, **n**, que va a asumir el valor propio de **numero**, el único argumento de la función.
  * 6. En esta segunda línea del cuerpo, multiplicamos **n** por dos y almacenamos el resultado en la variable **doble**.

Esto último fue fácil, ¿o no? :relaxed:

```python
def duplicar(numero):
  n = numero
  doble = n * 2

  return print(doble) #7
```
  * 7. En este punto, aparece la otra palabra clave, `return`. Con ella concluye la construcción de nuestra función, y antecede aquello que obtenemos cada vez que la ejecutamos.  En este caso, queremos que la función nos "devuelva" la impresión del valor de la multiplicación, de allí que escribamos `print(doble)` a continuación del `return`.

Aquí concluye la definión de nuestra función. Sin embargo, aún no hemos hecho nada con ella, y de poco sirve un método que sólo sea definido y nunca utilizado...

```python
def duplicar(numero):
  n = numero
  doble = n * 2
  
  return print(doble)

duplicar(3) # 8
ム
> 6
```

  * 8. Para hacer uso de una función previamente definida, basta con llamarla por su nombre e indicar entre paréntesis qué valor adoptan sus argumentos, si los hubiere. En nuestro ejemplo, al ejecutar `duplicar(3)`, obtenemos como resultado un 6, que no es otra cosa que la impresión del doble de 3, el número que utilizamos como argumento de nuestra función `duplicar()`.

De ahora en más, podremos usar nuestra función cuantas veces queramos, como se muestra a continuación:

```python
doble(5)

ム
> 10

doble(1.5)

ム
> 3
```

Parece que trabajar con funciones nos va a ahorrar muchas líneas de código, ¿no? :smile:

