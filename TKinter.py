import tkinter as tk #impor library tkinter untuk membuat GUI, dan disingkat sebagai tk agar lebih mudah digunakan di dalam kode.
from tkinter import messagebox #impor messagebox dari tkinter, yang akan digunakan untuk menampilkan pesan error dalam kotak dialog.

#membuat fungsi untuk validasi input dan menampilkan hasil prediksi ketika tombol "Hasil Prediksi" diklik.
def hasil_prediksi():
    try: #pengondisian blok untuk cek ValueError
        for entry in entries: #loop untuk setiap Entry di dalam list entries. Setiap Entry mewakili input nilai mata pelajaran.
            nilai = int (entry.get()) #mengambil teks dari Entry, lalu mengonversinya menjadi integer agar bisa diproses sebagai angka.
            if not (0 <= nilai <= 100): #pengondisian nilai input untuk menampilkan ValueError
                raise ValueError("Nilai berupa angka 0 - 100.") #menghasilkan error jika nilai tidak berada dalam rentang 0 hingga 100.
            hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve: #menampilkan error ValueError jika input salah.
        messagebox.showerror("Input Error", "Pastikan nilai berupa angka 0 - 100.") #menampilkan pesan error jika ada nilai di luar rentang 0-100 atau bukan angka.

root = tk.Tk() #membuat jendela utama aplikasi.
root.title("Aplikasi Predikski Prodi Pilihan") #membuat judul window
root.geometry("400x540") #menentukan ukuran window utama
root.configure(bg="#f0f0f0") #mengatur warna bg window, diatur dalam warna abu-abu muda

#label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16)) #membuat dan menentukan teks untuk label judul aplikasi, juga setting font arial dengan ukuran 16 
judul_label.pack(pady=20) #mengatur posisi label judul berada di tengah dengan jarak 20px dari atas dan bawah

#frame untuk input nilai mapel
frame_input = tk.Frame(root, bg="#f0f0f0") #membuat dan mengatur frame untuk wadah input nilai mapel dengan warna bg sama dengan warna window
frame_input.pack(pady=10) #mengatur posisi frame dalam window dengan jarak 10px dari atas dan bawah

#entry 10 nilai mapel
entries = [] #membuat list kosong untuk menympan entry setiap nilai
for i in range(1, 11): #looping 10x untuk masing-masing untuk setiap nilai mapel
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i}", bg="#f0f0f0") #membuat label untuk setiap nilai mapel dari 1-10 dan menentukan isi teks nya sekaligus warnanya 
    entry = tk.Entry(frame_input) #mebuat input entry untuk memasukan nolai mapel dari 1-10
    label.grid(row=i-1, column=0, padx=5, pady=5) #membuat label pada kolom 0 dan baris 1 dan jarak antar kolom dan baris dalam frame_input
    entry.grid(row=i-1, column=1, padx=5, pady=5) #membuat entry pada kolom 1 dan baris 1 dan jarak antar kolom dan baris dalam frame_input
    entries.append(entry) #menambahkan entry kedalam list entries agar dapat diakses dalam fungsi hasil_prediksi

#button untuk tampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12), bg="#d1e7dd") #membuat tombol hasil prediksi dan mengatur tampilan teks beserta bg nya. button juga diatur untuk menjalankan fungsi hasil_prediksi() ketika di klik
prediksi_button.pack(pady=20) #mengatur posisi tombol dengan jarak 20px dari atas dan bawah

#label untuk tampilan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="#f0f0f0") #membuat label untuk menampilkan isi hasil prediksi. text="" untuk menentukan teks kosong pada awal label yang akan diperbarui dengan hasil prediksi (setelah menekan button). Juga mengatur jenis ukuran dan warna font.
hasil_label.pack(pady=10) #mengatur posisi label dengan jarak 10px dari atas dan bawah

#running app
root.mainloop() #memulai loop utama tkinter agar GUI tetap berjalan saampai di tutup.