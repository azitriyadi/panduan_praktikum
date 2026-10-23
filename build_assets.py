import os
import io
import html
import keyword
import tokenize

KEYWORDS = set(keyword.kwlist) | {'True', 'False', 'None'}
BUILTINS = {
    'print', 'input', 'int', 'float', 'str', 'list', 'dict', 'set',
    'tuple', 'len', 'range', 'max', 'min', 'sum', 'append', 'isdigit',
    'map', 'open', 'type', '__name__'
}

def escape_xml(s):
    return html.escape(s, quote=True)

def generate_python_svg(filename, code_text, badge_text="Ketik Ulang (No Copy)"):
    lines = code_text.strip().split("\n")
    num_lines = len(lines)
    
    line_height = 22
    header_height = 42
    top_margin = 18
    bottom_margin = 20
    total_height = header_height + top_margin + (num_lines * line_height) + bottom_margin
    total_width = 820
    
    # Tokenize Python code
    token_spans_by_line = {i: [] for i in range(1, num_lines + 1)}
    
    try:
        tokens = tokenize.tokenize(io.BytesIO(code_text.strip().encode('utf-8')).readline)
        for tok in tokens:
            t_type = tok.type
            t_str = tok.string
            srow, scol = tok.start
            erow, ecol = tok.end
            
            if t_type in (tokenize.ENCODING, tokenize.ENDMARKER, tokenize.NEWLINE, tokenize.NL):
                continue
            
            # Determine color
            color = "#cdd6f4" # default text
            font_weight = "normal"
            font_style = "normal"
            
            if t_type == tokenize.COMMENT:
                color = "#9399b2"
                font_style = "italic"
            elif t_type == tokenize.STRING:
                color = "#a6e3a1"
            elif t_type == tokenize.NUMBER:
                color = "#fab387"
            elif t_type == tokenize.NAME:
                if t_str in KEYWORDS:
                    color = "#cba6f7"
                    font_weight = "bold"
                elif t_str in BUILTINS:
                    color = "#89b4fa"
                else:
                    color = "#cdd6f4"
            elif t_type == tokenize.OP:
                color = "#89dceb"
                
            if srow in token_spans_by_line:
                token_spans_by_line[srow].append({
                    'text': t_str,
                    'scol': scol,
                    'ecol': ecol,
                    'color': color,
                    'weight': font_weight,
                    'style': font_style
                })
    except Exception as e:
        pass

    # Build SVG content
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width} {total_height}" width="100%" height="{total_height}" style="max-width: {total_width}px; border-radius: 10px; font-family: Consolas, \'Cascadia Code\', \'Fira Code\', monospace;">')
    
    # Window Frame & Background
    svg_lines.append(f'  <!-- Window Background -->')
    svg_lines.append(f'  <rect width="{total_width}" height="{total_height}" rx="10" fill="#181825" stroke="#313244" stroke-width="1.5"/>')
    svg_lines.append(f'  <rect y="{header_height}" width="{total_width}" height="{total_height - header_height}" fill="#1e1e2e"/>')
    
    # Header Bar
    svg_lines.append(f'  <!-- Header Bar -->')
    svg_lines.append(f'  <path d="M 0 10 Q 0 0 10 0 L {total_width - 10} 0 Q {total_width} 0 {total_width} 10 L {total_width} {header_height} L 0 {header_height} Z" fill="#11111b" stroke="#313244" stroke-width="1"/>')
    
    # macOS window buttons
    svg_lines.append(f'  <circle cx="20" cy="21" r="6" fill="#f38ba8"/>')
    svg_lines.append(f'  <circle cx="38" cy="21" r="6" fill="#f9e2af"/>')
    svg_lines.append(f'  <circle cx="56" cy="21" r="6" fill="#a6e3a1"/>')
    
    # Window Title
    svg_lines.append(f'  <text x="78" y="26" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#cdd6f4">{escape_xml(filename)}</text>')
    
    # Badge (Ketik Ulang / Dilarang Salin)
    badge_width = 220
    badge_x = total_width - badge_width - 15
    svg_lines.append(f'  <!-- Anti Copy Badge -->')
    svg_lines.append(f'  <rect x="{badge_x}" y="9" width="{badge_width}" height="24" rx="12" fill="#f38ba8" fill-opacity="0.12" stroke="#f38ba8" stroke-width="1" stroke-opacity="0.5"/>')
    svg_lines.append(f'  <text x="{badge_x + (badge_width // 2)}" y="25" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600" fill="#f38ba8">✍️ {escape_xml(badge_text)}</text>')
    
    # Line number separator
    sep_x = 52
    svg_lines.append(f'  <line x1="{sep_x}" y1="{header_height}" x2="{sep_x}" y2="{total_height}" stroke="#313244" stroke-width="1"/>')
    
    # Render Code Lines
    for idx, raw_line in enumerate(lines, start=1):
        y_pos = header_height + top_margin + (idx * line_height) - 5
        
        # Line number
        svg_lines.append(f'  <text x="40" y="{y_pos}" text-anchor="end" font-size="12" fill="#585b70" font-weight="normal">{idx}</text>')
        
        # Token spans or raw text
        spans = token_spans_by_line.get(idx, [])
        if spans:
            line_svg_spans = []
            cur_col = 0
            for sp in spans:
                scol = sp['scol']
                if scol > cur_col:
                    line_svg_spans.append(escape_xml(" " * (scol - cur_col)))
                
                weight_attr = f' font-weight="{sp["weight"]}"' if sp['weight'] != 'normal' else ''
                style_attr = f' font-style="{sp["style"]}"' if sp['style'] != 'normal' else ''
                escaped_text = escape_xml(sp['text'])
                line_svg_spans.append(f'<tspan fill="{sp["color"]}"{weight_attr}{style_attr}>{escaped_text}</tspan>')
                cur_col = sp['ecol']
            
            line_content = "".join(line_svg_spans)
            svg_lines.append(f'  <text x="65" y="{y_pos}" font-size="13" xml:space="preserve">{line_content}</text>')
        else:
            escaped_raw = escape_xml(raw_line)
            svg_lines.append(f'  <text x="65" y="{y_pos}" font-size="13" fill="#cdd6f4" xml:space="preserve">{escaped_raw}</text>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def generate_gitignore_svg(filename, content):
    lines = content.strip().split("\n")
    num_lines = len(lines)
    
    line_height = 22
    header_height = 42
    top_margin = 18
    bottom_margin = 20
    total_height = header_height + top_margin + (num_lines * line_height) + bottom_margin
    total_width = 720
    
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width} {total_height}" width="100%" height="{total_height}" style="max-width: {total_width}px; border-radius: 10px; font-family: Consolas, \'Cascadia Code\', monospace;">')
    svg_lines.append(f'  <rect width="{total_width}" height="{total_height}" rx="10" fill="#1e1e2e" stroke="#313244" stroke-width="1"/>')
    svg_lines.append(f'  <path d="M 0 10 Q 0 0 10 0 L {total_width - 10} 0 Q {total_width} 0 {total_width} 10 L {total_width} {header_height} L 0 {header_height} Z" fill="#181825" stroke="#313244" stroke-width="1"/>')
    svg_lines.append(f'  <circle cx="20" cy="21" r="6" fill="#ff5f56"/>')
    svg_lines.append(f'  <circle cx="38" cy="21" r="6" fill="#ffbd2e"/>')
    svg_lines.append(f'  <circle cx="56" cy="21" r="6" fill="#27c93f"/>')
    svg_lines.append(f'  <text x="80" y="26" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#a6adc8">{escape_xml(filename)}</text>')
    
    badge_x = total_width - 195
    svg_lines.append(f'  <rect x="{badge_x}" y="10" width="180" height="22" rx="11" fill="#f38ba8" fill-opacity="0.15" stroke="#f38ba8" stroke-width="1" stroke-opacity="0.4"/>')
    svg_lines.append(f'  <text x="{badge_x + 90}" y="25" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#f38ba8">🔒 Ketik Ulang (No Copy)</text>')
    
    sep_x = 52
    svg_lines.append(f'  <line x1="{sep_x}" y1="{header_height}" x2="{sep_x}" y2="{total_height}" stroke="#313244" stroke-width="1"/>')
    
    for idx, raw_line in enumerate(lines, start=1):
        y_pos = header_height + top_margin + (idx * line_height) - 5
        svg_lines.append(f'  <text x="40" y="{y_pos}" text-anchor="end" font-size="12.5" fill="#585b70">{idx}</text>')
        
        escaped_line = escape_xml(raw_line)
        if raw_line.strip().startswith("#"):
            svg_lines.append(f'  <text x="65" y="{y_pos}" font-size="13" fill="#6c7086" font-style="italic" xml:space="preserve">{escaped_line}</text>')
        elif raw_line.strip():
            svg_lines.append(f'  <text x="65" y="{y_pos}" font-size="13" fill="#89dceb" xml:space="preserve">{escaped_line}</text>')
        else:
            svg_lines.append(f'  <text x="65" y="{y_pos}" font-size="13" fill="#cdd6f4" xml:space="preserve"></text>')
            
    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


