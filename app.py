import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="LamarKilat - Depok", page_icon="🚀", layout="centered")

if "lowongan" not in st.session_state:
    st.session_state.lowongan = [
        {"id":1, "posisi":"Kasir Toko","kategori":"Sales","tipe":"Full-time","lokasi":"Margonda, Depok","gaji":"2.5-3jt","deskripsi":"Butuh kasir jujur","pelamar":12,"tanggal":"2026-10-25"},
    ]
if "pelamar" not in st.session_state:
    st.session_state.pelamar = [
        {"nama":"Siti","posisi":"Kasir Toko","wa":"0812xxxx","status":"Baru"},
    ]

st.title("🚀 LamarKilat")
tab1, tab2, tab3 = st.tabs(["📋 Kelola Lowongan", "👥 Pelamar", "📊 Export"])

with tab1:
    with st.expander("➕ [+ Buat Lowongan Baru] - KLIK DISINI", expanded=True):
        with st.form("form_loker"):
            posisi = st.text_input("Nama Posisi *", placeholder="Kasir, Admin, OB")
            kategori = st.selectbox("Kategori", ["Admin","Marketing","Sales","Operasional","IT"])
            tipe = st.selectbox("Tipe", ["Full-time","Part-time","Contract"])
            lokasi = st.text_input("Lokasi", value="Depok")
            gaji = st.text_input("Gaji", placeholder="2.5jt - 3.5jt")
            deskripsi = st.text_area("Deskripsi")
            if st.form_submit_button("🚀 Simpan & Publish", type="primary", use_container_width=True):
                if posisi:
                    st.session_state.lowongan.append({"id":len(st.session_state.lowongan)+1, "posisi":posisi, "kategori":kategori, "tipe":tipe, "lokasi":lokasi, "gaji":gaji, "deskripsi":deskripsi, "pelamar":0, "tanggal": datetime.now().strftime("%Y-%m-%d")})
                    st.success(f"✅ {posisi} berhasil!"); st.balloons()

    st.subheader(f"Daftar Lowongan ({len(st.session_state.lowongan)})")
    for job in reversed(st.session_state.lowongan):
        with st.container(border=True):
            st.markdown(f"**{job['posisi']}** ` {job['kategori']} `")
            st.caption(f"📍 {job['lokasi']} | 💰 {job['gaji']}")
