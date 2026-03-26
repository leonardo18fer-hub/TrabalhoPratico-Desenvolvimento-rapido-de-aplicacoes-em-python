with open("tabuada_9.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"9 x {i} = {9 * i}\n")

print("Arquivo 'tabuada_9.txt' criado!")
