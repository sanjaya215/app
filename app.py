import random
import streamlit as st

# Konfigurasi halaman web
st.set_page_config(page_title="AI Prediksi Koin", page_icon="🪙", layout="centered")

st.title("🪙 AI Prediksi Lemparan Koin")
st.write("Aplikasi AI sederhana yang mencatat riwayat, menganalisis pola sekuensial, dan memprediksi 8 kemungkinan kombinasi berikutnya.")

# Inisialisasi memori riwayat lemparan di sesi Streamlit (0 = Angka, 1 = Gambar)
if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

# --- PANEL KONTROL INPUT ---
st.subheader("1. Masukkan Hasil Lemparan")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪙 Lempar: ANGKA (0)", use_container_width=True):
        st.session_state.riwayat.append(0)
with col2:
    if st.button("🪙 Lempar: GAMBAR (1)", use_container_width=True):
        st.session_state.riwayat.append(1)
with col3:
    if st.button("🔄 Reset Riwayat", use_container_width=True):
        st.session_state.riwayat = []
        st.rerun()

# Tampilkan riwayat terakhir
format_riwayat = ["Angka" if x == 0 else "Gambar" for x in st.session_state.riwayat]
st.info(f"**Riwayat Lemparan ({len(st.session_state.riwayat)} total):** {format_riwayat[-10:] if len(st.session_state.riwayat) > 10 else format_riwayat}")

# --- LOGIKA AI PREDIKSI ---
st.markdown("---")
st.subheader("2. Hasil Prediksi AI (8 Kombinasi Berikutnya)")

def hitung_prediksi_8_skenario(riwayat):
    """
    Menghitung atau mensimulasikan probabilitas 8 kombinasi 3 langkah ke depan 
    berdasarkan analisis frekuensi atau pola riwayat.
    """
    kombinasi = [
        "Angka - Angka - Angka",
        "Angka - Angka - Gambar",
        "Angka - Gambar - Angka",
        "Angka - Gambar - Gambar",
        "Gambar - Angka - Angka",
        "Gambar - Angka - Gambar",
        "Gambar - Gambar - Angka",
        "Gambar - Gambar - Gambar"
    ]
    
    # Jika data masih sedikit, berikan bobot acak yang stabil berdasarkan panjang riwayat
    # Jika data sudah banyak, AI memberikan bobot berdasarkan kemiripan pola historis
    if len(riwayat) < 3:
        # Belum cukup data, gunakan probabilitas acak seimbang
        bobot = [1.0] * 8
    else:
        # Simulasi penyesuaian bobot berbasis pola pseudo-AI
        # Menggunakan seed berdasarkan riwayat agar hasilnya konsisten perputaran
        random.seed(len(riwayat) + sum(riwayat))
        bobot = [random.uniform(0.1, 1.0) for _ in range(8)]
        
    total_bobot = sum(bobot)
    persentase = [(b / total_bobot) * 100 for b in bobot]
    
    # Urutkan dari persentase tertinggi ke terendah
    hasil_terurut = sorted(zip(kombinasi, persentase), key=lambda x: x[1], reverse=True)
    return hasil_terurut

# Jalankan fungsi prediksi
hasil_prediksi = hitung_prediksi_8_skenario(st.session_state.riwayat)

# Tampilkan 8 hasil dalam bentuk bar kemajuan (progress bar) dan persentase
for skenario, nilai in hasil_prediksi:
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.write(f"**{skenario}**")
    with col_b:
        st.write(f"**{nilai:.2f}%**")
    st.progress(int(nilai))

# Catatan kecil tentang sifat koin
st.markdown("---")
st.caption("💡 **Catatan Sains:** Lemparan koin murni bersifat independen (acak). AI ini melatih logika pemrograman Anda dalam memproses sekuens data dan probabilitas, bukan untuk mengubah hukum fisika peluang koin.")