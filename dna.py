dna = input()
s = 1
for i in range(-len(dna), -1):
    if dna[i] == dna[i+1]:
        s = s+1
        continue
    elif dna[i] != dna[i+1]:
        print(dna[i], end="")
        print(s, end="")
        s = 1
print(dna[-1], end="")
print(s)

