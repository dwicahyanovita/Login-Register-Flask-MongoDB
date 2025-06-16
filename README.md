# ⛄️🔐 Happy Login - Sistem Login & Register dengan Flask dan MongoDB

**Happy Login** adalah aplikasi web sederhana yang memungkinkan pengguna untuk melakukan **registrasi**, **login**, dan melihat **informasi akun** menggunakan **Flask** sebagai backend dan **MongoDB Compass** sebagai database.
Aplikasi ini dilengkapi dengan berbagai fitur keamanan, termasuk:

* **Validasi format email** agar sesuai dengan standar email yang benar.
* **Validasi kekuatan password**, di mana password harus memiliki **minimal 8 karakter**, mengandung **huruf besar**, **huruf kecil**, **angka**, dan **simbol**.
* **Pencegahan duplikat** dengan memastikan bahwa **email dan username tidak boleh sama** dengan yang sudah terdaftar.
* Password disimpan dalam bentuk **terenkripsi** menggunakan hashing untuk menjaga keamanan akun pengguna.

---

## 🛠️ Teknologi yang Digunakan

* Python 3
* Flask
* MongoDB (Compass)
* HTML / CSS / JS

---

## 📁 Struktur Database

* **Nama Database**: `auth_db`
* **Nama Collection**: `users`

**Contoh Dokumen:**

```json
{
  "_id": "uuid",
  "username": "unik",
  "email": "unik",
  "password": "hashed_password",
  "created_at": "ISO8601 timestamp",
  "last_login": "ISO8601 timestamp / null"
}
```

---

## 🔐 Fitur Aplikasi

### 🔐 1. Register

Pengguna baru dapat melakukan pendaftaran dengan mengisi:

* **username**
* **email**
* **password**

Saat mendaftar, sistem:

* Mengecek apakah **email/username sudah digunakan**
* Memastikan format email valid
* Memvalidasi kekuatan password:

  * Minimal **8 karakter**
  * Mengandung **huruf besar**, **huruf kecil**, **angka**, dan **simbol**
* Mengenkripsi password
* Menyimpan data ke MongoDB beserta **waktu created\_at**

---

### 🔑 2. Login

Pengguna login menggunakan:

* **Email dan password**

Saat login:

* Sistem mencocokkan email dan password (dengan verifikasi hash)
* Jika berhasil:

  * Menampilkan pesan **“Login berhasil”**
  * Menyimpan **waktu last\_login**
  * Mengarahkan ke halaman **Dashboard**

---

### 🏠 3. Dashboard (Home)

Menampilkan informasi akun pengguna yang berhasil login:
**ID**, **Username**, **Email**, **Created At**, **Last Login**

---

## Antarmuka Aplikasi

Berikut adalah tampilan halaman pada aplikasi ini:

1. **Halaman Register**

<img width="800" alt="Tangkapan Layar 2025-06-16 pukul 9 18 58 PM" src="https://github.com/user-attachments/assets/2c23e417-10b8-432f-b692-7d6244520f20" />

2. **Halaman Login**

  <img width="800" alt="Tangkapan Layar 2025-06-16 pukul 9 20 04 PM" src="https://github.com/user-attachments/assets/09409136-99db-4523-b233-5b6bf81a0f45" />

3. **Respon JSON saat Register**
   
     <img width="800" alt="Tangkapan Layar 2025-06-16 pukul 9 19 44 PM" src="https://github.com/user-attachments/assets/8a5cf090-b64c-470f-802e-061acafe7e90" />
 
4. **Halaman Dashboard (Home)**
   
   <img width="800" alt="Tangkapan Layar 2025-06-16 pukul 9 20 27 PM" src="https://github.com/user-attachments/assets/336d6d8a-4137-4dfe-abda-3333dafe30b3" />

5. **Koleksi MongoDB (users) di Compass**
<img width="800" alt="Tangkapan Layar 2025-06-16 pukul 10 18 29 PM" src="https://github.com/user-attachments/assets/20876e39-ef4c-494a-aafc-ae1a8b03d4d9" />

    

---

## 🚀 Cara Menjalankan Aplikasi

1. **Aktifkan Virtual Environment dan Install Dependency**

```bash
python3 -m venv env
source env/bin/activate  # Untuk Mac/Linux
env\Scripts\activate     # Untuk Windows

pip install flask pymongo passlib
```

2. **Pastikan MongoDB sudah berjalan**, dan nama database-nya `auth_db` dengan collection `users`.

3. **Jalankan Aplikasi:**

```bash
python app.py
```

Buka browser dan akses `http://127.0.0.1:5000`.

---
-Dwi Cahya Nov
