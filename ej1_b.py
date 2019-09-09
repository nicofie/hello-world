def ej1b(inicio, fin):
    a = list()
    """Ejer num 1:
    :param a: 
    :param inicio:
    :param fin:
    :return:
    """

    for i in range(inicio, fin + 1):
        if i % 7 == 0 and i % 5 != 0:
            a.append(i)

    return ",".join("a")
    


"""+ 0 porque el ultimo lo excluye"""


