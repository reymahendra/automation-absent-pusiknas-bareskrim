import customtkinter as ctk
import threading
from tkinter import messagebox
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FormApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        

        self.title("Auto-Fill Daily Activity MTJ")
        self.geometry("800x750")

        self.label = ctk.CTkLabel(
            self,
            text="Daily Activity MTJ",
            font=("Arial", 45, "bold"),  # Ukuran & jenis huruf
            text_color="white",          # Warna teks
            )
        self.label.pack(pady=(25, 5))
        self.label_tanggal = ctk.CTkLabel(self, text="Masukan Tanggal (DD-MM-YYYY, pisahkan koma)")
        self.label_tanggal.pack(pady=(20, 5))
        self.entry_tanggal = ctk.CTkEntry(self, width=500)
        self.entry_tanggal.pack()

        # Input Email
        self.label_email = ctk.CTkLabel(self, text="Email")
        self.label_email.pack(pady=(10, 5))
        self.email_var = ctk.StringVar(value="reymahndra@gmail.com")
        self.entry_email = ctk.CTkEntry(self, textvariable=self.email_var, width=500)
        self.entry_email.pack()

        # Pilih Nama
        self.label_nama = ctk.CTkLabel(self, text="")
        self.label_nama.pack(pady=(5, 5))
        self.nama_var = ctk.StringVar(value="Raehan Putra M")
        self.option_nama = ctk.CTkOptionMenu(self, values=["Raehan Putra M"], variable=self.nama_var)
        self.option_nama.pack()
        

        # 2. Tambahkan ini saat membuat OptionMenu shift
        self.label_shift = ctk.CTkLabel(self, text="")
        self.label_shift.pack(pady=(5, 5))
        self.shift_var = ctk.StringVar(value="Pilih Shift")
        self.option_shift = ctk.CTkOptionMenu(
        self, values=["Pagi", "Malam"],
        variable=self.shift_var,
        command=self.update_daily_text  # ← trigger ketika shift diganti
        )
        self.option_shift.pack()

        # Input Daily
        self.label_daily = ctk.CTkLabel(self, text="")
        self.label_daily.pack(pady=(5, 5))
        self.textbox_daily = ctk.CTkTextbox(self, width=500, height=100)
        self.textbox_daily.insert("0.0", "Masukkan aktivitas harian di sini...")
        self.textbox_daily.pack()

        #Button Jalankan
        self.btn_jalankan = ctk.CTkButton(self, text="Jalankan", command=self.jalankan_otomasi)
        self.btn_jalankan.pack(pady=10)

        #Button Tutup Browser
        self.btn_tutup_browser = ctk.CTkButton(self, text="Tutup Browser", command=self.tutup_browser)
        self.btn_tutup_browser.pack(pady=10)

        self.text_log = ctk.CTkTextbox(self, height=300)
        self.text_log.pack(padx=10, pady=10, fill="both", expand=True)

        self.driver = None

    def log(self, message):
        self.text_log.insert("end", message + "\n")
        self.text_log.see("end")

    def jalankan_otomasi(self):
        tanggal_input = self.entry_tanggal.get()
        shift_input = self.shift_var.get()

        if not tanggal_input:
            messagebox.showerror("Error", "Daftar tanggal tidak boleh kosong.")
            return

        try:
            tanggal_list = [datetime.strptime(t.strip(), "%d-%m-%Y").strftime("%d-%m-%Y") for t in tanggal_input.split(',')]
        except ValueError:
            messagebox.showerror("Format Salah", "Pastikan semua tanggal berformat DD-MM-YYYY.")
            return

        threading.Thread(target=self.run_selenium, args=(tanggal_list, shift_input), daemon=True).start()
    
    def update_daily_text(self, value):
        if value == "Pagi":
            default_daily = """(PAGI)
    • Dokumentasi Pergantian shift
    • Mempelajari Bahasa Pemrograman Python/Java/PHP
    • Mempelajari Framework React & Laravel
    • Membuat Laporan Monitoring Server
    • Membuat Laporan Kegiatan Harian Perangkat Utama
    • Membuat Laporan Kegiatan Harian Integrasi
    • Membuat Berita Acara Visualisasi Informasi
    • Membuat Laporan Penarikan Data Piknas
    • Membuat Laporan monitoring harian (Pagi)
    • Melakukan Penarikan Laporan Shift rentan waktu 12 jam"""
        else:
            default_daily = """(MALAM)
    • Melakukan Penarikan Data Masuk
    • Melakukan Penarikan Laporan Shift rentan waktu 24 jam
    • Membuat Laporan Berita Acara Pemeriksaan integrasi (SPPT-TI & NON SPPT-TI)
    • Membuat Laporan Kegiatan Harian Perawatan Data (SPPT-TI & NON SPPT-TI)
    • Membuat Laporan Berita Acara Pemeriksaan data
    • Membuat Laporan Laporan monitoring harian
    • Mempelajari Bahasa Pemrograman Python/Java/PHP
    • Menulis Mutasi Laporan Di buku Mutasi
    • Mempelajari Framework React & Laravel
    • Dokumentasi Pergantian Shift"""

        # Bersihkan dan isi ulang textbox
        self.textbox_daily.delete("0.0", "end")
        self.textbox_daily.insert("0.0", default_daily)

    def run_selenium(self, tanggal_list, shift_input):
        self.log("Memulai WebDriver...")

        try:
            self.driver = webdriver.Edge()
        except Exception as e:
            self.log(f"Gagal membuka Edge: {e}")
            return

        driver = self.driver

        form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSed0VeJM8JWy_cXq6RUeU1X-iWFJWkV8FEx2xi8XVcv1scCQA/viewform'

        default_email = self.email_var.get()
        default_nama = self.nama_var.get()
        default_waktu_akhir = "00"
        default_job_title = "IT Support"
        default_ordered_by = ""
        default_pencapaian = ""
        default_note = ""
        default_lokasi_kerja = ""
        default_durasi_lembur = ""
        default_waktu_masuk = "08"
        default_waktu_pulang = "20"
        default_activity = self.textbox_daily.get("0.0", "end").strip()

        if shift_input == "Pagi":
            default_waktu_masuk = "08"
            default_waktu_pulang = "20"
        else:
            default_waktu_masuk = "20"
            default_waktu_pulang = "08"
        
        for default_tanggal in tanggal_list:
            try:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(form_url)

                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input'))).send_keys(default_email)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'))).send_keys(default_tanggal)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'))).send_keys(default_waktu_masuk)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input'))).send_keys(default_waktu_akhir)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'))).send_keys(default_waktu_pulang)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input'))).send_keys(default_waktu_akhir)

                # Mengklik dropdown untuk memilih nama
                dropdown = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]/span'))
                )
                dropdown.click()

                nama_options = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[20]/span'))
                )

                nama_pilih = next((option for option in nama_options if default_nama in option.text), None)
                if nama_pilih:
                    nama_pilih.click()
                else:
                    print("Nama default tidak ditemukan.")

                #Pilih Job
                job_title_checkboxes = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]'))
                )

                for checkbox in job_title_checkboxes:
                    print(checkbox.text)

                job_title_pilih = next((checkbox for checkbox in job_title_checkboxes if default_job_title in checkbox.text), None)
                if job_title_pilih:
                    driver.execute_script("arguments[0].scrollIntoView(true);", job_title_pilih)
                    time.sleep(0.5)
                    ActionChains(driver).move_to_element(job_title_pilih).click().perform()
                else:
                    print("Job title default tidak ditemukan.")

                lokasi_kerja_checkbox = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label/div'))
                )
                if not lokasi_kerja_checkbox.is_selected():
                    lokasi_kerja_checkbox.click()
                
                pencapaian_checkbox = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label/div'))
                )
                if not pencapaian_checkbox.is_selected():
                    pencapaian_checkbox.click()

                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea'))).send_keys(default_activity)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(default_ordered_by)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(default_note)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]/textarea'))).send_keys(default_durasi_lembur)

                self.log(f"Berhasil mengisi form untuk {default_tanggal}")
                time.sleep(2)

            except Exception as e:
                self.log(f"Gagal mengisi form untuk {default_tanggal}: {e}")

        self.log("Selesai. Tutup browser secara manual jika diperlukan.")

    def tutup_browser(self):
        if self.driver:
            self.driver.quit()
            self.log("Browser telah ditutup.")
        else:
            self.log("Browser belum dijalankan.")

if __name__ == "__main__":
    app = FormApp()
    app.mainloop()
