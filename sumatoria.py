def sumatoria_cubica(n):
    """
    Entradas: Cantidad de veces que se itera.
    Salidas: El valor de la función f(n) en complejidad temporal cúbica.
    """

    resultado = 0

    for i in range(n+1):

        for j in range(i+1):

            for k in range(j,i+j):
                resultado += 1

    return resultado

    raise NotImplementedError()

def sumatoria_constante(n):
    """
    Entradas: Cantidad de veces que se itera.
    Salidas El valor de la función f(n) en complejidad temporal constante.
    """
    return (n*(n+1)*(n+2))/3

    raise NotImplementedError()