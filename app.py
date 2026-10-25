import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="LamarKilat Pro", page_icon="⚡", layout="wide")

# --- CSS WEBSITE BERKUALITAS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #0e1117; }
.hero {
  background: linear-gradient(135deg, #6a5af9 0%, #d66efd 50%, #ff7e5f 100%);
  padding: 40px; border-radius: 20px; color: white; margin-bottom: 25px;
}
.hero h1 { font-size: 42px; font-weight: 800; margin:0; letter-spacing: -1px; }
.hero p { opacity:0.9; font-size: 18px; margin-top:8px; }
.metric-card {
  background: #1c1f26; border: 1px solid #2d313e; border-radius: 16px;
  padding: 20px; transition: 0.3s;
}
.metric-card:hover { border-color: #6a5af9; transform: translateY(-2px); }
.job-card {
  background: #1c1f26; border: 1px solid #2d313e; border-radius: 16px;
  padding: 18px 20px; margin-bottom: 12px;
}
.job-card b { font-size: 16px; }
.badge {
  display:inline-block; padding: 4px 10px; border-radius: 20px;
  font-size: 12px; font-weight: 600; margin-right: 6px;
}
.badge-purple { background: #2a254f; color: #a99cff; }
.badge-green { background: #1e3a2f; color: #6ee7b7; }
div[data-baseweb="select"] > div { background: #262730 !important; border-radius: 10px !important;}
input, textarea { border-radius: 10px !important; }
.stButton>button { border-radius: 12px !important; font-weight: 700 !important; height: 48px; }
</style>
""", unsafe_allow_html=True)

if "lowongan" not in st.session_state:
    st.session_state.lowongan = [
        {"id":1, "posisi":"Kasir Toko Modern","kategori":"Sales","tipe":"Full-time","lokasi":"Margonda, Depok","gaji":"Rp 2.8 - 3.5 Jt","deskripsi":"Jujur, teliti, bisa pakai POS","pelamar":12,"tanggal":"2026-10-25","status":"Aktif"},
        {"id":2, "posisi":"Admin Online Shop","kategori":"Admin","tipe":"Full-time","lokasi":"Beji, Depok","gaji":"Rp 3 - 4 Jt","deskripsi":"Balas chat Shopee/Tokped","pelamar":8,"tanggal":"2026-10-24","status":"Aktif"},
    ]
if "pelamar" not in st.session_state:
    st.session_state.pelamar = [
        {"nama":"Siti Aisyah","posisi":"Kasir Toko Modern","wa":"08123456789","status":"Baru","tgl":"25 Okt"},
        {"nama":"Budi Santoso","posisi":"Admin Online Shop","wa":"08129876543","status":"Interview","tgl":"24 Okt"},
    ]

# --- HERO HEADER ---
st.markdown("""
<div class="hero">
  <h1>⚡ LamarKilat Pro</h1>
  <p>Platform rekrutmen #1 untuk UMKM Depok. Kelola lowongan & pelamar dalam 1 dashboard modern.</p>
</div>
""", unsafe_allow_html=True)

# --- METRICS ---
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown(f'<div class="metric-card">👁️ <small>TOTAL LOWONGAN</small><br><h2 style="margin:0">{len(st.session_state.lowongan)}</h2><small style="color:#6ee7b7">+2 hari ini</small></div>', unsafe_allow_html=True)
with c2: st.markdown(f'<div class="metric-card">👥 <small>TOTAL PELAMAR</small><br><h2 style="margin:0">{len(st.session_state.pelamar)*6 + 18}</h2><small style="color:#a99cff">18 baru</small></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="metric-card">✅ <small>DITERIMA</small><br><h2 style="margin:0">4</h2><small style="color:#6ee7b7">Minggu ini</small></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="metric-card">⏱️ <small>WAKTU RESPON</small><br><h2 style="margin:0">2.4j</h2><small style="color:#ff7e5f">Rata-rata</small></div>', unsafe_allow_html=True)

st.write("")

tab1, tab2 = st.tabs(["📋 **Kelola Lowongan**", "👥 **Data Pelamar**"])

with tab1:
    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        st.subheader("Lowongan Aktif")
        for job in reversed(st.session_state.lowongan):
            st.markdown(f"""
            <div class="job-card">
              <div style="display:flex; justify-content:space-between">
                <b>{job['posisi']}</b> <span class="badge badge-green">{job['status']}</span>
              </div>
              <div style="margin-top:8px">
                <span class="badge badge-purple">{job['kategori']}</span>
                <span class="badge badge-purple">{job['tipe']}</span>
                <span style="font-size:13px; opacity:0.7">📍 {job['lokasi']} • 💰 {job['gaji']}</span>
              </div>
              <div style="margin-top:10px; font-size:13px; opacity:0.6">👥 {job['pelamar']} pelamar • {job['tanggal']}</div>
            </div>
            """, unsafe_allow_html=True)

    with col_right:
        with st.container(border=True):
            st.markdown("### ➕ Buat Lowongan Baru")
            st.caption("Isi form, langsung tayang ke halaman publik.")
            with st.form("form_pro", clear_on_submit=True):
                posisi = st.text_input("Nama Posisi *", placeholder="Contoh: Kasir Minimarket")
                cA, cB = st.columns(2)
                kategori = cA.selectbox("Kategori", ["Sales","Admin","Marketing","Operasional","IT","Kitchen"])
                tipe = cB.selectbox("Tipe Kerja", ["Full-time","Part-time","Contract","Freelance"])
                lokasi = st.text_input("Lokasi", value="Depok, Jawa Barat")
                gaji = st.text_input("Range Gaji", placeholder="Rp 2.5jt - Rp 3.5jt")
                deskripsi = st.text_area("Deskripsi Pekerjaan", placeholder="Tulis kriteria & jam kerja...", height=100)
                btn = st.form_submit_button("🚀 Terbitkan Lowongan", type="primary", use_container_width=True)
                if btn and posisi:
                    st.session_state.lowongan.append({
                        "id":len(st.session_state.lowongan)+1, "posisi":posisi, "kategori":kategori,
                        "tipe":tipe, "lokasi":lokasi, "gaji":gaji, "deskripsi":deskripsi,
                        "pelamar":0, "tanggal": datetime.now().strftime("%d %b"), "status":"Aktif"
                    })
                    st.success(f"Lowongan {posisi} berhasil diterbitkan!")
                    st.balloons()

with tab2:
    st.subheader("Kandidat Terbaru")
    df = pd.DataFrame(st.session_state.pelamar)
    st.dataframe(df, use_container_width=True, hide_index=True, 
                 column_config={
                     "wa": st.column_config.LinkColumn("WhatsApp", display_text="Chat WA"),
                     "status": st.column_config.SelectboxColumn("Status", options=["Baru","Interview","Diterima","Ditolak"])
                 })
    st.info("💡 Tips Pro: Klik status untuk ubah jadi Interview / Diterima. Nanti WA otomatis.")
