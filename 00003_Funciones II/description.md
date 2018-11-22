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

<br>

