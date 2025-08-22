# 🛒 Kelontong App

Aplikasi web sederhana untuk membantu pengelolaan **stok barang, transaksi, harga beli/jual, dan expired date** di toko kelontong.  
Dibuat dengan tujuan memudahkan operasional toko sekaligus sebagai project pembelajaran dalam membangun aplikasi **fullstack (Next.js + FastAPI)**.

---

## 🚀 Features (MVP)
- 📦 **Manajemen Barang (CRUD)** → tambah, edit, hapus, lihat stok.  
- 🧾 **Catat Transaksi** → pembelian (stok masuk) & penjualan (stok keluar).  
- 📊 **Dashboard Stok** → menampilkan daftar barang + stok saat ini.  
- ⏰ **Alert** → stok minim & barang hampir kadaluarsa.  
- 💾 **Histori Harga Beli** → mencatat harga grosir untuk menentukan harga jual.  

---

## 📐 Tech Stack
**Frontend**
- [Next.js](https://nextjs.org/) – React Framework  
- [Tailwind CSS](https://tailwindcss.com/) – Styling UI  

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) – REST API  
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM  
- [SQLite](https://www.sqlite.org/) (development) → PostgreSQL (production)  

**Deployment**
- Vercel (frontend)  
- Render / Railway (backend)  

---

## 📂 Project Structure
kelontong-app/
├── backend/ # FastAPI backend
├── frontend/ # Next.js frontend
├── docs/ # Dokumentasi (ERD, UI sketsa, catatan)
├── .gitignore
└── README.md

yaml
Copy
Edit

---

## 📌 Roadmap (Tahap Pengembangan)

### ✅ Phase 1 – MVP (Core Features)
- [ ] CRUD Barang
- [ ] Input Transaksi (beli/jual)
- [ ] Dashboard Stok
- [ ] Alert Stok Minim & Expired

### 🔜 Phase 2 – Advanced
- [ ] Laporan penjualan harian/bulanan (export Excel/PDF)
- [ ] Multi-user (admin / kasir)
- [ ] Grafik tren penjualan
- [ ] Integrasi AI (prediksi stok & harga)

---

## 👨‍💻 Author
- **Raditya Mulya** – [GitHub Profile](https://github.com/Raditxt)  
Project personal untuk membantu usaha keluarga & belajar Fullstack Development + AI Engineering.