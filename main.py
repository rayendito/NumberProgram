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
angkas = [float(angka) for angka in input("Masukkan angka-angka : ").split()]

# Sorting diimplementasi dengan algoritma rekursif quick sort
# Fungsi menerima deret angka dan mereturn deret angka yang sudah terurut
# dengan menggunakan algoritma Quick Sort

# import library untuk testing
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

def rataRata(angkas):
    sum = 0
    for i in range(len(angkas)):
        sum += angkas[i]
    return sum/len(angkas)

def productAll(angkas):
    prod = 1
    for i in range(len(angkas)):
        sum *= angkas[i]
    return prod

def median(angkas):
    n = len(angkas)
    quickSort(angkas,0,n)
    if(n%2 == 0):
        return (angkas(n//2)+angkas((n//2)-1))/2
    else:
        return angkas(n//2)


# TESTING MENGGUNAKAN NUMPY
# Uncomment untuk menjalankan
# for i in range(10):
#     randnums = [random.randint(-10,10) for i in range(10)]
#     print("Awal :",randnums)
#     quickSort(randnums,0,9)
#     print("Terurut: ", randnums)
#     print()
