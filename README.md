# Instagram Tools & PDF Converter

Proyek ini menyediakan alat sederhana namun powerful untuk mengelola konten media sosial dan dokumen Anda.

## Fitur Unggulan

### 1. Smart Instagram Poster (`post_instagram.py`)
Tools ini tidak hanya memposting gambar ke Instagram, tetapi juga **mempercantik tampilan postingan Anda secara otomatis**.

*   **Smart Frame (Bingkai Cerdas)**: Otomatis mengubah ukuran gambar apa pun menjadi rasio 4:5 (rasio terbaik untuk Instagram) tanpa memotong gambar asli. Bagian kosong akan diisi dengan efek blur yang estetis.
*   **Watermark Otomatis**: Tambahkan teks watermark (seperti username atau brand Anda) ke setiap postingan untuk melindungi hak cipta dan meningkatkan branding.
*   **Aman & Stabil**: Menggunakan library `instagrapi` yang lebih stabil dibandingkan versi lama.

### 2. PDF to Word Converter (`pdf_to_docx.py`)
Konversi file PDF menjadi dokumen Word (.docx) yang dapat diedit dengan mudah.
*   **Akurat**: Mengekstrak teks dari setiap halaman PDF.
*   **Rapi**: Menyusun setiap halaman PDF menjadi halaman terpisah di Word.

## Instalasi

Pastikan Anda sudah menginstal Python. Kemudian, install library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

Isi dari `requirements.txt`:
*   `instagrapi`
*   `pillow`
*   `python-docx`
*   `pypdf`

## Cara Penggunaan

### 1. Posting ke Instagram

Gunakan script `post_instagram.py` melalui terminal/command prompt.

**Format Perintah:**
```bash
python post_instagram.py -u "USERNAME" -p "PASSWORD" -i "path/ke/gambar.jpg" -c "Caption Anda" --watermark "@username_anda"
```

**Contoh:**
```bash
python post_instagram.py -u "myuser" -p "mypassword123" -i "foto_liburan.jpg" -c "Liburan seru! #holiday" --watermark "@myuser_official"
```

**Mode Percobaan (Dry Run):**
Ingin melihat hasil edit gambar sebelum diposting? Gunakan `--dry-run`.
```bash
python post_instagram.py -i "foto.jpg" --watermark "Test Watermark" --dry-run
```
Hasil gambar yang sudah diedit akan disimpan sebagai `processed_image.jpg`.

### 2. Konversi PDF ke Word

Gunakan script `pdf_to_docx.py`.

**Format Perintah:**
```bash
python pdf_to_docx.py -i "input.pdf" -o "output.docx"
```

**Contoh:**
```bash
python pdf_to_docx.py -i "laporan.pdf" -o "laporan_edit.docx"
```

## Catatan
File lama (`instagrampost.py` dan `Convert_pdf_to_docx.ipynb`) telah disimpan sebagai file legacy (`legacy_...`) jika Anda masih membutuhkannya. Disarankan untuk menggunakan script baru yang lebih optimal.

---
*Dibuat dengan ❤️ untuk mempermudah produktivitas Anda.*
