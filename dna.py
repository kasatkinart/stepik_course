DNA = input()
dna = DNA.lower()+'1'
s=1
for i in range(1, len(dna)):
    if dna[i-1] == dna[i]:
      s = s+1
      continue
    else:
        print(dna[i-1], end='')
        print(s,end='')
        s=1


