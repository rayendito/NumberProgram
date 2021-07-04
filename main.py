# Ryandito Diandaru
# ryanditod@gmail.com
# 081233369604

# import library untuk testing
import random
import numpy as np

'''
Program Angka
Program dapat memasukkan sejumlah angka, diasumsikan dapat bertipe float
Program dapat mengurutkan angka yang dimasukkan dan mencetak ke layar
Program juga dapat  menampilkan keluaran yang mencakup:
nilai rata-rata, nilai tengah dan hasil perkalian dari semua bilangan yang dimasukkan

Sorting diimplementasi dengan algoritma rekursif quick sort
Fungsi menerima deret angka dan mereturn deret angka yang sudah terurut
dengan menggunakan algoritma Quick Sort

Asumsi program diimplementasi dari nol, tidak menggunakan
built in function sort, atau mean, median, dan sejenisnya
'''

def quickSort(angkas, left, right):
    #cek kondisi awal
    if(left < right):
        #simpan parameter left right untuk diubah
        begin, end = left, right

        #jadikan paling kiri pivot
        pivot = angkas[left]
        
        #partisi dengan paling kiri selalu menjadi pivot
        while(begin < end):
            #lanjut ke kiri/kanan jika memenuhi kondisi
            if(pivot <= angkas[end]):
                end -= 1
            elif(angkas[begin] <= pivot):
                begin += 1

            #jika terpenuhi kondisi tukar, tukar dan jalan satu langkah ke kiri 
            elif(angkas[begin] > pivot and pivot > angkas[end]):
                angkas[begin], angkas[end] = angkas[end], angkas[begin]
                end -= 1

        #tukar nilai pivot dengan titik bertemu di mana begin = end
        angkas[left], angkas[end] = angkas[end], angkas[left]
        
        #rekursi ke partisi bagian kiri dan kanan titik bertemu begin = end
        quickSort(angkas, left, end-1)
        quickSort(angkas, end+1, right)

def rataRata(angkas):
    # inisialisasi return value dengan 0
    sum = 0

    # jumlahkan semua nilai dalam integer
    for i in range(len(angkas)):
        sum += angkas[i]

    # return dengan dibagi dengan panjang deret angka
    try:
        return sum/len(angkas)
    except:
        print("Pembagian dengan 0, input invalid")

def productAll(angkas):
    # cek input tidak kosong
    if(len(angkas) != 0):
        # inisialisasi return value dengan 1 karena perkalian
        prod = 1

        # kalikan seluruh angka dengan return value 
        for i in range(len(angkas)):
            prod *= angkas[i]

        # mereturn hasil
        return prod
    
    # return none jika deret kosong
    return "None"

def median(angkas):
    # menyimpan len input untuk menghemat kalkulasi len
    n = len(angkas)

    # mengurutkan angka terlebih dahulu
    quickSort(angkas,0,n-1)

    # jika berjumlah genap, kembalikan rerata antara 2 angka di tengah,
    # kembalikan angka tengah biasa jika ganjil
    try:
        if(n%2 == 0):
            return (angkas[n//2]+angkas[(n//2)-1])/2
        else:
            return angkas[n//2]
    except:
        print("Akses index di luar range, input invalid")

def main():
    # Memasukkan input
    # format input angka dipisah dengan spasi:
    # Contoh : 7 3 6 2 0 9
    angkas = [float(angka) for angka in input("Masukkan angka-angka : ").split()]
    print("Awal :",angkas)

    # Mengurutkan
    quickSort(angkas,0,len(angkas)-1)
    print("Terurut: ", angkas)

    # Rata-rata
    print("Rata-rata :",rataRata(angkas))

    # Median/nilai tengah
    print("Nilai tengah :", median(angkas))

    # Hasil perkalian
    print("Hasil perkalian seluruh bilangan :", productAll(angkas))

# Jalankan fungsi driver
main()


'''
TESTING ALGORITMA QUICKSORT MENGGUNAKAN NUMPY DAN RANDOM
Uncomment untuk menjalankan
'''
# for i in range(10):
#     randnums = [random.randint(-10,10) for i in range(10)]
#     print("Awal :",randnums)
#     quickSort(randnums,0,9)
#     print("Terurut: ", randnums)
#     print()
