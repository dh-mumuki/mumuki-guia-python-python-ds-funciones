## Funciones

Una función es un conjunto de instrucciones que realizan alguna tarea en particular y que, mediante un nombre, pueden ser llamadas durante la ejecución de un programa en python.


Existen múltiples motivaciones para agrupar el código en funciones: si una acción específica debe ser realizada de forma recurrente, para hacer mas legible el código, para dividir un problema en partes, etc.

En python para definir una función es necesario asignarle un nombre y opcionalmente los argumentos, una función puede devolver uno o mas valores que pueden ser asignados a una variable, utilizarse como parte de una expresión lógica, etc.

Para utilizar una función, esta debe ser llamada desde el programa, con el nombre asignado en la definición y en el caso de tener argumentos, le deben ser dados entre paréntesis.


A continuación vamos a definir una función que suma dos números.

``` python
def sumando():
    return 2 * 3
```

Definimos una función cuyo nombre es sumando, para definirla, hicimos el llamado a `def` y posteriormente elegimos el nombre **sumando**, a continuación utilizamos los paréntesis vacios, que indican que la función no recibe argumentos.

Despúes definimos el código, que consta de una única instrucción `return` y una operación de multiplicación entre dos números. 

Este `return` devuelve un valor (el producto de dos números), cada vez que es llamada.

Cuando dentro de la función se ejecuta un `return`, la función termina su tarea.

Ahora vamos a realizar un llamado a la función definida mas arriba:

``` python
mi_numero = sumando()

print(mi_numero)
```
  _Salida:_
**> 6 **

``` python
mi_numero = sumando()

print(6 == sumando() )
```
  _Salida:_
**> True **

``` python
if sumando < 3:
    print('es mayor a 3')
    
else:
    print('no es mayor a 3')

```
  _Salida:_
**> no es mayor a 3 **
