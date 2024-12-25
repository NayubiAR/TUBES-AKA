import time
import random
import matplotlib.pyplot as plt

# Barang mewakili sebuah item dengan atribut tertentu
class Barang:
    def _init_(self, nama, ukuran, berat, nilai):
        self.nama = nama
        self.ukuran = ukuran
        self.berat = berat
        self.nilai = nilai
        self.rasio = 0

# memo akan menyimpan hasil perhitungan ransel2D[i][u][b]
memo = []

# UNDEF sebagai penanda bahwa belum dihitung
UNDEF = -1

# FungsiRanselGreedyIteratif menghitung nilai maksimum menggunakan algoritma greedy secara iteratif
def FungsiRanselGreedyIteratif(daftarBarang, kapasitasUkuran, kapasitasBerat):
    for brg in daftarBarang:
        brg.rasio = brg.nilai / brg.berat

    daftarBarang.sort(key=lambda brg: brg.rasio, reverse=True)

    totalNilai = 0.0
    totalUkuran = 0
    totalBerat = 0

    for brg in daftarBarang:
        if totalUkuran + brg.ukuran <= kapasitasUkuran and totalBerat + brg.berat <= kapasitasBerat:
            totalNilai += brg.nilai
            totalUkuran += brg.ukuran
            totalBerat += brg.berat
        else:
            sisaUkuran = kapasitasUkuran - totalUkuran
            sisaBerat = kapasitasBerat - totalBerat
            jumlahDiambil = min(sisaUkuran, sisaBerat) / brg.berat
            totalNilai += jumlahDiambil * brg.nilai
            break

    return totalNilai

# FungsiRansel2DRekursif menghitung nilai maksimum dengan cara rekursif + memo
def FungsiRansel2DRekursif(daftarBarang, i, u, b):
    if i < 0 or u <= 0 or b <= 0:
        return 0

    if memo[i][u][b] != UNDEF:
        return memo[i][u][b]

    opsiTidakAmbil = FungsiRansel2DRekursif(daftarBarang, i - 1, u, b)

    opsiAmbil = 0
    if daftarBarang[i].ukuran <= u and daftarBarang[i].berat <= b:
        opsiAmbil = FungsiRansel2DRekursif(daftarBarang, i - 1, u - daftarBarang[i].ukuran, b - daftarBarang[i].berat) + daftarBarang[i].nilai

    hasilTerbaik = max(opsiTidakAmbil, opsiAmbil)

    memo[i][u][b] = hasilTerbaik

    return hasilTerbaik

# Fungsi utama untuk menghitung nilai maksimum menggunakan kedua algoritma
def hitungNilaiMaksimum(daftarBarang, kapasitasUkuran, kapasitasBerat):
    nilaiMaksGreedy = FungsiRanselGreedyIteratif(daftarBarang, kapasitasUkuran, kapasitasBerat)

    global memo
    memo = [[[UNDEF for _ in range(kapasitasBerat + 1)] for _ in range(kapasitasUkuran + 1)] for _ in range(len(daftarBarang))]

    nilaiMaksDinamis = FungsiRansel2DRekursif(daftarBarang, len(daftarBarang) - 1, kapasitasUkuran, kapasitasBerat)

    return nilaiMaksGreedy, nilaiMaksDinamis