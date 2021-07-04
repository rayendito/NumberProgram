# Ryandito Diandaru
# ryanditod@gmail.com
# 081233369604

# Program Angka
# Program dapat memasukkan sejumlah angka, diasumsikan dapat bertipe float
# Program dapat mengurutkan angka yang dimasukkan dan mencetak ke layar
# Program juga dapat  menampilkan keluaran yang mencakup:
# nilai rata-rata, nilai tengah dan hasil perkalian dari semua bilangan yang dimasukkan

# Memasukkan input
# format input angka dipisah dengan spasi:
# Contoh : 7 3 6 2 0 9
# angkas = [float(angka) for angka in input("Masukkan angka-angka : ").split()]

# Sorting Diimplementasi dengan Quick Sort
# Fungsi menerima deret angka dan mereturn deret angka yang sudah terurut
# dengan menggunakan algoritma Quick Sort

import random
import numpy as np

def quickSort(angkas, left, right):
    if(left < right):
        begin, end = left, right
        pivot = angkas[left]
        
        while(begin < end):
            if(pivot <= angkas[end]):
                end -= 1
            elif(angkas[begin] <= pivot):
                begin += 1
            elif(angkas[begin] > pivot and pivot > angkas[end]):
                angkas[begin], angkas[end] = angkas[end], angkas[begin]
                end -= 1

        angkas[left], angkas[end] = angkas[end], angkas[left]
        
        quickSort(angkas, left, end-1)
        quickSort(angkas, end+1, right)

#TESTING USING NUMPY
for i in range(10):
    randnums = [random.randint(-10,10) for i in range(10)]
    print("Awal :",randnums)
    quickSort(randnums,0,9)
    print("Terurut: ", randnums)
    print()

# a = [6, 7, -7, 5, 2, -6, -5, -8, 1, 8]
# b = [3, 5, -3, -1, 1, 2, 4]
# quickSort(a, 0, len(a)-1)
# quickSort(b, 0, len(b)-1)
# print(a)
# print(b)
            
