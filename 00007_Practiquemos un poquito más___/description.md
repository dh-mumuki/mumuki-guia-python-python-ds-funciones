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

ム
>5
```

``` python
# Se evalua una condicion logica, en donde se pregunta si 6 es igual al resultado de la funcion sumando()
print(sumando() == 5)

ム
>True
```

Como podemos observar el valor que devuelve la función, que es un numero entero,  puede ser utilizado directamente para realizar varias operaciones.
<br>

> :memo: **Definí una función que permita calcular el prodcuto entre dos números**