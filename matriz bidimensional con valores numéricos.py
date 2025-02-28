def ordenar_fila(matriz, fila_a_ordenar):
  """Ordena una fila específica de una matriz usando Bubble Sort."""

  fila = matriz[fila_a_ordenar]
  n = len(fila)

  for i in range(n):
    for j in range(0, n - i - 1):
      if fila[j] > fila[j + 1]:
        fila[j], fila[j + 1] = fila[j + 1], fila[j]

  matriz[fila_a_ordenar] = fila  # Actualiza la matriz con la fila ordenada

matriz = [
  [9, 2, 7],
  [1, 8, 5],
  [6, 3, 4]
]
fila_a_ordenar = 0

print("Matriz original:")
for fila in matriz:
  print(fila)

ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
  print(fila)
