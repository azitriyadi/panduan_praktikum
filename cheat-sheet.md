# 📖 Cheat Sheet Praktikum: Python Lanjutan & Kolaborasi GitHub

Selamat datang di lembar contekan (*cheat sheet*) resmi praktikum **Python Lanjutan & Kolaborasi GitHub**.

> [!CAUTION]
> ### ⚠️ TATA TERTIB: DILARANG CURI START!
> Seluruh kode praktikum dan tugas mandiri di bawah ini **sengaja disembunyikan** di dalam menu lipat (*drop-down/accordion*).
> - **JANGAN** membuka atau mengetik kode sebelum ada instruksi resmi dari dosen/pemateri di depan kelas!
> - Pahami logika dan analogi yang diterangkan terlebih dahulu, kemudian ketik mandiri (*jangan asal copy-paste*).

---

## 📑 Navigasi Praktikum
Gunakan tautan di bawah ini untuk melompat langsung ke sesi yang sedang berlangsung:

- [1. Konfigurasi Berkas `.gitignore`](#1-konfigurasi-berkas-gitignore)
- [2. Praktikum 1: Nested If - Evaluasi Kelulusan](#-praktikum-1-nested-if-evaluasi-kelulusan) (`praktikum_01.py`)
- [3. Praktikum 2: Bilangan Prima & Break](#-praktikum-2-bilangan-prima--break) (`praktikum_02.py`)
- [4. Praktikum 3: Deret Aritmatika & Akumulator](#-praktikum-3-deret-aritmatika--akumulator) (`praktikum_03.py`)
- [5. Praktikum 4: Nested Loop & Manipulasi List](#-praktikum-4-nested-loop--manipulasi-list) (`praktikum_04.py`)
- [6. Tugas Mandiri (Modul & Menu Konsol)](#-tugas-mandiri-aplikasi-kalkulator-konsol) (`operasi3.py` & `tugas3_menu.py`)
- [7. Panduan Pengumpulan Tugas ke GitHub](#-panduan-alur-pengumpulan-tugas-ke-github)

---

## 1. Konfigurasi Berkas `.gitignore`
Pastikan berkas `.gitignore` diletakkan di dalam folder mahasiswa kalian agar file-file sampah Python dan konfigurasi IDE tidak ikut terunggah ke repositori GitHub.

<details>
<summary><b>📄 Lihat Isi Template Berkas <code>.gitignore</code></b></summary>

<br>

Simpan dengan nama berkas: `.gitignore`

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Lingkungan Virtual & IDE
.vscode/
.idea/
*.swp

# Berkas Environment / Rahasia
.env
.venv/
env/
venv/
```
</details>

---

## 2. Praktikum 1: Nested If (Evaluasi Kelulusan)
* **Target File:** `praktikum_01.py`
* **Konsep Inti:** Percabangan Bersarang (*Nested If*), Gerbang Validasi Berlapis (Kehadiran $\rightarrow$ Nilai).

<details>
<summary><b>🔒 [KLIK UNTUK MEMBUKA KODE] Praktikum 1: Nested If</b></summary>

<br>

> ⚠️ **Peringatan:** Buka hanya saat pemateri menginstruksikan Praktikum 1 dimulai!

```python
# ==========================================
# PRAKTIKUM 1: NESTED IF (KELULUSAN)
# Simpan sebagai: praktikum_01.py
# ==========================================

kehadiran = int(input("Jumlah kehadiran (1-14): "))
nilai = int(input("Nilai ujian (0-100): "))

# Pintu Luar: Evaluasi Kehadiran Mahasiswa
if kehadiran >= 12:
    # Pintu Dalam: Evaluasi Nilai Ujian (hanya dievaluasi jika kehadiran memenuhi)
    if nilai >= 75:
        print("Status: LULUS - Nilai Memuaskan")
    else:
        print("Status: REMEDIAL - Nilai Ujian Kurang")
else:
    print("Status: TIDAK LULUS - Kehadiran Kurang dari 12")
```

#### 💡 Poin Pembahasan Logika:
1. **Pintu Luar (`if kehadiran >= 12`)**: Berfungsi sebagai penyaring utama. Jika mahasiswa tidak memenuhi syarat kehadiran minimum, kondisi nilai ujian sama sekali tidak diperiksa.
2. **Pintu Dalam (`if nilai >= 75`)**: Berjalan di dalam blok `if` pertama untuk menentukan predikat kelulusan akhir.

</details>

---

## 3. Praktikum 2: Bilangan Prima & Break
* **Target File:** `praktikum_02.py`
* **Konsep Inti:** Perulangan `for`, Operator Modulus (`%`), Penggunaan Penanda Boolean (*Flag*), dan Pernyataan `break`.

<details>
<summary><b>🔒 [KLIK UNTUK MEMBUKA KODE] Praktikum 2: Bilangan Prima & Break</b></summary>

<br>

> ⚠️ **Peringatan:** Buka hanya saat pemateri menginstruksikan Praktikum 2 dimulai!

```python
# ==========================================
# PRAKTIKUM 2: BILANGAN PRIMA & BREAK
# Simpan sebagai: praktikum_02.py
# ==========================================

angka = int(input("Masukkan angka bulat positif: "))
is_prima = True  # Prasangka awal: asumsikan angka adalah prima

if angka < 2:
    is_prima = False  # Angka kurang dari 2 (seperti 0, 1, atau negatif) bukan prima
else:
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            is_prima = False  # Ditemukan faktor pembagi selain 1 dan dirinya sendiri
            break             # Langsung hentikan pencarian seketika untuk efisiensi

if is_prima:
    print(f"Hasil: {angka} adalah BILANGAN PRIMA")
else:
    print(f"Hasil: {angka} BUKAN bilangan prima")
```

#### 💡 Poin Pembahasan Logika:
1. **Prasangka Awal (*Flagging*)**: Variabel `is_prima = True` disiapkan di awal sebelum perulangan menguji ada tidaknya pembagi habis.
2. **Optimasi dengan `break`**: Begitu ditemukan satu saja angka pembagi dengan sisa bagi nol (`angka % pembagi == 0`), perulangan langsung dihentikan detik itu juga tanpa menghabiskan siklus CPU yang tidak perlu.

</details>

---

## 4. Praktikum 3: Deret Aritmatika & Akumulator
* **Target File:** `praktikum_03.py`
* **Konsep Inti:** Pola Penjumlahan Berulang (*Accumulator Pattern*), Penambahan Nilai Beda Deret, dan Parameter `end=" "` pada fungsi `print`.

<details>
<summary><b>🔒 [KLIK UNTUK MEMBUKA KODE] Praktikum 3: Deret & Akumulator</b></summary>

<br>

> ⚠️ **Peringatan:** Buka hanya saat pemateri menginstruksikan Praktikum 3 dimulai!

```python
# ==========================================
# PRAKTIKUM 3: DERET & AKUMULATOR
# Simpan sebagai: praktikum_03.py
# ==========================================

awal = int(input("Suku Pertama : "))
beda = int(input("Beda Deret   : "))
banyak = int(input("Banyak Suku  : "))

suku = awal
total = 0  # Celengan akumulator untuk menampung total jumlah

print("Susunan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku    # Memasukkan nilai suku saat ini ke dalam akumulator
    suku += beda     # Menyiapkan nilai suku untuk iterasi berikutnya

print(f"\nTotal Jumlah Seluruh Deret = {total}")
```

#### 💡 Poin Pembahasan Logika:
1. **Pola Akumulator (`total += suku`)**: Diibaratkan seperti celengan yang setiap putaran iterasi terus dimasukkan nilai suku terbaru.
2. **Parameter `end=" "`**: Mencegah fungsi `print()` membuat baris baru otomatis, sehingga deret tercetak memanjang ke samping.

</details>

---

## 5. Praktikum 4: Nested Loop & Manipulasi List
* **Target File:** `praktikum_04.py`
* **Konsep Inti:** Perulangan Bersarang (*Nested Loop 2D*), Karakter Tabulasi (`\t`), Struktur Data `list`, Metode `.append()`, dan Fungsi Agregasi `max()`.

<details>
<summary><b>🔒 [KLIK UNTUK MEMBUKA KODE] Praktikum 4: Nested Loop & List</b></summary>

<br>

> ⚠️ **Peringatan:** Buka hanya saat pemateri menginstruksikan Praktikum 4 dimulai!

```python
# ==========================================
# PRAKTIKUM 4: NESTED LOOP & LIST
# Simpan sebagai: praktikum_04.py
# ==========================================

# 1. Matriks Tabel Perkalian (Nested Loop)
print("--- Tabel Perkalian Matriks (1-3) ---")
for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris * kolom}\t", end="")
    print()  # Pindah baris setelah inner loop kolom tuntas dieksekusi

# 2. Pengenalan Wadah Data List
print("\n--- Pengolahan Data List ---")
nilai_maba = [80, 75, 90]
nilai_maba.append(95)  # Menambahkan data baru di posisi paling belakang

print("Seluruh Isi List :", nilai_maba)
print("Data Pertama (0) :", nilai_maba[0])  # Indeks list selalu berawal dari 0
print("Nilai Tertinggi  :", max(nilai_maba))
```

#### 💡 Poin Pembahasan Logika:
1. **Outer Loop & Inner Loop**: Perulangan `baris` mengontrol pergerakan vertikal, sedangkan perulangan `kolom` mencetak elemen horizontal.
2. **Karakter Escape `\t`**: Memberikan jarak tabulasi otomatis agar tata letak kolom matriks sejajar rapi.

</details>

---

## 6. Tugas Mandiri: Aplikasi Kalkulator Konsol
Tugas mandiri terdiri dari **2 berkas** yang saling terhubung: modul fungsi matematika (`operasi3.py`) dan menu interaktif utama (`tugas3_menu.py`).

### 📦 Berkas 1: Modul Operasi Matematika (`operasi3.py`)
<details>
<summary><b>🔒 [KLIK UNTUK MEMBUKA KODE] Berkas Modul: operasi3.py</b></summary>

<br>

> ⚠️ **Peringatan:** Pastikan modul ini dibuat di folder yang sama dengan `tugas3_menu.py`.

```python
# ==========================================
# TUGAS MANDIRI: MODUL FUNGSI MATEMATIKA
# Simpan sebagai: operasi3.py
# ==========================================

def hitung_tambah(a, b):
    """Menghitung hasil penjumlahan dua bilangan"""
    return a + b

def hitung_kurang(a, b):
    """Menghitung hasil pengurangan dua bilangan"""
    return a - b

def hitung_kali(a, b):
    """Menghitung hasil perkalian dua bilangan"""
    return a * b

def hitung_bagi(a, b):
    """Menghitung hasil pembagian dua bilangan dengan pencegahan pembagian nol"""
    if b == 0:
        return "Error: Pembagi tidak boleh bernilai nol"
    return a / b
```
</details>

### 💻 Berkas 2: Program Utama Menu Interaktif (`tugas3_menu.py`)
<details>
<summary><b>🔒 [KLIK UNTUK MEMBUKA KODE] Berkas Utama: tugas3_menu.py</b></summary>

<br>

> ⚠️ **Peringatan:** Buka jika sudah menyelesaikan modul `operasi3.py`.

```python
# ==========================================
# TUGAS MANDIRI: PROGRAM MENU KONSOL
# Simpan sebagai: tugas3_menu.py
# ==========================================
import operasi3

while True:
    print("\n" + "=" * 35)
    print("   APLIKASI KALKULATOR KONSOL")
    print("=" * 35)
    print("1. Hitung Operasi Matematika")
    print("2. Tabel Perkalian (Nested Loop)")
    print("3. Keluar")
    print("=" * 35)
    
    pilihan = input("Pilih Menu (1-3): ")
    
    if pilihan == "3":
        print("Terima kasih telah menggunakan program!")
        break
    elif pilihan == "1":
        input_angka1 = input("Masukkan angka pertama: ")
        input_angka2 = input("Masukkan angka kedua  : ")
        
        # Validasi input untuk mencegah program crash akibat bukan angka
        if input_angka1.isdigit() and input_angka2.isdigit():
            a = int(input_angka1)
            b = int(input_angka2)
            print(f"Hasil Penjumlahan: {operasi3.hitung_tambah(a, b)}")
        else:
            print("Peringatan: Masukan harus berupa angka bulat positif!")
    elif pilihan == "2":
        print("\n--- Tabel Matriks Perkalian ---")
        for i in range(1, 4):
            for j in range(1, 4):
                print(f"{i * j}\t", end="")
            print()
    else:
        print("Pilihan menu tidak valid, silakan coba lagi!")
```
</details>

---

## 7. Panduan Alur Pengumpulan Tugas ke GitHub

Ikuti tahapan alur Git di bawah ini secara disiplin untuk mengumpulkan hasil praktikum dan tugas mandiri:

<details>
<summary><b>🚀 [KLIK UNTUK MELIHAT LANGKAH KERJA GIT & PENGUMPULAN]</b></summary>

<br>

### Langkah 1: Fork Repositori
1. Buka repositori `tugas-minggu-2` milik organisasi kelompok di GitHub.
2. Klik tombol **Fork** di pojok kanan atas untuk menduplikasi repositori ke akun GitHub pribadi kalian.

---

### Langkah 2: Clone ke Komputer Lokal
Jalankan perintah berikut di terminal (*Command Prompt / PowerShell / Git Bash*):
```bash
git clone https://github.com/USERNAME-KAMU/tugas-minggu-2.git
cd tugas-minggu-2
```

---

### Langkah 3: Buat Folder Pribadi Sesuai Format
Buat direktori baru dengan format `nama-NPM`:
```bash
mkdir ahmad-2610001
cd ahmad-2610001
```
> *Ganti `ahmad-2610001` dengan nama panggilan dan NPM resmi kalian.*

Pindahkan seluruh berkas tugas praktikum ke dalam folder tersebut:
- `.gitignore`
- `README.md`
- `praktikum_01.py`
- `praktikum_02.py`
- `praktikum_03.py`
- `praktikum_04.py`
- `operasi3.py`
- `tugas3_menu.py`

---

### Langkah 4: Lakukan Commit Bertahap (Minimal 3 Commit)
Disiplin riwayat *commit* menjadi penilaian kolaborasi. Jangan melakukan satu commit borongan sekaligus!

```bash
# Commit 1: Menambahkan modul matematika
git add operasi3.py
git commit -m "feat: menambahkan modul operasi matematika"

# Commit 2: Menyusun program menu utama dan seluruh praktikum
git add tugas3_menu.py praktikum_*.py
git commit -m "feat: menyelesaikan modul menu konsol dan latihan praktikum 1-4"

# Commit 3: Menambahkan dokumentasi README pribadi dan konfigurasi gitignore
git add README.md .gitignore
git commit -m "docs: menambahkan dokumentasi identitas dan konfigurasi gitignore"
```

---

### Langkah 5: Push ke Repositori Fork
Unggah seluruh perubahan lokal ke branch utama GitHub pribadi kalian:
```bash
git push origin main
```

---

### Langkah 6: Ajukan Pull Request (PR)
1. Buka kembali halaman repositori fork kalian di GitHub.
2. Klik tombol **Contribute** $\rightarrow$ **Open Pull Request**.
3. Pastikan *base repository* mengarah ke repositori induk organisasi.
4. Gunakan format judul Pull Request:
   ```text
   Nama Lengkap - NPM - Tugas Minggu 2
   ```
5. Isi deskripsi PR dengan ringkasan tugas yang telah diselesaikan, lalu klik **Create Pull Request**.

</details>

---

<div align="center">
  <sub>Praktikum Python Lanjutan & Kolaborasi GitHub • Dibuat untuk panduan praktikum interaktif</sub>
</div>