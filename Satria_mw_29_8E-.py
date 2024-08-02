import tkinter as tk

# Data soal untuk setiap kategori
soal_mtk = [
    {"soal": "Berapa hasil dari 2 + 2?", "pilihan": ["A. 3", "B. 4", "C. 5"], "jawaban": "B"},
    {"soal": "Apa rumus keliling lingkaran?", "pilihan": ["A. 2πr", "B. πr²", "C. πd"], "jawaban": "A"},
    {"soal": "Berapa hasil dari 7 x 6?", "pilihan": ["A. 42", "B. 36", "C. 48"], "jawaban": "A"},
    {"soal": "Apa hasil dari 9 ÷ 3?", "pilihan": ["A. 3", "B. 6", "C. 9"], "jawaban": "A"},
    {"soal": "Sebuah segitiga memiliki sudut 90 derajat. Apa jenis segitiganya?", "pilihan": ["A. Segitiga Sama Sisi", "B. Segitiga Sembarang", "C. Segitiga Siku-Siku"], "jawaban": "C"},
    {"soal": "Jika x = 4, berapa nilai 3x + 2?", "pilihan": ["A. 14", "B. 12", "C. 10"], "jawaban": "A"},
    {"soal": "Apa hasil dari 15 - 8?", "pilihan": ["A. 5", "B. 7", "C. 8"], "jawaban": "B"},
    {"soal": "Apa rumus volume kubus?", "pilihan": ["A. s³", "B. 6s²", "C. 4/3πr³"], "jawaban": "A"},
    {"soal": "Berapa 5²?", "pilihan": ["A. 10", "B. 25", "C. 30"], "jawaban": "B"},
    {"soal": "Jika 4a = 16, berapa nilai a?", "pilihan": ["A. 4", "B. 2", "C. 8"], "jawaban": "A"}
]

soal_ipa = [
    {"soal": "Bagian tumbuhan yang berfungsi sebagai tempat fotosintesis adalah...", "pilihan": ["A. Akar", "B. Batang", "C. Daun"], "jawaban": "C"},
    {"soal": "Peristiwa perubahan wujud dari gas menjadi cair disebut...", "pilihan": ["A. Sublimasi", "B. Kondensasi", "C. Evaporasi"], "jawaban": "B"},
    {"soal": "Apa nama proses pembuatan makanan oleh tumbuhan dengan bantuan sinar matahari?", "pilihan": ["A. Respirasai", "B. Fotosintesis", "C. Transpirasi"], "jawaban": "B"},
    {"soal": "Apa unit dasar sistem pengukuran massa dalam SI?", "pilihan": ["A. Gram", "B. Kilogram", "C. Ons"], "jawaban": "B"},
    {"soal": "Bagian tubuh manusia yang berfungsi untuk bernapas adalah...", "pilihan": ["A. Hati", "B. Paru-paru", "C. Ginjal"], "jawaban": "B"},
    {"soal": "Apa nama unsur kimia dengan simbol H?", "pilihan": ["A. Helium", "B. Hidrogen", "C. Heli"], "jawaban": "B"},
    {"soal": "Sumber energi utama bagi manusia berasal dari...", "pilihan": ["A. Matahari", "B. Batuan", "C. Air"], "jawaban": "A"},
    {"soal": "Apa nama proses perubahan wujud dari padat menjadi gas?", "pilihan": ["A. Sublimasi", "B. Kondensasi", "C. Pembekuan"], "jawaban": "A"},
    {"soal": "Bagaimana cara tanaman mengeluarkan oksigen?", "pilihan": ["A. Fotosintesis", "B. Respirasi", "C. Evaporasi"], "jawaban": "A"},
    {"soal": "Apa organ tubuh yang menyaring darah di manusia?", "pilihan": ["A. Hati", "B. Ginjal", "C. Paru-paru"], "jawaban": "B"}
]

