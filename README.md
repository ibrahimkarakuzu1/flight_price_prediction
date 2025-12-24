# # ✈️ Uçak Bileti Fiyat Tahmin Sistemi (Flight Price Prediction)

Bu proje, makine öğrenmesi teknikleri kullanılarak uçak bileti fiyatlarının tahmin edilmesi amacıyla geliştirilmiştir. Geçmiş uçuş verileri, rota bilgileri ve zamanlama faktörleri analiz edilerek, dinamik fiyatlandırma mekanizmalarını anlamaya ve gelecekteki bilet fiyatlarını öngörmeye yardımcı olur.

## 🎯 Projenin Amacı
Havayolu taşımacılığında bilet fiyatları sürekli değişkenlik gösterir. Bu proje; kalkış/varış noktası, havayolu şirketi ve uçuş zamanı gibi değişkenleri kullanarak en uygun fiyat tahminini yapmayı hedefler. Özellikle **dinamik fiyatlandırma (dynamic pricing)** stratejileri üzerine odaklanan bir ön çalışmadır.

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler
Proje **Python** dili ile geliştirilmiş olup aşağıdaki kütüphaneler kullanılmıştır:

* **Scikit-learn:** Makine öğrenmesi modeli (Linear Regression) eğitimi için.
* **Pandas:** Veri setini işlemek ve analiz etmek için.
* **NumPy:** Sayısal hesaplamalar için.
* **Pickle:** Eğitilen modelin kaydedilmesi ve tekrar yüklenmesi için.

## 📂 Proje Yapısı

```text
ml_project3/
├── app.py              # Tahminleme yapan ana uygulama dosyası
├── model.pkl           # Eğitilmiş Lineer Regresyon modeli
├── requirements.txt    # Gerekli Python kütüphaneleri
└── README.md           # Proje dokümantasyonu
