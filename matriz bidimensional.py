matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    def buscar_valor(matriz, valor):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor:
                    return (i, j)
        return None
    valor_a_buscar = 5

    resultado = buscar_valor(matriz, valor_a_buscar)

    if resultado:
        fila, columna = resultado
        print(f"El valor {valor_a_buscar} se encontró en la posición ({fila}, {columna})")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
