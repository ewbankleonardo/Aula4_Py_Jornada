lista_de_numeros:list = [64, 34, 25, 12, 22, 11, 90]


def ordenar_lista_numeros(lista_numeros:list) -> list:
    nova_lista = lista_numeros.copy()
    for i in range(len(nova_lista)):
        for j in range(i+1, len(nova_lista)):
            if nova_lista[i] > nova_lista[j]:
                nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]

    return nova_lista

nova_lista = ordenar_lista_numeros(lista_de_numeros)
print(nova_lista)