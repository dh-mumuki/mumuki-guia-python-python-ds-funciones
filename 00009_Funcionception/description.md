Como veíamos antes, teniendo funciones pequeñas podemos combinarlas para hacer cosas mas complejas.

Por ejemplo, si queremos sumar dos números y después multiplicarlos por 3, podríamos hacerlo de la siguiente forma:

```python
def suma_por_tres(numero1,numero2):
  resultado_de_suma = sumar(numero1,numero2)
  return resultado_de_suma * 3 

```

Acá vemos que al ya tener la función **sumar()** definida, podemos llamarla dentro de otra función y hacernos el trabajo mas fácil.

> Veamos si con la función `sumar()` podemos hacer una función `cuadrado_de_suma()` que tome un parámetro y nos devuelva el doble del siguiente. 