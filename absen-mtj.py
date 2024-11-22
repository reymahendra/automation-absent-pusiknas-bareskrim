from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSed0VeJM8JWy_cXq6RUeU1X-iWFJWkV8FEx2xi8XVcv1scCQA/viewform'


# Initialize WebDriver
driver = webdriver.Edge()
### JAM ###
tanggal_list = ["27-10-2024", "29-10-2024", "03-11-2024", "17-11-2024"]
kondisi = "Malam"

if kondisi == "Pagi":
    default_waktu_masuk = "08"
    default_waktu_pulang = "20"
    default_activity = "(PAGI)\n• Dokumentasi Pergantian shift\n• Mempelajari Bahasa Pemrograman Python/Java/PHP\n• Mempelajari Framework React & Laravel\n• Membuat Laporan Monitoring Server\n• Membuat Laporan Kegiatan Harian Perangkat Utama\n• Membuat Laporan Kegiatan Harian Integrasi\n• Membuat Berita Acara Visualisasi Informasi\n• Membuat Laporan Penarikan Data Piknas\n• Membuat Laporan monitoring harian (Pagi)\n• Melakukan Penarikan Laporan Shift rentan waktu 12 jam\n"
else :
    default_waktu_masuk = "20"
    default_waktu_pulang = "08"
    default_activity = "(MALAM)\n• Melakukan Penarikan Data Masuk\n• Melakukan Penarikan Laporan Shift rentan waktu 24 jam\n• Membuat Laporan Berita Acara Pemeriksaan integrasi (SPPT-TI & NON SPPT-TI)\n• Membuat Laporan Kegiatan Harian Perawatan Data (SPPT-TI & NON SPPT-TI)\n• Membuat Laporan Berita Acara Pemeriksaan data\n• Membuat Laporan Laporan monitoring harian\n• Mempelajari Bahasa Pemrograman Python/Java/PHP\n• Menulis Mutasi Laporan Di buku Mutasi\n• Mempelajari Framework React & Laravel\n• Dokumentasi Pergantian Shift\n"
### JAM ###

default_email = "reymahndra@gmail.com"
default_nama = "Raehan Putra M"
default_waktu_masuk    # Set default time for masuk
default_waktu_pulang   # Set default time for pulang
default_waktu_akhir = "00"
default_job_title = "IT Support"  # Set default job title
default_activity  # Set default activity
default_ordered_by = ""  # Set default value for "ORDERED BY"
default_pencapaian = ""  # Set default value for PENCAPAIAN PER HARI
default_note = ""  # Set default value for NOTE
default_lokasi_kerja = ""  # Set default value for LOKASI KERJA
default_durasi_lembur = ""  # Set default value for TOTAL DURASI LEMBUR JAM

for default_tanggal in tanggal_list:
    # Open a new tab
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])  # Switch to new tab
    driver.get(form_url)

    try:
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input'))
        )
        email_input.send_keys(default_email)

        # Tanggal
        tanggal_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'))
        )
        tanggal_input.send_keys(default_tanggal)

        # Waktu Masuk
        waktu_masuk_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'))
        )
        waktu_masuk_input.send_keys(default_waktu_masuk)

        waktu_akhir_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input'))
        )
        waktu_akhir_input.send_keys(default_waktu_akhir)


        # Waktu Pulang
        waktu_pulang_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'))
        )
        waktu_pulang_input.send_keys(default_waktu_pulang)

        waktu_akhir_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input'))
        )
        waktu_akhir_input.send_keys(default_waktu_akhir)

         # Mengklik dropdown untuk memilih nama
        dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]/span'))  # Ganti dengan XPath untuk dropdown
        )
        dropdown.click()

        # Tunggu dan pilih nama dari dropdown
        nama_options = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[20]/span'))  # Ganti dengan XPath untuk nama
        )

        # Mencari dan mengklik nama yang sesuai
        nama_pilih = next((option for option in nama_options if default_nama in option.text), None)

        if nama_pilih:
            nama_pilih.click()
        else:
            print("Nama default tidak ditemukan.")

        # Pilih Job Title
        job_title_checkboxes = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]'))
        )

        # Debug: Print semua job title yang ditemukan
        for checkbox in job_title_checkboxes:
            print(checkbox.text)

        job_title_pilih = next((checkbox for checkbox in job_title_checkboxes if default_job_title in checkbox.text), None)

        if job_title_pilih:
            driver.execute_script("arguments[0].scrollIntoView(true);", job_title_pilih)
            time.sleep(0.5)  # Menambahkan delay sebelum mengklik
            ActionChains(driver).move_to_element(job_title_pilih).click().perform()
        else:
            print("Job title default tidak ditemukan.")

        # Masukkan Activity
        activity_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea'))
        )
        activity_input.send_keys(default_activity)

        # Masukkan field "ORDERED BY"
        ordered_by_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'))  # Gantilah dengan XPath yang sesuai
        )
        ordered_by_input.send_keys(default_ordered_by)

        # Pilih Checkbox "PENCAPAIAN PER HARI"
        pencapaian_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label/div'))  # Gantilah dengan XPath yang sesuai
        )
        if not pencapaian_checkbox.is_selected():
            pencapaian_checkbox.click()

        # Masukkan field "NOTE"
        note_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input'))  # Gantilah dengan XPath yang sesuai
        )
        note_input.send_keys(default_note)

        # Pilih Checkbox "LOKASI KERJA"
        lokasi_kerja_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label/div'))  # Gantilah dengan XPath yang sesuai
        )
        if not lokasi_kerja_checkbox.is_selected():
            lokasi_kerja_checkbox.click()

        # Masukkan field "TOTAL DURASI LEMBUR JAM"
        durasi_lembur_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]/textarea'))  # Gantilah dengan XPath yang sesuai
        )
        durasi_lembur_input.send_keys(default_durasi_lembur)

        # Tunggu hingga formulir selesai
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/button'))
        )

        input_data = {
            'email': default_email,
            'nama': default_nama,
            'tanggal': default_tanggal,
            'waktu_masuk': default_waktu_masuk,
            'waktu_pulang': default_waktu_pulang,
            'job_title': default_job_title,
            'activity': default_activity,
            'ordered_by': default_ordered_by,
            'pencapaian': default_pencapaian,
            'note': default_note,
            'lokasi_kerja': default_lokasi_kerja,
            'durasi_lembur': default_durasi_lembur
        }

        print("Data yang dimasukkan:")
        print(f"Email: {input_data['email']}")
        print(f"Nama: {input_data['nama']}")
        print(f"Tanggal: {input_data['tanggal']}")
        print(f"Waktu Masuk: {input_data['waktu_masuk']}")
        print(f"Waktu Pulang: {input_data['waktu_pulang']}")
        print(f"Job Title: {input_data['job_title']}")
        print(f"Activity: {input_data['activity']}")
        print(f"Ordered By: {input_data['ordered_by']}")
        print(f"Pencapaian: {input_data['pencapaian']}")
        print(f"Note: {input_data['note']}")
        print(f"Lokasi Kerja: {input_data['lokasi_kerja']}")
        print(f"Total Durasi Lembur Jam: {input_data['durasi_lembur']}")

        time.sleep(2)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Tunggu hingga pengguna menekan Enter untuk menutup browser
input("Tekan Enter untuk menutup browser...")
driver.quit()
