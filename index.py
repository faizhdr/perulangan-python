# angka1 = int(input("Masukkan angka pertama : "))
# angka2 = int(5)

# hasil = angka1 + angka2
# print(hasil)
# hasil2 = (int(4) + hasil)
# print(hasil2)

#perbedaan end dan sep
# print('A', 1, 'xyz', 2, end='-')
# print('A', 1, 'xyz', 2, sep='-')

#membuat array 
#index dari 0=Yamaha
# motor = ['Yamaha', 'Mio', 'Vario']
# for i in range(3):
#     print(motor[i]) 

#membuat array buah 
#menggunakan perulangan for
# buah = ['nanas', 'apel', 'jeruk', 'mangga', 'durian', 'semangka', 'jambu']
# for buahan in buah:
#     print("Nama buah : ",buahan)

# #menggunakan manual
# print("Nama buah : ", buah[0])
# print("Nama buah : ", buah[1])
# #dst

#membuat program biodata

#membuat variabel nama_saya yang menerima inputan
# nama_saya = input("Masukkkan Nama Lengkap : ")

# #membuat variabel asal_daerah yang menerima inputan
# asal_daerah = input("Masukkan Asal Daerah : ")
# # 
# #membuat array biodata untu mengumpulkan hasil inputan
# biodata = [nama_saya, asal_daerah]
# for isi_biodata in biodata:
#     print(isi_biodata)

#membuat array siswa
siswa = []

#membuat perlangan for
for i in range(3):

    #menngecek nilai indeks
    print("")
    print("ini adalah indeks ke-",i)

    #input data nama siswa
    nama_siswa = input("Masukkan nama siswa : ")

    #memasukkan hasil inputan naa ke array siswa
    siswa.append(nama_siswa)

print("")

#membuat perulangan untuk mengecek data dari array siswa
for k in siswa:
    
    #mengecek array siswa
    print("Nama siswa : ", k)