## Funciones

Una función es un conjunto de instrucciones que realizan alguna tarea en particular y que, mediante un nombre, pueden ser llamadas durante la ejecución de un programa en python.


Existen múltiples motivaciones para agrupar el código en funciones: si una acción específica debe ser realizada de forma recurrente, para hacer mas legible el código, para dividir un problema en partes, etc.

En python para definir una función es necesario asignarle un nombre y opcionalmente los argumentos, una función puede devolver uno o mas valores que pueden ser asignados a una variable, utilizarse como parte de una expresión lógica, etc.

Para utilizar una función, esta debe ser llamada desde el programa, con el nombre asignado en la definición y en el caso de tener argumentos, le deben ser dados entre paréntesis.


A continuación vamos a definir una función que suma dos números.

``` python
def sumando():
    return 2 * 3
```

Definimos una función cuyo nombre es sumando, para definirla, hicimos el llamado a `def` y posteriormente elegimos el nombre **sumando**, a continuación utilizamos los paréntesis vacios, que indican que la función no recibe argumentos.

Despúes definimos el código, que consta de una única instrucción `return` y una operación de multiplicación entre dos números. 

Este `return` devuelve un valor (el producto de dos números), cada vez que es llamada.

Cuando dentro de la función se ejecuta un `return`, la función termina su tarea.

Ahora vamos a realizar una serie de llamados a la función definida mas arriba:

``` python
mi_numero = sumando()

print(mi_numero)
```
_Salida:_
**> 6**

``` python
mi_numero = sumando()

print(6 == sumando() )
```
  _Salida:_
**> True**


Como podemos observar, el valor que devuelve la función puede ser utilizada directamente para varias operaciones.

Definamos una función que utiliza argumentos, en este caso es una función simple que indica si un número natural es a la vez par.

``` python
def entero_par(numero):
    
    if numero % 2 == 0 and numero > 0:
        return True
    else:
        return False
  
``

Ahora vamos a definir una función que toma un número `num` y devuelve una lista en donde cada posición es el resultado de potenciar el número, con el valor de la posición.

``` python
def elevado(num):
    # definimos una lista vacia
    mi_lista = []
    
    # iteramos en un rango de 10 asignando un valor creciente a i (crece de 1 en 1)
    for i in range(10):
        # elevamos a la potencia dada en i y lo guardamos en num_elevado
        num_elevado = num ** i
        # guardamos al final de la lista el numero elevado a la potencia i
        mi_lista.append(num_elevado)
      
    return mi_lista  

# hacemos el llamado a función y lo imprimimos.
print(elevado(2))
```
  _Salida:_
**[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]**

#### Expicación
Definimos una función que toma un numero `num`, a este valor se le llama argumento.

Dentro de la función lo primero que hacemos es definir una lista vacía, esta lista la definimos vacía para poblarla durante la iteración.

La idea es que a medida que iteramos sobre el `range(10)` el valor de `i` cambie sucesivamente, sumando 1 en cada iteracion. 

Este valor de `i` lo utilizamos para elevar el numero `num` que pedimos como argumento de la función.

El resultado de elevar el número lo guardamos en la variable `num_elevado` y utilizamos el método `append` para integrarlo a la lista, durante la iteración.

Una vez que la iteración termina, la función devuelve la lista con los valores calculados.




