Como veíamos antes, podemos combinar distintas funciones sencillas para hacer cosas más complejas.

Por ejemplo, si queremos sumar dos números y después multiplicar el resultado por 3, podríamos hacerlo de la siguiente forma:

```python
def suma_por_tres(numero1, numero2):
    resultado_de_suma = sumando(numero1, numero2)
    return resultado_de_suma * 3
```

Acá, vemos que, [ya habiendo definido la función `sumando()`](https://mumuki.io/data-science.digitalhouse/exercises/6137-nivelacion-python-funciones-practiquemos-un-poquito-mas), podemos utilizarla dentro de otra función para simplificar la escritura del código.

> :memo: Veamos si podemos aprovechar la función `sumando()` y utilizarla dentro de otra función, llamada `cuadrado_de_suma()`, que tome dos números y devuelva el cuadrado de su suma.