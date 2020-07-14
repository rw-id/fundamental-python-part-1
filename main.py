# SINTAKS DASAR PYTHON
# SEQUENTIAL = Eksekusi kode berurutan
print('Hello World!')
print('by Riffadi')
print('Tanggal 14 Juli 2020')
print('-' * 20)


# 2. Percabangan(branching)  = eksekusi terpilih
# Membuat data / variabel

data = False

if data:
 print('Done')
else:
 print('NOT COMPLETE')
 print('-' * 20)

# 3. Perulangan(looping)
shape = 4

for shape in range(1, shape+1): # perulangan dimulai dari 0
 print(f'This is shape {shape}')  # f = fungsi string terbaru di python untuk menysisipkan variable kedalam teks