# --- CODE DEFINITIONS ---

GITIGNORE_CODE = """# Byte-compiled / optimized / DLL files
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
venv/"""

PRAKTIKUM_1_CODE = """# ==========================================
# PRAKTIKUM 1: NESTED IF (EVALUASI KELULUSAN)
# Simpan sebagai: praktikum_01.py
# ==========================================

kehadiran = int(input("Jumlah kehadiran (1-14): "))
nilai = int(input("Nilai ujian (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai Memuaskan")
    else:
        print("REMEDIAL - Nilai Ujian Kurang")
else:
    print("TIDAK LULUS - Kehadiran Kurang dari 12")"""

PRAKTIKUM_2_CODE = """# ==========================================
# PRAKTIKUM 2: BILANGAN PRIMA & BREAK
# Simpan sebagai: praktikum_02.py
# ==========================================

def cek_prima(angka):
# Studi Kasus: Uji Bilangan Prima
angka = int(input("Masukkan angka: "))
is_prima = True  # Flag penanda

if angka < 2:
    is_prima = False
else:
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            is_prima = False  # Ditemukan pembagi selain 1 dan dirinya
            break             # Hentikan pencarian

if is_prima:
    print(f"{angka} adalah BILANGAN PRIMA")
else:
    print(f"{angka} BUKAN bilangan prima")"""

