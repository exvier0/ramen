def find_middle (array, left, right):
    # Basis: Jika hanya ada satu elemen
    if left == right:
        return array[left]
        #Parameter:
      #array: List yang ingin dicari elemen maksimumnya.
      #left: Indeks awal dari array yang sedang diproses.
      #right: Indeks akhir dari array yang sedang diproses.

    # Bagian: Bagi array menjadi dua bagian
    mid = (left + right) // 2
    #Jika hanya ada satu elemen (ketika left == right), 
    #fungsi langsung mengembalikan elemen tersebut

    # Rekursif: Cari maksimum di kedua bagian
    mid_left = find_middle(array, left, mid)
    mid_right = find_middle(array, mid + 1, right)

    # Kombinasi: Ambil nilai maksimum dari kedua bagian
    return min(mid_left, mid_right)

# Fungsi utama untuk menjalankan aplikasi
def main():
    print("Aplikasi Pencari Elemen Maksimum dengan Divide and Conquer")
    # //Mencetak Judul Aplikasi:
    
    # Input: Masukkan array
    array = input("Masukkan elemen array (pisahkan dengan spasi): ").split()
    array = [int(x) for x in array]
    #Menerima Input dari Pengguna:
    #Pengguna diminta memasukkan array dalam bentuk angka yang dipisahkan spasi.
    #Input diubah menjadi list integer

    
    middle = find_middle(array, 0, len(array) - 1)
    # Proses: Panggil fungsi find_maximum
    # Array yang diinputkan pengguna diproses menggunakan fungsi find_maximum,
    # dengan batas awal (0) dan batas akhir (len(array) - 1):

    # Output: Tampilkan hasil
    print(f"Elemen minimum dalam array adalah: {middle}")
    
    #Menampilkan Hasil:
#Hasil elemen maksimum ditampilkan ke pengguna:

    # Contoh penggunaan
    print("\nContoh Penggunaan:")

    # Contoh 1
    print("\nContoh 1:")
    example_array_1 = [12, 3, 45, 7, 29]
    print(f"Array: {example_array_1}")
    example_max_1 = find_middle(example_array_1, 0, len(example_array_1) - 1)
    print(f"Elemen middle: {example_max_1}")
    
    #Contoh Penggunaan:
    #Untuk memberikan ilustrasi, terdapat dua contoh array bawaan
    #yang diproses menggunakan find_maximum:

#Contoh 1: Array [12, 3, 45, 7, 29], hasil maksimum: 45.
#Contoh 2: Array [5, 8, 3, 1, 9, 6, 7], hasil maksimum: 9
#Contoh Bawaan di Program:
    # Contoh 2
    print("\nContoh 2:")
    example_array_2 = [5, 8, 3, 0, 9, 6, 7]
    print(f"Array: {example_array_2}")
    example_max_2 = find_middle(example_array_2, 0, len(example_array_2) - 1)
    print(f"Elemen middle: {example_max_2}")

if __name__ == "__main__":
    main()
