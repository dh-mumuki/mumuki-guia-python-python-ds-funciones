> :memo: **¿Qué devuelve el siguiente `print()`?**

``` python
def funcion(numero):
    numero += 3
    mi_lista = [numero]
    
    mi_lista.append(numero**2)
    
    return 'mi_lista'

llamado = funcion(20)    
print(llamado)
```