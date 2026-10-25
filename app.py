import streamlit as st
from datetime import datetime

st.set_page_config(page_title="LamarKilat Luxury", page_icon="💎", layout="wide")

# --- BACKGROUND MEWAH LUXURY ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }

.stApp {
  background: radial-gradient(1200px 600px at 10% -10%, #3b2ff5 0%, transparent 60%),
              radial-gradient(1000px 500px at 90% 0%, #ff3d9a 0%, transparent 60%),
              radial-gradient(800px 400px at 50% 120%, #00d4ff 0%, transparent 60%),
              #080a12 !important;
}
div[data-testid="stHeader"] { background: transparent; }

.hero-luxury {
  background: linear-gradient(180deg, rgba(255,255,255,0.12), rgba(255,255,255,0.04));
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 28px;
  padding: 36px 32px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.2);
  position: relative; overflow: hidden;
}
.hero-luxury::before {
  content:""; position:absolute; top:-50%; left:-30%; width:80%; height:200%;
  background: radial-gradient(circle, rgba(255,255,255,0.18) 0%, transparent 60%);
  transform: rotate(20deg);
}
.metric-lux {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  backdrop-filter: blur(16px);
  border-radius: 20px; padding: 22px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}
.empty-state {
  background: rgba(255,255,255,0.04);
  border: 1px dashed rgba(255,255,255,0.2);
  border-radius: 24px; padding: 60px 20px; text-align: center;
  margin-top: 20px;
}
.job-card {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 20px; padding: 20px; backdrop-filter: blur(12px);
  margin-bottom: 14px;
}
.stButton>button {
  background: linear-gradient(90deg, #6a5af9, #ff3d9a) !important;
  color: white !important; border: none !important;
  border-radius: 14px !important; font-weight: 800 !important;
  height: 52px; box-shadow: 0 10px 20px rgba(106,90,249,0.4);
}
input, textarea, div[data-baseweb="select"] > div {
  background: rgba(0,0,0,0.3) !important;
  border: 1px solid rgba(255,255,255,0.15) !important;
  border-radius: 14px !important; color: white !important;
}
</style>
""", unsafe_allow_html=True)

# --- DATA KOSONG TOTAL ---
if "lowongan" not in st.session_state:
    st.session_state.lowongan = []  # KOSONG
if "pelamar" not in st.session_state:
    st.session_state.pelamar = []  # KOSONG

# --- HERO MEWAH ---
st.markdown("""
<div class="hero-luxury">
  <div style="position:relative; z-index:2">
    <div style="display:flex; align-items:center; gap:12px">
      <div style="width:48px; height:48px; background:linear-gradient(135deg,#6a5af9,#ff3d9a); border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:24px">💎</div>
      <div><h1 style="margin:0; font-size:34px; font-weight:800; letter-spacing:-1px; color:white">LamarKilat</h1><small style="letter-spacing:4px; opacity:0.7; font-weight:600">LUXURY EDITION</small></div>
    </div>
    <p style="margin:18px 0 0 0; font-size:17px; line-height:1.5; opacity:0.85; max-width:600px">
      Dashboard rekrutmen paling mewah untuk UMKM Depok. Dibuat untuk toko yang ingin terlihat profesional & terpercaya.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# Metrics kosong = 0
c1, c2, c3, c4 = st.columns(4)
c1.markdown(f'<div class="metric-lux"><small style="opacity:0.6">LOWONGAN</small><h2 style="margin:8px 0 0 0; font-size:32px">{len(st.session_state.lowongan)}</h2><small style="color:#a99cff">Siap tayang</small></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="metric-lux"><small style="opacity:0.6">PELAMAR</small><h2 style="margin:8px 0 0 0; font-size:32px">{len(st.session_state.pelamar)}</h2><small style="color:#6ee7b7">Belum ada</small></div>', unsafe_allow_html=True)
c3.markdown('<div class="metric-lux"><small style="opacity:0.6">DITERIMA</small><h2 style="margin:8px 0 0 0; font-size:32px">0</h2><small style="opacity:0.6">Mulai rekrut</small></div>', unsafe_allow_html=True)
c4.markdown('<div class="metric-lux"><small style="opacity:0.6">WAKTU RESPON</small><h2 style="margin:8px 0 0 0; font-size:32px">-</h2><small style="opacity:0.6">Baru mulai</small></div>', unsafe_allow_html=True)

st.write("")
tab1, tab2 = st.tabs(["📋 Kelola Lowongan", "👥 Data Pelamar"])

with tab1:
  col1, col2 = st.columns([1.3, 1])
  with col1:
    if len(st.session_state.lowongan) == 0:
        st.markdown("""
        <div class="empty-state">
          <div style="font-size:48px">📭</div>
          <h3 style="margin-top:12px">Belum ada lowongan</h3>
          <p style="opacity:0.6">Klik form di samping untuk buat lowongan pertama toko Anda.<br>Akan terlihat profesional langsung.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for job in reversed(st.session_state.lowongan):
            st.markdown(f'<div class="job-card"><b>{job["posisi"]}</b> • {job["lokasi"]}<br><small style="opacity:0.6">{job["kategori"]} • {job["tipe"]} • {job["gaji"]}</small></div>', unsafe_allow_html=True)

  with col2:
    with st.container(border=True):
        st.markdown("#### ➕ Buat Lowongan Pertama")
        with st.form("lux_form", clear_on_submit=True):
            posisi = st.text_input("Posisi *", placeholder="Contoh: Kasir Toko")
            kategori = st.selectbox("Kategori", ["Sales","Admin","Marketing","Operasional","IT"])
            tipe = st.selectbox("Tipe", ["Full-time","Part-time"])
            lokasi = st.text_input("Lokasi", value="Depok")
            gaji = st.text_input("Gaji", placeholder="Rp 3jt")
            desk = st.text_area("Deskripsi singkat")
            if st.form_submit_button("✨ Terbitkan Sekarang", use_container_width=True, type="primary"):
                if posisi:
                    st.session_state.lowongan.append({"posisi":posisi,"kategori":kategori,"tipe":tipe,"lokasi":lokasi,"gaji":gaji,"desk":desk})
                    st.success("Berhasil! Lowongan pertama jadi.")
                    st.balloons()
                    st.rerun()

with tab2:
  if len(st.session_state.pelamar) == 0:
      st.markdown("""
      <div class="empty-state">
        <div style="font-size:48px">👥</div>
        <h3>Belum ada pelamar</h3>
        <p style="opacity:0.6">Setelah toko buat lowongan, pelamar akan masuk otomatis di sini.</p>
      </div>
      """, unsafe_allow_html=True)
  else:
      st.dataframe(st.session_state.pelamar)
