Definamos otra función que evalúa un número y devuelve `True` si es natural y par, y `False` en caso contrario.

``` python
def entero_par(numero):
    # Evaluación de las condiciones lógicas
    if numero % 2 == 0 and numero > 0:
        return True
    else:
        return False
  
```

Una vez definida la función, si queremos ejecutarla múltiple veces, podemos incluirla dentro de un bucle, como vemos a continuación:

``` python
for numero in [1,2,3,4,5]:
    print(entero_par(numero))

ム
>False
>True
>False
>True
>False
```<br>

Es interesante destacar la posibilidad de definir una función e incluirla en ditintas estructuras. Aquí es donde se ve la potencia de las funciones y cómo nos permiten facilitar la escritura del código.<br>

Así como podemos incluir una función dentro de un bucle, también podemos incluir funciones dentro de otras funciones. 🤯 ¿Suena raro? ¡Ya vas a ver que es más sencillo de lo que parece!<br>

Supongamos que ahora queremos definir una función que encuentre los números enteros y pares de una lista y los guarde en otra lista. Para esto, podemos aprovechar la función `entero_par()`, que ya habíamos definido anteriormente.<br>

``` python
def enteros_pares_en_lista(lista):
    lista_pares = []
    for numero in lista:
        if entero_par(numero) == True:
            lista_pares.append(numero)
    return lista_pares
```

Acá observamos que, en lugar de reescribir las instrucciones que evalúan si un número es natural y par, podemos hacer una llamada a `entero_par()` dentro del cuerpo de `enteros_pares_en_lista()`. De esta manera, simplificamos y reutilizamos nuestro código. ¿Viste qué fácil y práctico es? :smile:

> :memo: **Escribí una función que sume los elementos de una lista, otra que cuente los elementos de una lista y una última función que calcule la media de los elementos de una lista. Recordá que es posible reutilizar una función dentro de otras.**