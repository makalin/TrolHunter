# TrolHunter

![TrolHunter Logo](trolhunter_logo.png)

**TrolHunter**, X (Twitter) platformunda trol hesaplarını tespit etmek ve tanımlamak için tasarlanmış, Python tabanlı bir araçtır ve özellikle Türkçe içeriğe odaklanır. Kullanıcı profillerini, tweet'leri ve davranış kalıplarını analiz ederek bir "trol puanı" atar; bu, profilinize saldıran agresif hesapları engelleyip engellememeye veya yok saymaya karar vermenize yardımcı olur.

## Özellikler
- `tweepy` aracılığıyla X API'sini kullanarak X kullanıcı verilerini (takipçiler, takip edilenler, tweet'ler, hesap yaşı) çeker.
- Tweet'ler üzerinde çok dilli BERT modeli kullanarak duygu analizi yapar.
- Trol benzeri davranışları sezgisel yöntemlerle tespit eder (örneğin, düşük takipçi/takip edilen oranı, aşırı gönderi paylaşımı).
- Özelleştirilebilir bir Türkçe trol anahtar kelime listesi içerir.
- Sonuçları kolay inceleme için CSV dosyasına çıkarır.

## Kurulum

1. **Depoyu Klonlayın**:
   ```bash
   git clone https://github.com/makalin/TrolHunter.git
   cd TrolHunter
   ```

2. **Bağımlılıkları Kurun**:
   ```bash
   pip install tweepy transformers pandas torch
   ```

3. **X API Kimlik Bilgilerini Ayarlayın**:
   - API anahtarlarınızı [developer.x.com](https://developer.x.com) adresinden alın.
   - `trolhunter.py` dosyasındaki yer tutucuları değiştirin:
     ```python
     API_KEY = "api_anahtarınız"
     API_SECRET = "api_gizliniz"
     ACCESS_TOKEN = "erişim_belirteciniz"
     ACCESS_TOKEN_SECRET = "erişim_belirteci_gizliniz"
     ```

## Kullanım

1. **Hedef Kullanıcıları Düzenleyin**:
   - `trolhunter.py` dosyasını açın ve analiz etmek istediğiniz X kullanıcı adlarını `target_users` listesine ekleyin:
     ```python
     target_users = ["kullanıcı1", "kullanıcı2", "kullanıcı3"]
     ```

2. **Betiyi Çalıştırın**:
   ```bash
   python trolhunter.py
   ```

3. **Sonuçları Kontrol Edin**:
   - Sonuçlar konsola yazdırılır ve `troll_detection_results.csv` dosyasına kaydedilir.
   - "Trol mü?" sütununa bakın: "Evet", muhtemel bir trolü gösterir.

## Örnek Çıktı
```
kullanıcı1 analiz ediliyor: Trol (Puan: 10)
kullanıcı2 analiz ediliyor: Trol Değil (Puan: 3)
kullanıcı3 analiz ediliyor: Trol (Puan: 8)
Sonuçlar troll_detection_results.csv dosyasına kaydedildi
```

## Özelleştirme
- **Trol Anahtar Kelimeler**: Betikteki `troll_keywords` listesini daha fazla Türkçe terimle genişletin:
  ```python
  troll_keywords = ["salak", "aptal", "kudur", ...]
  ```
- **Eşik Değeri**: `analyze_user` fonksiyonunda trol puanı eşiğini (varsayılan: 8) ayarlayın.
- **Model**: Duygu modeli Türkçe’ye özgü bir modelle değiştirin (örneğin, `dbmdz/bert-base-turkish-cased`).

## Sınırlamalar
- X API hesabı gerektirir (ücretsiz katman hız sınırlarına sahiptir).
- Yanlış pozitifler/negatifler olabilir; doğruluk için sezgisel yöntemleri ayarlayın.
- Duygu analizi çok dillidir ancak varsayılan olarak Türkçe için optimize edilmemiştir.

## Katkıda Bulunma
Çatallayabilir, sorun bildirebilir veya çekme istekleri gönderebilirsiniz! Geliştirme önerileri:
- Türkçe için daha gelişmiş NLP ekleyin.
- Gerçek zamanlı izleme uygulayın.
- Puanlamayı makine öğrenimi ile geliştirin.

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Teşekkürler
- [tweepy](https://github.com/tweepy/tweepy) ve [transformers](https://github.com/huggingface/transformers) ile oluşturulmuştur.
- Türkçe X trollerine karşı savunma ihtiyacıdan ilham alınmıştır.
