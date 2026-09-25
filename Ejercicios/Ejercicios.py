#En todos los casos podrías reemplazar los conjuntos fijos por input() si necesitas que el usuario los ingrese:
##1. Unión (elementos en A o en B, o en ambos)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)


### 2. Intersección (elementos en A y en B)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)


###3.Diferencia simétrica (elementos en A o en B, pero no en ambos)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A ^ B)

##4. Subconjunto (¿A es subconjunto de B?) 
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))

##5. Número de elementos de A
A = {1, 2, 3, 4}
print(len(A))

