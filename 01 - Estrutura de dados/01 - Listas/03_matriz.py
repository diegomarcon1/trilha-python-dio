matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz2 = [
    [10, 12.5, "zé"],
    ["mm", "qu", 35],
    ["12", "24", 36]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

print(matriz2[2])
print(matriz2[2][1])
print(matriz2[1][-2])
print(matriz2[-1][-1])

for all in matriz:
    print(all)

print("---")

for all in matriz2:
    print(all)

