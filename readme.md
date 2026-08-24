# YouTube Downloader

Downloader video sederhana berbasis Python dan `yt-dlp`.

Program memilih format secara otomatis:

- Jika FFmpeg tersedia, program mengunduh video dan audio dengan kualitas terbaik lalu menggabungkannya.
- Jika FFmpeg belum tersedia, program mengunduh format terbaik yang sudah berisi video dan audio sehingga tidak terjadi error merge.

## Persyaratan

- Windows 10 atau Windows 11
- Python 3.9 atau lebih baru
- Koneksi internet
- FFmpeg, direkomendasikan untuk kualitas terbaik

## Instalasi

Buka PowerShell di folder project, lalu jalankan:

```powershell
python -m pip install -U yt-dlp
```

Pasang FFmpeg menggunakan WinGet:

```powershell
winget install --id Gyan.FFmpeg --exact --source winget
```

Jika WinGet menyatakan paket sudah terpasang tetapi perintah `ffmpeg` belum dikenali, tutup seluruh VS Code melalui **File > Exit**, kemudian buka kembali VS Code dan terminal baru.

Verifikasi instalasi:

```powershell
ffmpeg -version
python -c "import yt_dlp, shutil; print('yt-dlp: OK'); print('ffmpeg:', shutil.which('ffmpeg') or 'tidak ditemukan')"
```

Jika terminal lama masih memakai PATH sebelumnya, muat ulang PATH secara manual:

```powershell
$env:Path = [Environment]::GetEnvironmentVariable("Path", "User") + ";" + [Environment]::GetEnvironmentVariable("Path", "Machine")
ffmpeg -version
```

## Menjalankan Program

Jalankan dari folder project:

```powershell
python main.py
```

Masukkan URL video ketika diminta. File hasil download disimpan di folder project saat ini, sesuai aturan nama file dari `yt-dlp`.

## Troubleshooting

### `ffmpeg is not installed`

Pastikan `ffmpeg -version` berhasil di terminal yang sama dengan terminal untuk menjalankan Python. Jika belum berhasil:

1. Jalankan kembali perintah instalasi WinGet di atas.
2. Tutup dan buka ulang VS Code agar PATH diperbarui.
3. Jalankan verifikasi `ffmpeg -version`.

Program tetap dapat mengunduh tanpa FFmpeg menggunakan satu format gabungan, tetapi kualitas maksimal dan penggabungan audio/video memerlukan FFmpeg.

### `No module named yt_dlp`

Instal dependency dengan interpreter Python yang digunakan untuk menjalankan program:

```powershell
python -m pip install -U yt-dlp
```

### URL tidak dapat diunduh

Perbarui `yt-dlp`, pastikan URL valid, dan periksa koneksi internet:

```powershell
python -m pip install -U yt-dlp
```

## Catatan Penggunaan

Gunakan program hanya untuk konten yang boleh Anda unduh dan sesuai dengan ketentuan layanan platform serta hukum yang berlaku.
