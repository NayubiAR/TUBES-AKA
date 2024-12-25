import time
import random
import matplotlib.pyplot as plt

# Fungsi untuk menguji perbandingan waktu eksekusi antara kedua algoritma
def uji_perbandingan_waktu():
    jumlah_barang_list = [5, 10, 20, 30, 40, 50]
    running_time_greedy_list = []
    running_time_rekursif_list = []
    nilai_greedy_list = []
    nilai_rekursif_list = []

    for jumlah_barang in jumlah_barang_list:
        daftar_barang = [
            Barang(f"Barang_{i}", ukuran=5, berat=5, nilai=50) for i in range(jumlah_barang)
        ]

        kapasitas_ukuran = 20
        kapasitas_berat = 50

        # Mengukur running time untuk algoritma greedy
        start = time.time()
        nilai_greedy, _ = hitungNilaiMaksimum(daftar_barang, kapasitas_ukuran, kapasitas_berat)
        end = time.time()
        running_time_greedy = end - start
        running_time_greedy_list.append(running_time_greedy)
        nilai_greedy_list.append(nilai_greedy)

        # Mengukur running time untuk algoritma rekursif
        start = time.time()
        _, nilai_rekursif = hitungNilaiMaksimum(daftar_barang, kapasitas_ukuran, kapasitas_berat)
        end = time.time()
        running_time_rekursif = end - start
        running_time_rekursif_list.append(running_time_rekursif)
        nilai_rekursif_list.append(nilai_rekursif)

    # Menampilkan hasil running time dan nilai
    for i, jumlah_barang in enumerate(jumlah_barang_list):
        print(f"Jumlah Barang: {jumlah_barang}")
        print(f"  Running Time Greedy: {running_time_greedy_list[i]:.6f} detik, Nilai Greedy: {nilai_greedy_list[i]}")
        print(f"  Running Time Rekursif: {running_time_rekursif_list[i]:.6f} detik, Nilai Rekursif: {nilai_rekursif_list[i]}")
        print("-" * 50)

    # Membuat grafik perbandingan running time
    plt.plot(jumlah_barang_list, running_time_greedy_list, label='Greedy', marker='o')
    plt.plot(jumlah_barang_list, running_time_rekursif_list, label='Rekursif (Memoization)', marker='o')

    plt.xlabel('Jumlah Barang')
    plt.ylabel('Running Time (detik)')
    plt.title('Perbandingan Running Time Algoritma Greedy vs Rekursif')
    plt.legend()
    plt.grid(True)
    plt.show()

# Panggil fungsi uji_perbandingan_waktu untuk menghasilkan grafik dan hasil
uji_perbandingan_waktu()