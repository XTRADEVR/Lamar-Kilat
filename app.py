import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="LamarKilat Depok", page_icon="🚀", layout="centered")

if "lowongan" not in st.session_state:
    st.session_state.lowongan = [
        {"id":1, "posisi":"Kasir Toko","kategori":"Sales","tipe":"Full-time","lokasi":"Margonda, Depok","gaji":"2.5-3jt","deskripsi":"Butuh kasir jujur, bisa komputer","pelamar":12,"tanggal":"2026-10-25"},
    ]
if "pelamar" not in st.session_state:
    st.session_state.pelamar = [
        {"nama":"Siti","posisi":"Kasir Toko","wa":"0812xxxx","status":"Baru"},
    ]

st.title("🚀 LamarKilat")
st.caption("Dashboard Toko - Anti Firebase Error")

tab1, tab2 = st.tabs(["📋 Kelola Lowongan", "👥 Pelamar"])

with tab1:
    with st.expander("➕ [+ Buat Lowongan Baru] - KLIK DISINI", expanded=True):
        with st.form("form_loker"):
            posisi = st.text_input("Nama Posisi *", placeholder="Kasir, Admin")
            kategori = st.selectbox("Kategori", ["Admin","Marketing","Sales","Operasional","IT"])
            tipe = st.selectbox("Tipe", ["Full-time","Part-time","Contract"])
            lokasi = st.text_input("Lokasi", value="Depok")
            gaji = st.text_input("Gaji", placeholder="2.5jt - 3.5jt")
            deskripsi = st.text_area("Deskripsi")
            submit = st.form_submit_button("🚀 Simpan Lowongan", type="primary", use_container_width=True)
            if submit and posisi:
                st.session_state.lowongan.append({
                    "id":len(st.session_state.lowongan)+1, "posisi":posisi, "kategori":kategori,
                    "tipe":tipe, "lokasi":lokasi, "gaji":gaji, "deskripsi":deskripsi,
                    "pelamar":0, "tanggal": datetime.now().strftime("%Y-%m-%d")
                })
                st.success(f"✅ {posisi} berhasil!")
                st.balloons()

    st.subheader(f"Daftar Lowongan ({len(st.session_state.lowongan)})")
    for job in reversed(st.session_state.lowongan):
        with st.container(border=True):
            st.markdown(f"**{job['posisi']}** - {job['kategori']} - {job['lokasi']}")
            st.caption(f"{job['tipe']} | {job['gaji']}")

with tab2:
    st.dataframe(pd.DataFrame(st.session_state.pelamar), use_container_width=True)
