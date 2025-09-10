# 🏪 Toko Kelontong App

Aplikasi web sederhana untuk membantu pengelolaan toko kelontong. Fokus utama: mencatat transaksi, memantau stok barang, dan menampilkan ringkasan omzet dalam bentuk dashboard yang mudah dipahami.

## 🚀 Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (pakai SQLAlchemy + Alembic untuk migrasi)
- **Frontend**: React + Tailwind CSS
- **Deployment**: (Planned) Docker + Cloud Hosting (Railway, Render, Supabase, dsb.)

## 📂 Struktur Proyek

```
toko-kelontong-app/
├── backend/
│   ├── app/
│   │   ├── main.py          # Entry point FastAPI
│   │   ├── models.py        # Database models
│   │   ├── schemas.py       # Pydantic schemas
│   │   ├── database.py      # DB connection
│   │   └── routers/         # API routes (products, transactions, dashboard)
│   └── requirements.txt     # Backend dependencies
│
├── frontend/
│   ├── src/                 # React source code
│   ├── public/              # Public assets for React
│   └── package.json         # Frontend dependencies
│
├── docker-compose.yml       # (Optional, planned for local containerization)
└── README.md                # Dokumentasi proyek ini
```

## ⚙️ Setup Development

Untuk menjalankan aplikasi ini secara lokal, ikuti langkah-langkah berikut:

### 1. Clone Repository

```bash
git clone <URL_REPO_ANDA>
cd toko-kelontong-app
```

> **Catatan**: Ganti `<URL_REPO_ANDA>` dengan URL repository GitHub atau Git Anda.

### 2. Backend (FastAPI)

**Prerequisites**: Pastikan Anda memiliki Python dan pip terinstal.

```bash
# Masuk ke direktori backend
cd backend

# Buat dan aktifkan virtual environment
python -m venv venv

# Untuk Mac/Linux
source venv/bin/activate
# Untuk Windows
venv\Scripts\activate

# Instal semua dependensi
pip install -r requirements.txt

# Jalankan server FastAPI
uvicorn app.main:app --reload
```

✅ **Server backend akan berjalan di**: `http://127.0.0.1:8000`

📚 **API Documentation**: Akses dokumentasi API interaktif (Swagger UI) di `http://127.0.0.1:8000/docs`

### 3. Frontend (React + Tailwind)

**Prerequisites**: Pastikan Anda memiliki Node.js dan npm terinstal.

```bash
# Pindah ke direktori frontend
cd ../frontend  # Jika Anda masih di direktori backend
# atau
cd frontend     # Jika Anda di root direktori proyek

# Instal semua dependensi
npm install

# Jalankan aplikasi React
npm start
```

✅ **Aplikasi frontend akan berjalan di**: `http://localhost:3000`

## 📊 Fitur (Planned)

Berikut adalah beberapa fitur utama yang akan dikembangkan:

### 📈 Dashboard & Reporting
- **Dashboard omzet** harian & bulanan yang mudah dipahami (untuk orang tua)
- **Laporan transaksi** harian & bulanan
- **Export Laporan** ke format CSV / PDF

### 📦 Manajemen Inventory  
- **Manajemen Stok** (tambah, edit, hapus barang) dengan detail harga beli, harga jual, dan stok awal
- **Notifikasi** untuk barang yang stoknya hampir habis atau kadaluarsa

### 💰 Transaksi & Penjualan
- **Pencatatan Transaksi** (penjualan/pembelian) yang tercatat otomatis

### 📊 Analisis Bisnis
- **Analisis Bisnis** (barang fast-moving, slow-moving, profit bulanan)

## 👥 Catatan

- Proyek ini masih dalam **tahap awal** (planning & setup) dan akan terus dikembangkan secara bertahap
- Tujuan utamanya adalah menyediakan solusi inventory yang **scalable** dan **maintainable** untuk kebutuhan monitoring toko kelontong keluarga

## 🤝 Kontribusi

Sangat terbuka untuk kontribusi! Jika Anda tertarik untuk membantu pengembangan, silakan:

1. **Fork** repository ini
2. **Buat branch baru**: `git checkout -b feature/nama-fitur-anda`
3. **Lakukan perubahan** dan commit: `git commit -m 'feat: menambahkan fitur baru'`
4. **Push ke branch** Anda: `git push origin feature/nama-fitur-anda`
5. **Buat Pull Request**

## 📄 Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT**.