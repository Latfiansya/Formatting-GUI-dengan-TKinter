import tkinter as tk
from tkinter import messagebox

#fungsi memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int (entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai berupa angka 0 - 100.")
            hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan nilai berupa angka 0 - 100.")

root = tk.Tk()
root.title("Aplikasi Predikski Prodi Pilihan")
root.geometry("400x540")
root.configure(bg="#f0f0f0")

#label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.pack(pady=20)

#frame untuk input nilai mapel
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

#entry 10 nilai mapel
entries = []
for i in range(1, 11):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i}", bg="#f0f0f0")
    entry = tk.Entry(frame_input)
    label.grid(row=i-1, column=0, padx=5, pady=5)
    entry.grid(row=i-1, column=1, padx=5, pady=5)
    entries.append(entry)

#button untuk tampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12), bg="#d1e7dd")
prediksi_button.pack(pady=20)

#label untuk tampilan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=10)

#running app
root.mainloop()