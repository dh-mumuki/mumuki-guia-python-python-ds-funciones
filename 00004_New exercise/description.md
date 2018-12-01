Definamos otra función que utiliza argumentos, en este caso es una función simple que indica si un número natural es a la vez par.

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