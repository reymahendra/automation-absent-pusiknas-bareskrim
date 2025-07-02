# 📝 Auto-Fill Daily Activity MTJ

Aplikasi desktop berbasis Python dan `customtkinter` untuk mengisi otomatis **Google Form** laporan kegiatan harian shift (Pagi/Malam) menggunakan **Selenium WebDriver**.

## 📦 Fitur

- GUI modern menggunakan `customtkinter`
- Input tanggal massal (multi tanggal dengan koma)
- Pilihan shift: **Pagi** atau **Malam**
- Auto-fill form Google secara otomatis menggunakan browser Microsoft Edge
- Log aktivitas pengisian langsung di aplikasi
- Tombol untuk **menutup browser otomatis**

## 🔧 Instalasi

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Requirements

- Python 3.8+
- Microsoft Edge terinstall
- Edge WebDriver terpasang (pastikan versinya sesuai dengan Microsoft Edge)
  [Download WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## ▶️ Menjalankan Aplikasi

```bash
python DailyAct_MTJ.py
```

## 📁 requirements.txt

```
customtkinter
selenium
```
