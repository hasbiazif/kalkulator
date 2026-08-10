# 🧮 Kalkulator Scientific

Aplikasi kalkulator sederhana berbasis streamlit, project untuk belajar python dan streamlit

🔗 **Coba online:** https://kalkulator-belajar.streamlit.app/

## ✨ Fitur
- Operasi dasar: penjumlahan (+), pengurangan (−), perkalian (×), pembagian (÷)
- Scientific: pangkat, akar kuadrat, persen
- Trigonometri: sin, cos, tan (dalam derajat)
- Logaritma: log (basis 10) dan ln (natural)
- Memori: M+, M−, MR, MC

## 🛠️ Teknologi
- **Python** — bahasa pemrograman
- **Streamlit** — framework untuk bikin web app dari Python

## 📁 Struktur Project
| File | Fungsi |
|------|--------|
| `kalkulator.py` | Logika — semua fungsi matematika (Python murni) |
| `app.py` | Tampilan web Streamlit (memakai fungsi dari kalkulator.py) |
| `requirements.txt` | Daftar library yang dibutuhkan |

## 🚀 Cara Menjalankan di Komputer
1. Clone repo: `git clone https://github.com/hasbiazif/kalkulator.git`
2. Install library: `pip install -r requirements.txt`
3. Jalankan: `streamlit run app.py`

## 📚 Yang Saya Pelajari

- Fungsi (`def`) & memisahkan logika dari tampilan
- Modul `math` (akar, trigonometri, logaritma)
- Error handling (bagi nol) & perbedaan `print` vs `return`
- `session_state` Streamlit untuk fitur memori
- Workflow Git/GitHub (init, commit, push)
- Deploy ke Streamlit Cloud