PRAKTIKUM_3_CODE = """# ==========================================
# PRAKTIKUM 3: DERET ARITMATIKA & AKUMULATOR
# Simpan sebagai: praktikum_03.py
# ==========================================

print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukkan Suku Pertama (a): "))
beda = int(input("Masukkan Beda Deret    (b): "))

# 1. IMPLEMENTASI WHILE: Validasi input jumlah suku agar harus positif (> 0)
banyak = int(input("Masukkan Banyak Suku   (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebih dari 0!")
    banyak = int(input("Silakan masukkan ulang Banyak Suku (n): "))

# 2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totalnya
suku = awal
total = 0  # Celengan Akumulator

print("\nBarisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku    # Akumulasi penjumlahan bertahap
    suku += beda     # Menyiapkan suku berikutnya

print(f"\nTotal Jumlah Seluruh Deret = {total}")"""

PRAKTIKUM_4_CODE = """# ==========================================
# PRAKTIKUM 4: NESTED LOOP & PENGOLAHAN LIST
# Simpan sebagai: praktikum_04.py
# ==========================================

for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris}x{kolom}={baris*kolom}", end="\t")
    print()  # Pindah baris

# 2. Pengenalan List Data Nilai
nilai_maba = [12, 32-35]
nilai_maba.append(95)  # Menambah data di akhir

print("Daftar Nilai :", nilai_maba)
print("Nilai Tertinggi:", max(nilai_maba)))"""

