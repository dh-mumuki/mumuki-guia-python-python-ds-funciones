A continuación, vamos a definir una función que suma dos números:

``` python
def sumando(a, b):
    return a + b
```

¡Listo! Ya hemos creado la función `sumando()`. Para definirla, primero hicimos el llamado a `def`, luego elegimos el nombre **sumando** y, entre paréntesis, incluimos **a** y **b**, que son los argumentos de esta función. Por último, siempre colocamos los `:` antes de especificar qué instrucciones cumplirá nuestra función.

Despúes, en la siguiente línea, incluimos el cuerpo de la función (¡no te olvides de la indentación!), que consta únicamente del `return`, aquello que esperamos obtener cada vez que ejecutemos la función: la suma de a y b.

**Para tener en cuenta:**<br>
Cuando se ejecuta la instrucción del `return`, la función termina su tarea.

Ahora, vamos a realizar una serie de llamados a la función definida, `sumando()`. En este caso, sumaremos 2 más 3 y le asignaremos el resultado a una variable que, finalmente, imprimiremos.

``` python
# Se realiza un llamado a la función sumando() y se guarda el resultado en la variable mi_numero
mi_numero = sumando(2, 3) # a y b, los argumentos, asumen los valores de los números que queremos sumar

# Imprimimos la variable mi_numero
print(mi_numero)

ム
>5
```

``` python
# Se evalúa una condición lógica, en donde se pregunta si el resultado de la funcion sumando(2, 3) es igual a 5
print(sumando(2, 3) == 5)

ム
>True
```

Como podemos observar, el valor que devuelve la función puede ser utilizado directamente para realizar distintas operaciones, sin necesidad de almacernalo previamente en una variable.<br>

> :memo: **Definí una función que permita calcular el producto entre dos números cualesquiera.**