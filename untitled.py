import time
from selenium import webdriver

# Fungsi untuk mengirim pesan ke nomor WhatsApp tertentu
def send_message(message):
    # Ganti 'no_tujuan' dengan nomor WhatsApp penerima
    driver.get("https://api.whatsapp.com/send?phone=6288238113438&text=" + message)
    time.sleep(5) # Tunggu 5 detik untuk memastikan halaman terbuka
    driver.find_element_by_id("action-button").click()
    time.sleep(2) # Tunggu 2 detik untuk memastikan tombol "Lanjutkan ke WhatsApp" terklik
    driver.find_element_by_css_selector("._1U1xa").click() # Klik tombol "Lanjutkan ke WhatsApp"
    time.sleep(2) # Tunggu 2 detik untuk memastikan halaman terbuka
    driver.find_element_by_css_selector("._2S1VP").send_keys(Keys.ENTER) # Klik tombol "Kirim"

# Inisialisasi driver Selenium
driver = webdriver.Chrome()

# Ganti 'pesan' dengan pesan yang ingin Anda kirimkan
pesan = "Halo, ini adalah pesan otomatis dari Project Bot Wa!"

# Ganti 'no_tujuan' dengan nomor WhatsApp penerima
no_tujuan = "6288238113438"

# Ganti 'interval' dengan waktu antara setiap pengiriman pesan (dalam detik)
interval = 10

# Loop utama program
while True:
    send_message(pesan)
    time.sleep(interval)
