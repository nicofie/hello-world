'''Escribir la función factorial, que reciba como parámetro el numero inicial y compute su resultado.
a. Ejemplo factorial(8) = 8*7*6*5*4*3*2*1 = 40320. Recuerde que factorial de 0 por definición es 1.
b. Hacer la implementación inversa (si lo hizo recursivo, hacerlo iterativo o viceversa)'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
