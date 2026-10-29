letras=[
    ["a", "b", "c"],#file 0
    ["d", "e", "f"],#file 1
    ["g", "h", "i"],#file 2
    ["j", "k", "l"],#file 3
    ["m", "n", "ñ"],#file 4
    ["o", "p", "q"],#file 5
    ["r", "s", "t"],#file 6
    ["u", "v", "w"],#file 7
    ["y", "z"]#file 8
]

for i in range(0,7):
    for j in range(0,4):
        if i == 8 and j ==2:
            break
        print(f"posicion[{i}] [{j}]= {"abecedario"[i] [j]}")