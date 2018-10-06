¿Que devuelve el siguiente print?

``` python
def funcion(numero):
    numero += 3
    mi_lista = [3**3 for i in range(3)]
    
    mi_lista.append({ x : x*2 for x in  mi_lista})
    
    return 'mi_lista'

llamado = funcion(20)    
print(llamado)
```
