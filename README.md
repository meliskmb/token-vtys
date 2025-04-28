# token-vtys
# JWT Tabanlı Giriş / Kayıt Uygulaması (Flask + HTML + JS)

Bu proje, Python Flask kullanarak geliştirilen, JWT (JSON Web Token) tabanlı kimlik doğrulama sistemine sahip küçük bir tam yıkın (full-stack) uygulamadır.

## 🌍 Proje Özellikleri

- Kullanıcılar kayıt olabilir.
- Kullanıcılar email ve şifre ile giriş yapabilir.
- Giriş başarılı olursa JWT token alınır ve localStorage'da saklanır.
- Korumalı sayfaya sadece geçerli JWT token ile erişilebilir.
- Şifreler veritabanına hash'lenerek kaydedilir (bcrypt kullanılarak).
- Token süresi 60 saniyedir (1 dakika).
- Sunucu tarafında CORS izinleri doğru bir şekilde ayarlanmıştır.

## 🛠 Kullanılan Teknolojiler

- *Backend:* Flask, Flask SQLAlchemy, Flask CORS, bcrypt, PyJWT
- *Veritabanı:* SQLite
- *Frontend:* HTML, Vanilla JavaScript

## 🔧 Kurulum Talimatları

### 1. Gerekli Paketleri Yükleme

```bash
pip install flask flask_sqlalchemy flask_cors bcrypt pyjwt 


### 2. config.py Ayarı

config.py dosyasındaki SECRET_KEY sabit olmalıdır. Örnek:

python
class Config:
    SECRET_KEY = 'gizli-anahtariniz'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


### 3. Sunucuyu Başlatma

```bash
python app.py
```

Sunucu açıldığında:


 * Running on http://127.0.0.1:5000/


gibi bir çıktı görmelisiniz.

### 4. Frontend Dosyalarını Açma

- register.html dosyasını tarayıcıda açın.
- Kayıt olun, ardından login.html ile giriş yapın.
- Giriş yaptıktan sonra protected.html sayfasına yönleneceksiniz.

## ⚠ Dikkat Edilmesi Gerekenler

- Flask sunucusunun çalışıyor olması gerekir.
- Token süresi sadece 1 dakika olduğu için uzun süre işlem yapmazsanız yeniden giriş yapmanız gerekir.
- Tarayıcıda sorun yaşarsanız `localStorage`ı temizleyip yeniden deneyin.

## Projede Öğrenilenler

- Flask ile API endpoint'leri olu- Flask ile API endpoint'leri olu\u015turmak
- JWT ile oturum yönetimi yapmak
- Şifre hash'leme (bcrypt) ile güvenli kayıt işlemleri
- localStorage kullanarak tarayıcıda token saklamak
- Frontend - Backend arasında iletişim sağlamak
- CORS sorunlarını çözmek

## Projeyi Başlatma Adımları

```bash
# Proje klasörüne geç
cd /JWT-login-project

# (Eğer sanal ortam kullanıyorsan)
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Sunucuyu çalıştır
python app.py
```

Ardından register.html, login.html, protected.html dosyalarını tarayıcıdan açarak projeyi test edebilirsiniz.

## 👩‍💻 Hazırlayan
- Mihriban Melis Kömbe
-Sema Hacıbekiroğlu
-Zeynep Merve Koyuncu
> Bu proje, tam yıkın web geliştirme mantığını küçük ve öğretici bir örnekle öğrenmek amacıyla adım adım hazırlanmıştır.