TUGAS_OPERASI3_CODE = """# ==============================================================================
# MODUL: operasi3.py
# Modul fungsi mandiri (def) dengan nilai kembalian (return)
# ==============================================================================

def tambah(a, b):
    \"\"\"Mengembalikan hasil penjumlahan a + b\"\"\"
    return a + b

def kurang(a, b):
    \"\"\"Mengembalikan hasil pengurangan a - b\"\"\"
    return a - b

def kali(a, b):
    \"\"\"Mengembalikan hasil perkalian a * b\"\"\"
    return a * b

def bagi(a, b):
    \"\"\"
    Mengembalikan hasil pembagian a / b.
    Menangani pencegahan error saat pembagi bernilai nol.
    \"\"\"
    if b == 0:
        return "Error: Pembagi tidak boleh bernilai nol!"
    return a / b

def cek_ganjil_genap(angka):
    \"\"\"
    Memeriksa sifat bilangan ganjil atau genap 
    menggunakan operator modulus (%)
    \"\"\"
    if angka % 2 == 0:
        return "GENAP"
    else:
        return "GANJIL"

def hitung_deret_aritmatika(awal, beda, n):
    \"\"\"
    Menghitung total akumulasi deret menggunakan perulangan for
    \"\"\"
    total = 0
    suku = awal
    for i in range(n):
        total += suku
        suku += beda
    return total"""

TUGAS_KALKULATOR_CODE = """# ==============================================================================
# PROGRAM UTAMA: kalkulator.py
# Aplikasi Kalkulator Konsol Bermenu Interaktif
# ==============================================================================
import operasi3  # Memanggil modul fungsi terpisah

while True:
    print("\\n" + "=" * 45)
    print("        APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. Cek Sifat Bilangan (Ganjil / Genap)")
    print("3. Hitung Deret Aritmatika (For & Akumulator)")
    print("4. Cetak Tabel Perkalian Matriks (Nested Loop)")
    print("5. Keluar")
    print("=" * 45)

    pilihan = input("Pilih menu (1-5): ")

    # ----------------------------------------------------
    # MENU 5: KELUAR PROGRAM
    # ----------------------------------------------------
    if pilihan == "5":
        print("\\nTerima kasih telah menggunakan Kalkulator Konsol. Program selesai!")
        break

    # ----------------------------------------------------
    # MENU 1: OPERASI ARITMATIKA DASAR (+, -, *, /)
    # ----------------------------------------------------
    elif pilihan == "1":
        print("\\n--- Sub-Menu Operasi Dasar ---")
        print("A. Penjumlahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian   (*)")
        print("D. Pembagian   (/)")
        
        op = input("Pilih operasi (A/B/C/D): ").upper()
        
        # Validasi pilihan operasi (Nested If)
        if op in ["A", "B", "C", "D"]:
            inp1 = input("Masukkan angka pertama : ")
            inp2 = input("Masukkan angka kedua   : ")

            # Validasi input menggunakan .isdigit() agar tidak crash
            if inp1.isdigit() and inp2.isdigit():
                a = int(inp1)
                b = int(inp2)

                if op == "A":
                    hasil = operasi3.tambah(a, b)
                    print(f"Hasil {a} + {b} = {hasil}")
                elif op == "B":
                    hasil = operasi3.kurang(a, b)
                    print(f"Hasil {a} - {b} = {hasil}")
                elif op == "C":
                    hasil = operasi3.kali(a, b)
                    print(f"Hasil {a} * {b} = {hasil}")
                elif op == "D":
                    hasil = operasi3.bagi(a, b)
                    print(f"Hasil {a} / {b} = {hasil}")
            else:
                print("Peringatan: Masukan wajib berupa bilangan bulat!")
        else:
            print("Peringatan: Pilihan operasi tidak valid!")

    # ----------------------------------------------------
    # MENU 2: CEK SIFAT BILANGAN GANJIL / GENAP
    # ----------------------------------------------------
    elif pilihan == "2":
        print("\\n--- Cek Ganjil / Genap (Modulus %) ---")
        inp_angka = input("Masukkan angka bulat positif: ")

        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = operasi3.cek_ganjil_genap(angka)
            print(f"Hasil: Angka {angka} tergolong bilangan {status}")
        else:
            print("Peringatan: Masukan harus berupa angka murni!")

    # ----------------------------------------------------
    # MENU 3: HITUNG DERET ARITMATIKA (WHILE + FOR)
    # ----------------------------------------------------
    elif pilihan == "3":
        print("\\n--- Hitung Deret Aritmatika ---")
        inp_a = input("Suku Pertama (a) : ")
        inp_b = input("Beda Deret   (b) : ")
        inp_n = input("Banyak Suku  (n) : ")

        if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit():
            a = int(inp_a)
            b = int(inp_b)
            n = int(inp_n)

            # Perulangan bersyarat while untuk memastikan n > 0
            while n <= 0:
                print("Peringatan: Banyak suku (n) harus lebih dari 0!")
                n = int(input("Masukkan ulang banyak suku (n): "))

            total_deret = operasi3.hitung_deret_aritmatika(a, b, n)
            print(f"Total Jumlah Seluruh Deret = {total_deret}")
        else:
            print("Peringatan: Seluruh masukan wajib berupa angka bulat!")

    # ----------------------------------------------------
    # MENU 4: CETAK TABEL PERKALIAN MATRIKS (NESTED LOOP)
    # ----------------------------------------------------
    elif pilihan == "4":
        print("\\n--- Matriks Tabel Perkalian 1-3 (Nested Loop) ---")
        # Loop luar mengatur perpindahan baris
        for baris in range(1, 4):
            # Loop dalam mencetak seluruh kolom sampai selesai
            for kolom in range(1, 4):
                print(f"{baris * kolom}\\t", end="")
            print()  # Pindah ke baris baru

    # ----------------------------------------------------
    # KONDISI MENU TIDAK VALID
    # ----------------------------------------------------
    else:
        print("Pilihan tidak valid! Silakan masukkan opsi 1 sampai 5.")"""


