hora vamos a definir una función que toma un número `num` y devuelve una lista en donde cada posición es el resultado de potenciar el número, con el valor de la posición.

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

#### Explicación
Definimos una función que toma un numero `num`, a este valor se le llama argumento.

Dentro de la función lo primero que hacemos es definir una lista vacía, esta lista la definimos vacía para poblarla durante la iteración.<br>

La idea es que a medida que iteramos sobre el `range(10)` el valor de `i` cambie sucesivamente, sumando 1 en cada iteracion. <br>

Este valor de `i` lo utilizamos para elevar el numero `num` que pedimos como argumento de la función.<br>

El resultado de elevar el número lo guardamos en la variable `num_elevado` y utilizamos el método `append` para integrarlo a la lista, durante la iteración. <br>

Una vez que la iteración termina, la función devuelve la lista con los valores calculados.
<br>

:memo: **Escribí una función recibe una lista y devuelva una tupla con dos listas, una con los números pares y otra con los númeors impares.**

> Cuando definan la función, en el `return`incluyan las dos listas separadas por una coma: `return lista1, lista2`. De esta manera la función devolverá una tupla con ambas listas.