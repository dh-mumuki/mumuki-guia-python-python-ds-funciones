Ahora vamos a definir una función que toma un número y devuelve una lista en donde cada elemento es el resultado de elevar ese número a una determinada potencia.

``` python
def elevado(num): # 1
    # Definimos una lista vacía
    mi_lista = [] # 2
    
    # Iteramos en un rango de 10 asignando un valor creciente a i (crece de 1 en 1)
    for i in range(10): # 3
        # Elevamos a la potencia dada en i y lo guardamos en num_elevado
        num_elevado = num ** i # 4
        # Guardamos al final de la lista el numero elevado a la potencia i
        mi_lista.append(num_elevado) # 5
      
    return mi_lista # 6

# Hacemos el llamado a la función y lo imprimimos
print(elevado(2))# 7

ム
> [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

**Veamos qué hicimos en cada paso**:<br>
1. Primero, definimos una función llamada `elevado()`, que toma un número como argumento (**num**).<br>
2. Dentro de la función, lo primero que hacemos es definir una lista vacía, **mi_lista**, donde iremos volcando los resultados de nuestras operaciones.<br>
3. Vamos a ir iterando sobre la sucesión de números enteros que obtenemos con `range(10)`. En cada iteración, **i** adopta un valor distinto, comenzando en 0 y terminando en 9 (¿te acordabas de que el último valor nunca se incluye? :wink:).<br>
4. Definimos una variable, **num_elevado**, donde volcamos el resultado de elevar **num** a su _iésima_ potencia. Dicho de otra forma, lo potenciamos por el valor de **i** en cada repetición del bucle.<br>
5. Incluimos el resultado del paso anterior en la lista que habíamos definido previamente, **mi_lista**, usando el método `append()`.<br>
6. Una vez concluido el bucle, finalizamos la definición de nuestra función con el `return`, que en este caso nos devuelve **mi_lista** con los valores que almacenamos en ella.<br>
7. Ejecutamos la función pasándole el número 2 como argumento e imprimimos por pantalla el resultado. Como esperábamos, vemos que obtuvimos una lista con las potencias de 2.<br>

> :memo: **Escribí una función que reciba una lista de números enteros y devuelva una tupla con dos listas, una con los números pares y otra con los números impares.**


