#### Definiendo los argumentos de las funciones

Como vimos en los ejemplos anteriores, los argumentos son variables que se le entrega a una función cuando hacemos un llamado.

Se declara entre paréntesis con un nombre asignado por nosotros. 

Este argumento puede ser utilizado dentro del bloque de código de la función, según el nombre que le asignamos.

Definamos ahora una función que utiliza argumentos, en este caso lo único que va a hacer la función es recibir un valor y comparar su tipo de datos.

Acalración: La función isinstance(mi_objeto, tipo) compara el objeto que se le entrega como primer argumento y lo compara con el tipos de datos que se desea. Es una función built-in de Python, es decir que esta incluida en el lenguaje.

``` python
def comparar_tipo(mi_objeto, tipo):
    return isinstance(mi_objeto, tipo)
  
```

Ahora realizaremos el llamado a función con distintos argumentos. <br>

``` python
# Definimos una lista
lista = [1,3,5,7]
# hacemos un llamado a la funcion, dandole una lista como argumento
comparar_tipo(lista, list)

ム
> True
```

``` python
# Definimos un  entero
un_numero = 1
# hacemos un llamado a la funcion, dandole una variable que guarda un entero como argumento
comprar_tipo(un_numero, int)

ム
> True
```


``` python
# hacemos un llamado a la funcion, dandole a la funcion directamente un entero como un argumento
imprimir_tipo(23023213, int)

ム
> True
```

Como podemos observar, los valores que entregamos entre paréntesis es el que interpreta la función como argumento. Además podemos variar el valor de ese argumento y tambien su tipo.

<br>
> :memo: **Definí una función  que devuelva `True` si el tipo de dato es _string_, `False` si es un _integer_,  `True` si es un _float_ y`False` si es un _booleano_**.