soal_ips = [
    {"soal": "Siapa penemu benua Amerika?", "pilihan": ["A. Vasco da Gama", "B. Ferdinand Magellan", "C. Christopher Columbus"], "jawaban": "C"},
    {"soal": "Gunung tertinggi di dunia adalah...", "pilihan": ["A. Gunung Kilimanjaro", "B. Gunung Everest", "C. Gunung Fuji"], "jawaban": "B"},
    {"soal": "Apa ibu kota Indonesia?", "pilihan": ["A. Surabaya", "B. Jakarta", "C. Bandung"], "jawaban": "B"},
    {"soal": "Apa nama benua terbesar di dunia?", "pilihan": ["A. Afrika", "B. Asia", "C. Eropa"], "jawaban": "B"},
    {"soal": "Negara manakah yang memiliki jumlah penduduk terbesar di dunia?", "pilihan": ["A. India", "B. Amerika Serikat", "C. China"], "jawaban": "C"},
    {"soal": "Apa nama perjanjian yang mengakhiri Perang Dunia I?", "pilihan": ["A. Perjanjian Versailles", "B. Perjanjian Paris", "C. Perjanjian Tokyo"], "jawaban": "A"},
    {"soal": "Apa nama kerajaan kuno di Mesir?", "pilihan": ["A. Roma", "B. Yunani", "C. Mesir"], "jawaban": "C"},
    {"soal": "Siapa presiden pertama Amerika Serikat?", "pilihan": ["A. George Washington", "B. Abraham Lincoln", "C. John Adams"], "jawaban": "A"},
    {"soal": "Apa nama sungai terpanjang di dunia?", "pilihan": ["A. Amazon", "B. Nil", "C. Mississippi"], "jawaban": "B"},
    {"soal": "Apa negara yang memiliki banyak pulau?", "pilihan": ["A. Jepang", "B. India", "C. Rusia"], "jawaban": "A"}
]

soal_bindo = [
    {"soal": "Apa sinonim dari kata 'cerdas'?", "pilihan": ["A. Pintar", "B. Malas", "C. Bodoh"], "jawaban": "A"},
    {"soal": "Apa antonim dari kata 'berani'?", "pilihan": ["A. Takut", "B. Nekat", "C. Pemberani"], "jawaban": "A"},
    {"soal": "Kalimat manakah yang benar?", "pilihan": ["A. Saya suka pergi ke sekolah.", "B. Saya sukah pergi ke sekolah.", "C. Saya suka pergi ke sekolahnya."], "jawaban": "A"},
    {"soal": "Apa arti dari kata 'ramah'?", "pilihan": ["A. Sopan", "B. Kasar", "C. Bodoh"], "jawaban": "A"},
    {"soal": "Apa bentuk kata dari 'makan' dalam kalimat 'Saya sedang ____'?", "pilihan": ["A. Makan", "B. Memakan", "C. Memakanlah"], "jawaban": "A"},
    {"soal": "Apa sinonim dari kata 'senang'?", "pilihan": ["A. Gembira", "B. Sedih", "C. Marah"], "jawaban": "A"},
    {"soal": "Apa antonim dari kata 'besar'?", "pilihan": ["A. Kecil", "B. Panjang", "C. Tinggi"], "jawaban": "A"},
    {"soal": "Kalimat manakah yang benar secara tata bahasa?", "pilihan": ["A. Dia pergi ke pasar kemarin.", "B. Dia pasar ke pergi kemarin.", "C. Pasar dia pergi ke kemarin."], "jawaban": "A"},
    {"soal": "Apa arti dari kata 'belajar'?", "pilihan": ["A. Mempelajari sesuatu", "B. Beristirahat", "C. Makan"], "jawaban": "A"},
    {"soal": "Apa bentuk kata kerja dari 'tidur'?", "pilihan": ["A. Tidurlah", "B. Tiduran", "C. Tidur"], "jawaban": "C"}
]

# Fungsi untuk memulai game
def start_game():
    global current_category
    global current_question_index
    global score
    global lives
    global best_score
    global selected_category

    lives = 3
    score = 0
    current_question_index = 0
    selected_category = None

    # Menghapus semua widget dari root
    for widget in root.winfo_children():
        widget.destroy()

    # Menampilkan menu kategori
    category_menu()

