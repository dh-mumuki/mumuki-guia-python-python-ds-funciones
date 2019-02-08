Como vimos en los ejemplos anteriores, los **argumentos** son **variables** que le pasamos a una función cuando hacemos un llamado. Se declaran **entre paréntesis** con un nombre asignado por nosotros. Los argumentos pueden ser utilizado dentro del bloque de código de la función, según el nombre que le asignamos.

Definimos ahora una función que recibe un valor y evalúa su tipo de dato. Si el tipo coincide con el que nosotros consultamos, la función imprime un determinado mensaje y devuelve `True`; en caso contrario, imprime otro texto y devuelve `False`. Tanto el valor como el tipo serán los argumentos que incluiremos para esta función.

``` python
def comparar_tipo(mi_objeto, tipo):
    if isinstance(mi_objeto, tipo):
        print(mi_objeto, 'es del tipo', tipo)
    return True
    else:
        print(mi_objeto, 'no es del tipo', tipo)
    return False
```

**Aclaración**: la función `isinstance()` es un método propio de Python que recibe un elemento, evalúa si corresponde a un determinado tipo de dato y devuelve `True` o `False` según corresponda. Por ejemplo, `isinstance('Soy un string', str)` se evaluará como verdadero, mientras que `isinstance('No soy una lista', list)` será evaluado como falso.

Ahora, realizaremos distintos llamados a la función, cambiando en cada caso sus argumentos:<br>

``` python
# Definimos una lista
lista = [1,3,5,7]
# Hacemos el llamado a la función
comparar_tipo(lista, list) # La palabra reservada list hace referencia, obviamente, a una lista como estructura de datos

ム
> [1, 3, 5, 7] es del tipo <class 'list'>
> True
```

``` python
# Definimos un número
un_numero = 1
# Hacemos el llamado a la funcion
comprar_tipo(un_numero, list) 

ム
> 1 no es del tipo <class 'list'>
> False
```

``` python
# Hacemos el llamado a la función, dándole directamente un entero como un argumento
imprimir_tipo(350, int) # La palabra reservada int hace referencia a los números enteros

ム
> 350 es del tipo <class int>
> True
```

Como podemos observar, los valores de los argumentos que indicamos entre paréntesis en cada llamado son los mismos que asumen las variables propias de la función en cada ejecución. n esta función en particular, podemos variar el valor de podemos variar el valor de **mi_objeto**, así como también el tipo de dato contra el que se lo compara.<br>

¡Ahora te toca a vos! :smile:

> :memo: **Definí una función  que devuelva `True` si el tipo de dato es _string_, `False` si es un _integer_,  `True` si es un _float_ y`False` si es un _booleano_**.
