# MAC_VIEW_PY

macOS sistem kaynaklarını (CPU, RAM, Disk, Ağ ve Sensörler) anlık olarak takip edebileceğiniz, FastAPI tabanlı modern ve karanlık temalı bir web dashboard uygulamasıdır.

## 🚀 Özellikler

* **Gerçek Zamanlı Takip:** Sistem verileri her 2 saniyede bir otomatik olarak yenilenir.
* **Sistem Kaynakları:** CPU, RAM ve Disk kullanımı görsel ilerleme çubukları ile sunulur.
* **Ağ İzleme:** Toplam gönderilen ve alınan veri miktarını (MB cinsinden) gösterir.
* **Aktif Süre (Uptime):** Sistemin ne kadar süredir açık olduğunu hesaplar.
* **Süreç Yönetimi:** En yüksek CPU kullanan ilk 10 işlemi listeler.
* **Donanım Sensörleri:** macOS cihazlardaki (özellikle Intel modelleri) sıcaklık, fan hızı ve batarya durumunu izler.
* **Modern Arayüz:** Tailwind CSS kullanılarak oluşturulmuş, minimalist ve karanlık mod odaklı tasarım.

## 🛠️ Kurulum

1.  **Gereksinimler:**
    * Python 3.8+

2.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı Çalıştırın:**
    ```bash
    python app.py
    ```

4.  **Erişim:**
    Tarayıcınızdan `http://127.0.0.1:8000` adresine giderek dashboard'u görüntüleyebilirsiniz.

## 📦 Bağımlılıklar

* **FastAPI:** Web framework
* **psutil:** Sistem ve donanım bilgilerine erişim
* **Jinja2:** HTML şablon motoru
* **Uvicorn:** ASGI sunucusu