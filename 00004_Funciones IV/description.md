Definamos otra función que indica True si un número es natural y par, y False si no lo és.

``` python
def entero_par(numero):
    # evaluacion de las condiciones logicas
    if numero % 2 == 0 and numero > 0:
        return True
    else:
        return False
  
```
Veamos los posibles llamados a esta función.


``` python
for numero in [1,2,3,4,5]:
    print(entero_par(numero))
```
  _Salida:_<br>
**>>False**<br>
**>>True**<br>
**>>False**<br>
**>>True**<br>
**>>False**<br>
<br>
Es interesante empezar a ver la posibilidad de definir una función e incluirla en ditintas estructuras. Aquí es donde se ve la potencia de las funciones y como se reutiliza el código. Para ser eficientes en esto, una buena práctuca es definir funciones que hagan UNA tarea particular y simple, para poder utilizarlas libremente y sin restricciones.<br>
Animemosnos a utilizar funciones dentro de funciones! Claro que se puede!
<br>
Miremos el bloque de código anterior. Podríamos definir una función que encuentre los enteros pares de una lista y los guarde en otra lista. Lo haremos utilizando la función entero_par(), que lo hacía para un número.
<br>
``` python
def enteros_pares_en_lista(lista):
  lista_pares = []
  for numero in lista:
    if entero_par(numero) == True:
      lista_pares.append(numero)
  return lista_pares
```


:memo:**Text**