def category_menu():
    global current_category

    # Menghapus semua widget dari root
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Pilih kategori soal:", font=("Helvetica", 18)).pack(pady=20)

    button_config = {
        "font": ("Helvetica", 16),
        "width": 30,
        "height": 2,
        "anchor": "center"
    }

    tk.Button(root, text="Matematika", command=lambda: set_category(soal_mtk), **button_config).pack(pady=10)
    tk.Button(root, text="IPA", command=lambda: set_category(soal_ipa), **button_config).pack(pady=10)
    tk.Button(root, text="IPS", command=lambda: set_category(soal_ips), **button_config).pack(pady=10)
    tk.Button(root, text="Bahasa Indonesia", command=lambda: set_category(soal_bindo), **button_config).pack(pady=10)

def set_category(cat):
    global questions
    global selected_category
    questions = cat
    selected_category = cat  # Menyimpan kategori yang dipilih untuk digunakan nanti
    next_question()

def next_question():
    global current_question_index
    global questions
    global lives
    global score

    # Menghapus semua widget dari root
    for widget in root.winfo_children():
        widget.destroy()

    if current_question_index >= len(questions):
        show_results()
        return

    question = questions[current_question_index]

    # Menampilkan teks soal dengan pengaturan lebar yang lebih baik
    tk.Label(root, text=question["soal"], font=("Helvetica", 16), wraplength=500, justify="left").pack(pady=20)

    button_config = {
        "font": ("Helvetica", 14),
        "width": 40,
        "height": 2,
        "anchor": "center"
    }

    for option in question["pilihan"]:
        tk.Button(root, text=option, command=lambda opt=option: answer_question(opt), **button_config).pack(pady=5)

def answer_question(option):
    global current_question_index
    global questions
    global lives
    global score
    global best_score

    question = questions[current_question_index]
    correct_answer = question["jawaban"]

    # Menghapus semua widget dari root
    for widget in root.winfo_children():
        widget.destroy()

    # Pilih bagian jawaban dari string opsi
    selected_answer = option.split(".")[0].strip()  # Pisahkan berdasarkan titik, lalu hapus spasi ekstra

    if selected_answer == correct_answer:
        score += 10
        tk.Label(root, text="Jawaban benar!", font=("Helvetica", 18)).pack(pady=20)
    else:
        lives -= 1
        tk.Label(root, text="Jawaban salah!", font=("Helvetica", 18)).pack(pady=20)
        tk.Label(root, text=f"Nyawa tersisa: {lives}", font=("Helvetica", 18)).pack(pady=10)  # Tambah jarak

    current_question_index += 1

    # Tambahkan delay sebelum melanjutkan ke pertanyaan berikutnya
    if lives > 0:
        if current_question_index < len(questions):
            root.after(2000, next_question)  # Jeda 2 detik sebelum pindah ke pertanyaan berikutnya
        else:
            root.after(2000, show_results)  # Jika pertanyaan habis, tampilkan hasil
    else:
        root.after(2000, show_results)  # Jika nyawa habis, tampilkan hasil

def show_results():
    global score
    global best_score
    global selected_category

    # Menghapus semua widget dari root
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Skor Anda: {score}", font=("Helvetica", 20)).pack(pady=20)
    if score > best_score:
        best_score = score
        tk.Label(root, text=f"Skor Terbaik Baru: {best_score}", font=("Helvetica", 20)).pack(pady=20)
    else:
        tk.Label(root, text=f"Skor Terbaik: {best_score}", font=("Helvetica", 20)).pack(pady=20)

    button_config = {
        "font": ("Helvetica", 16),
        "width": 20,
        "height": 2,
        "anchor": "center"
    }

    tk.Button(root, text="Ulangi kategori ini", command=lambda: repeat_category(selected_category), **button_config).pack(pady=10)
    tk.Button(root, text="Pilih kategori lain", command=category_menu, **button_config).pack(pady=10)
    tk.Button(root, text="Keluar", command=root.quit, **button_config).pack(pady=10)

def repeat_category(cat):
    global current_question_index
    global lives
    global score
    global questions

    questions = cat
    current_question_index = 0
    lives = 3
    score = 0
    next_question()

# Inisialisasi variabel global
current_category = None
current_question_index = 0
score = 0
lives = 3
best_score = 0
questions = []
selected_category = None

# Membuat dan menampilkan jendela utama
root = tk.Tk()
root.title("Game Teka-Teki")

# Memulai game
start_game()

root.mainloop()
