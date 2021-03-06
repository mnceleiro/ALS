# lambdas (+ prog. funcional)

doble = lambda x: x * 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
Point.getX = lambda self: self.x
Point.getY = lambda self: self.y
Point.__str__ = lambda self: str.format("({0},{1})", self.getX(), self.getY() )

car = lambda l: None if l == None or l == [] else l[0]
cdr = lambda l: None if l == None else l[1:]

# copy list using lambda
lcopy = lambda l: None if l == None else [] if l == [] else [car(l)] + lcopy(cdr(l))

# Funcion lambda que se le pasa lista y que devuelve copia de esa lista con los elementos multiplicados por 2
lcopyx2 = lambda f, l: None if l == None else [] if l == [] else [doble(car(l))] + lcopy(doble(cdr(l)))

# map(doble,[1,2,3])
map = lambda f, l: None if l == None else [] if l == [] else [f, f(car(l))] + (f, f(cdr(l)))

# filter(lambda x: True if x%2 == 0 else False, [1,2,3,4,5,6])
filter = lambda f, l: None if l == None else [] if l == [] else [car(l)] + filter(f, cdr(l)) if f(car(l)) else filter(f, cdr(l))

reduce = lambda f, l: None if l == None else None if l == [] else car(l) if len(l) == 1 else f(car(l), reduce(f, cdr(l)))
# reduce(lambda x, y: x+y, [1,2,3])

# Las funciones map, filter y reduce ya existen por defecto

lcopy = lambda l: map(lambda x: x, l)

## Python 3
#for x in map(lambda x: x * 2, [1,2,3]):
    #if veces < 2:
        #print(x)
    #else:
        #break
    #veces +=1
    
## python 3
#import functools
#function reduce(lambda x, y: x + y, [1,2,3])

# fibonacci empezado por mi rofl
#fibonacci = lambda n: [] if n == 0 else [0] if n == 1 else [0,1] if n == 2 else l=[0,1] and l.append(l[(l.size-1)]+l[(l.size-2)])#

fibo = lambda x: [0] if x <= 0 else [0,1] if x == 1 else fibo(x-1) + [fibo(x-1)[-1] + fibo(x-1)[-2]]
#fibo(6)


# 1. Crear las funciones (utilizando car y cdr):
# - Penultimo(l)
# - Ultimo(l)
# - reescribir fibo para utilizarlos.

# 2. Reescribir fibo() en terminos de map, filter y reduce

# len(l) == 1 <==> car(cdr(1)) == None
# len(l) == 2 <==> car(cdr(cdr(l))) == None
ultimo = lambda l: None if l == [] or l == None else car(l) if len(l) == 1 else ultimo(cdr(l))
