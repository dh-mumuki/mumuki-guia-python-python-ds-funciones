> :memo: **¿Que devuelve el siguiente print?**

``` python
def funcion(numero):
    numero += 3
    mi_lista = [3**3 for i in range(3)]
    
    mi_lista.append({ x : x*2 for x in  mi_lista})
    
    return 'mi_lista'

llamado = funcion(20)    
print(llamado)
```


> Supongo que no reconocen la estructura que tiene una forma similar a esta: [x for x in lista]. Se llaman Listas por comprensión! No es necesario que lo sepan para resolver este ejercicio, pero si les interesa pueden ver de que se trata _acá_.