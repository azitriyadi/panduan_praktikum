# 🚀 Panduan Praktikum: Python Lanjutan & Kolaborasi GitHub

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-VCS-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Collaboration-181717?logo=github&logoColor=white)](https://github.com/)
[![VS Code](https://img.shields.io/badge/IDE-VS_Code-007ACC?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)

Selamat datang di repositori resmi praktikum **Python Lanjutan & Alur Kerja Kolaborasi GitHub**! Repositori ini disusun sebagai panduan praktikum interaktif yang menggabungkan penguasaan logika pemrograman Python dengan praktik alur kerja Git standar industri (*fork*, *branch*, *atomic commit*, dan *pull request*).

---

## 📖 Lembar Panduan & Cheat Sheet
Seluruh instruksi detail, materi, dan kode sumber latihan telah disiapkan dalam dokumen khusus:

👉 **[Buka Dokumen Cheat Sheet Praktikum](cheat-sheet.md)** 👈

> [!CAUTION]
> ### 🛑 TATA TERTIB & PERINGATAN RESMI: DILARANG CURI START!
> 1. **Tombol Salin Ditiadakan**: Seluruh kode latihan disajikan dalam bentuk **Visual Code Card (SVG)** tanpa tombol salin (*copy button*) bawaan. Mahasiswa **wajib mengetik ulang secara mandiri (*muscle memory*)** ke dalam teks editor VS Code.
> 2. **Tugas Mandiri (operasi3.py & kalkulator.py)**: Terdiri dari modul logika fungsi matematika mandiri (`operasi3.py`) dan aplikasi kalkulator konsol bermenu interaktif (`kalkulator.py`).
> 3. **Tunggu Aba-Aba**: Buka menu lipat (*drop-down*) hanya jika telah diinstruksikan secara resmi oleh pemateri di depan kelas.
> 4. **Pahami Analogi & Alur Logika**: Pahami alur berpikir komputasional dan penataan indentasi 4 spasi pada Python.

---

## 🎯 Ringkasan Materi Praktikum

| No | Modul / Praktikum | Berkas Target | Topik Bahasan & Integrasi |
|:---:|:---|:---|:---|
| 1 | **Praktikum 1** | `praktikum_01.py` | *Nested If* Modular (Evaluasi Kehadiran & Nilai Kelulusan) |
| 2 | **Praktikum 2** | `praktikum_02.py` | Pengujian Bilangan Prima, Operator Modulus (`%`), dan Berhenti Cepat |
| 3 | **Praktikum 3** | `praktikum_03.py` | Deret Aritmatika & Akumulator Nilai (Pengembalian *Tuple*) |
| 4 | **Praktikum 4** | `praktikum_04.py` | Matriks 2D (*Nested Loop*) & Analisis Statistik Wadah `list` |
| 5 | **Tugas Mandiri 1** | `operasi3.py` | Modul Logika & Fungsi Matematika Mandiri (+, -, *, /, Modulus, Deret) |
| 6 | **Tugas Mandiri 2** | `kalkulator.py` | **Aplikasi Kalkulator Konsol Bermenu (While True, Nested Loop, .isdigit)** |

---

## 📁 Struktur Folder Wajib Mahasiswa

Setiap mahasiswa wajib membuat satu folder kerja pribadi di dalam repositori hasil *fork* dengan format penamaan **`nama-NPM`** (huruf kecil semua, dipisahkan tanda strip):

```text
tugas-minggu-2/
└── ahmad-2610001/             <-- Ganti dengan nama panggilan dan NPM kalian
    ├── .gitignore             <-- Berkas pengabaian file sampah & virtual env
    ├── README.md              <-- Berkas identitas pribadi & catatan pengerjaan
    ├── praktikum_01.py        <-- Latihan Nested If
    ├── praktikum_02.py        <-- Latihan Prima & Modulus
    ├── praktikum_03.py        <-- Latihan Deret & Akumulator
    ├── praktikum_04.py        <-- Latihan Matriks & List
    ├── operasi3.py            <-- Modul Logika & Fungsi Matematika (Tugas Mandiri 1)
    └── tugas3_menu.py         <-- Program Utama Kalkulator Bermenu (Tugas Mandiri 2)
```

> [!IMPORTANT]
> Pastikan struktur penamaan berkas persis seperti di atas untuk memudahkan verifikasi otomatis dan penilaian oleh tim pengajar.

### 📝 Format Wajib Isi `README.md` Mahasiswa

Setiap mahasiswa wajib mengisi berkas `README.md` di dalam folder kerjanya dengan format berikut:

```markdown
# Tugas Minggu 2 - Pelatihan Python Lanjutan & GitHub

- **Nama**     : [Nama Lengkap]
- **NPM**      : [NPM Mahasiswa]
- **Kelompok** : [Nomor Kelompok]

## Daftar Berkas
1. `praktikum_01.py` : Latihan Percabangan Bertingkat (Nested If)
2. `praktikum_02.py` : Latihan Deteksi Bilangan Prima & Modulus
3. `praktikum_03.py` : Latihan Deret Aritmatika & Akumulator
4. `praktikum_04.py` : Latihan Matriks Perkalian & List
5. `operasi3.py`     : Modul Operasi Matematika
6. `tugas3_menu.py`  : Aplikasi Konsol Utama Kalkulator
```

---

## 🛠️ Prasyarat & Persiapan Lingkungan

Pastikan perangkat kalian telah terpasang perangkat lunak berikut sebelum praktikum dimulai:

1. **Python 3.10+**: Periksa via terminal dengan `python --version` atau `python3 --version`.
2. **Git**: Pastikan konfigurasi nama dan email lokal sudah sesuai akun GitHub:
   ```bash
   git config --global user.name "Nama Lengkap Kalian"
   git config --global user.email "email_kalian@domain.com"
   ```
3. **Visual Studio Code**: Disarankan memasang ekstensi resmi:
   - *Python* (oleh Microsoft)
   - *Pylance*

---

## ⚡ Cara Menjalankan Berkas Python

Buka terminal pada direktori folder kerja kalian (`ahmad-2610001/`), lalu jalankan file yang diinginkan:

```bash
# Menjalankan Praktikum 1
python praktikum_01.py

# Menjalankan Praktikum 2
python praktikum_02.py

# Menjalankan Praktikum 3
python praktikum_03.py

# Menjalankan Praktikum 4
python praktikum_04.py

# Menjalankan Program Tugas Mandiri
python kalkulator.py
```

---

## 📤 Alur Pengumpulan ke GitHub (Ringkas)

Alur lengkap beserta penjelasan perintah dapat dibaca di **[cheat-sheet.md](cheat-sheet.md#-panduan-alur-pengumpulan-tugas-ke-github)**.

```mermaid
flowchart LR
    A[Fork Repo Kelompok] --> B[Clone ke Komputer Lokal]
    B --> C[Buat Folder nama-NPM]
    C --> D[Ketik Praktikum & Tugas]
    D --> E[Minimal 3x Atomic Commit]
    E --> F[Push ke origin main]
    F --> G[Buat Pull Request ke Induk]
```

Format judul Pull Request resmi:
```text
Nama Lengkap - NPM - Tugas Minggu 2
```

---

<div align="center">
  <sub>© Tim Dosen & Asisten Laboratorium Praktikum • Dibuat dengan dedikasi untuk pengalaman belajar terbaik</sub>
</div>