def main():
    os.makedirs("assets", exist_ok=True)
    
    files_to_generate = [
        ("assets/code_gitignore.svg", lambda: generate_gitignore_svg(".gitignore", GITIGNORE_CODE)),
        ("assets/code_praktikum_01.svg", lambda: generate_python_svg("praktikum_01.py", PRAKTIKUM_1_CODE)),
        ("assets/code_praktikum_02.svg", lambda: generate_python_svg("praktikum_02.py", PRAKTIKUM_2_CODE)),
        ("assets/code_praktikum_03.svg", lambda: generate_python_svg("praktikum_03.py", PRAKTIKUM_3_CODE)),
        ("assets/code_praktikum_04.svg", lambda: generate_python_svg("praktikum_04.py", PRAKTIKUM_4_CODE)),
        ("assets/code_operasi3_template.svg", lambda: generate_python_svg("operasi3.py", TUGAS_OPERASI3_CODE, "Tugas Mandiri 1 • Modul Fungsi")),
        ("assets/code_kalkulator_template.svg", lambda: generate_python_svg("kalkulator.py", TUGAS_KALKULATOR_CODE, "Tugas Mandiri 2 • Aplikasi Kalkulator")),
        ("assets/code_tugas3_menu_template.svg", lambda: generate_python_svg("tugas3_menu.py", TUGAS_KALKULATOR_CODE, "Tugas Mandiri 2 • Aplikasi Kalkulator")),
    ]
    
    for path, gen_fn in files_to_generate:
        svg_content = gen_fn()
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Generated: {path}")

if __name__ == "__main__":
    main()
