## Funciones

Una función es un conjunto de instrucciones que realizan alguna tarea en particular y que, mediante un nombre, pueden ser llamadas durante la ejecución de un programa en python.


Existen múltiples motivaciones para agrupar el código en funciones: si una acción específica debe ser realizada de forma recurrente, para hacer mas legible el código, para dividir un problema en partes, etc.

En python para definir una función es necesario asignarle un nombre, el que querramos, y opcionalmente los argumentos. Una función puede devolver uno o mas valores que pueden ser asignados a una variable.

Para utilizar una función, ésta debe ser llamada desde el programa, con el nombre asignado en la definición y en el caso de tener argumentos, le deben ser dados entre paréntesis.


A continuación vamos a definir una función que suma dos números.

``` python
def sumando(a, b):
    return a + b
```

Definimos una función cuyo nombre es **sumando**. Para definirla, primero hicimos el llamado a `def`, luego elegimos el nombre **sumando** y finalmente **a** y **b** , dentro de los paréntesis, indican los argumentos de la función . Recordá siempre colocar los **:** en la primer línea de la definición.

Despúes definimos el bloque de código, que consta de una única instrucción `return` seguida de la suma de los dos argumentos, cada vez que es llamada.

Aclaración: Cuando dentro de la función se ejecuta un `return`, la función termina su tarea.


Ahora vamos a realizar una serie de llamados a la función definida mas arriba:
En este caso sumaremos dos y tres y le asignaremos el resultado a una variable. Finalmente, imprimiremos la variable.

``` python
# se realiza un llamado a la funcion **sumando()**,  y se guarda el resultado de la funcion en la **variable mi_numero**
mi_numero = sumando(2,3)

# se imprime la variable, **mi_numero**
print(mi_numero)
```
_Salida:_
**> 5**

``` python
# Se evalua una condicion logica, en donde se pregunta si 6 es igual al resultado de la funcion sumando()
print(sumando() == 5)
```
  _Salida:_
**> True**


Como podemos observar, el valor que devuelve la función, que es un numero entero,  puede ser utilizada directamente para realizar varias operaciones.

#### Definiendo los argumentos de las funciones.

Los argumentos son variables que se le entrega a una función cuando hacemos un llamado.

Se declara entre paréntesis con un nombre asignado por nosotros. 

Este argumento puede ser utilizado dentro del bloque de código de la función, según el nombre que le asignamos.

Definamos ahora una función que utiliza argumentos, en este caso lo único que va a hacer la función es recibir un valor e imprimir su tipo de datos.

Acalración: La función type() devuelve el tipo de datos de la variable que se coloque dentro de los paréntesis. Es una función built-in de Python, es decir que esta incluida en el lenguaje.

``` python
def imprimir_tipo(argumento):
    return print(type(argumento)) 
  
```

Ahora realizaremos el llamado a función con distintos argumentos.

``` python
# Definimos una lista
lista = [1,3,5,7]
# hacemos un llamado a la funcion, dandole una lista como argumento
imprimir_tipo(lista)
```
  _Salida:_
**class 'list'**

``` python
# Definimos un  entero
un_numero = 1
# hacemos un llamado a la funcion, dandole una variable que guarda un entero como argumento
imprimir_tipo(un_numero)
```
  _Salida:_
**class 'int'**


``` python
# hacemos un llamado a la funcion, dandole a la funcion directamente un entero como un argumento
imprimir_tipo(23023213)
```
  _Salida:_
**class 'int'**

Como podemos observar, el valor que entregamos entre paréntesis es el que interpreta la función como argumento, además podemos variar el valor de ese argumento y tambien su tipo.