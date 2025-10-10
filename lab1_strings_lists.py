#6. Annotate the sequence 'gctagctagctagcta' with exons [(0,3),(5,8)]
dna = 'gctagctagctagcta'
exons = [(0,3),(5,8)] #list of tuples with start and end positions of exons
annot = list(dna.lower()) 
for s,e in exons:    
  for i in range(s,e):   
    annot[i] = annot[i].upper() #changing to uppercase for exons
print(''.join(annot))
# Expected output: GCTAgCTAGctagcta

#7. Count how many times each nucleotide (A,T,G,C) occurs in the DNA string.
dna = 'gctagctagctagcta'
counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'} #counting each nucleotide 
print(counts)

#8. Reverse a DNA sequence and print it.
dna = 'gctagctagctagcta'
print(dna[::-1]) #reverse of the string