# Devscale Assignment - FastAPI dengan LLM

Repositori ini adalah tugas dari bootcamp **Devscale Indonesia**. Aplikasi ini merupakan sebuah web API sederhana berbasis **FastAPI** yang mengintegrasikan pemanggilan Large Language Model (LLM) dari OpenAI.

## Fitur Utama

Sesuai dengan kriteria tugas, aplikasi ini telah mengimplementasikan:
- **FastAPI Single Endpoint**: Memiliki satu endpoint utama (`/chat`) menggunakan metode `POST` untuk memproses interaksi dengan LLM.
- **LLM Call**: Terintegrasi dengan OpenAI API (model `gpt-4o-mini`) untuk memproses input teks dari user dan mengembalikan respons yang relevan.
- **Pydantic Models**: Validasi data secara ketat menggunakan Pydantic untuk Request Body (`MessageInput`) dan Response Body (`Chat`).
- **Scalar FastAPI**: Menggunakan **Scalar UI** sebagai dokumentasi API interaktif yang cantik dan modern (menggantikan atau melengkapi Swagger UI standar).

## Struktur Proyek

```text
belajar-fastapi/
├── .env                  # Environment variables (OpenAI API Key)
├── app/
│   ├── main.py           # Entry point aplikasi (Inisialisasi FastAPI & Scalar)
│   ├── router.py         # Definisi routing endpoint (POST /chat)
│   ├── schema.py         # Pydantic models untuk request & response
│   ├── services.py       # Logika bisnis dan pemanggilan ke OpenAI API
│   ├── prompts.py        # System prompt untuk mengatur behavior LLM
│   └── settings.py       # Pengelolaan konfigurasi / environment variable
├── pyproject.toml        # Konfigurasi dependensi project
├── uv.lock               # Lockfile untuk uv
└── README.md
```

## Persyaratan & Instalasi

Proyek ini dikelola menggunakan package manager modern (`uv`).

### 1. Clone Repositori

```bash
git clone <url-repo-anda>
cd belajar-fastapi
```

### 2. Setup Environment Variables

Duplikat atau copy file `.env.example` (jika ada) menjadi `.env`, lalu masukkan OpenAI API Key Anda.

```bash
cp .env.example .env
```
Isi `.env` dengan:
```env
OPENAI_API_KEY="sk-..."
```

### 3. Install Dependensi

Gunakan perintah bawaan `uv` atau `pip` standar untuk menginstal dependensi dari environment yang tersedia di `pyproject.toml`.

```bash
uv sync
```

### 4. Menjalankan Aplikasi

Jalankan server menggunakan command `fastapi` CLI (atau uvicorn):

```bash
fastapi dev app/main.py
```

Server akan berjalan secara default di `http://127.0.0.1:8000`.

## Dokumentasi API (Scalar UI)

Anda bisa melihat dokumentasi interaktif yang menggunakan **Scalar** dengan mengakses:

👉 **[http://127.0.0.1:8000/scalar](http://127.0.0.1:8000/scalar)**

## Contoh Penggunaan (Endpoint `/chat`)

**Request**:
```http
POST /chat
Content-Type: application/json

{
  "message": "Apa itu FastAPI?"
}
```

**Response**:
```json
{
  "response": "FastAPI adalah sebuah framework web modern dan cepat (high-performance) untuk membangun API dengan Python 3.8+ berdasarkan standar type hints."
}
```

---
*Dikembangkan sebagai bagian dari pembelajaran pada bootcamp Devscale Indonesia.*
