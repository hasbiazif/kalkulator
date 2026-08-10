import streamlit as st
from kalkulator import (
    tambah, kurang, kali, bagi,
    pangkat, akar, persen,
    sin, cos, tan, log, ln
)

if "memory" not in st.session_state:
    st.session_state.memory = 0.0
if "last_result" not in st.session_state:
    st.session_state.last_result = None

st.title("🧮 Kalkulator Scientific")
st.write("Kalkulator scientific berbasis web — project belajar Python & Streamlit.")

angka1 = st.number_input("Angka pertama", value=0.0)
angka2 = st.number_input("Angka kedua (untuk operasi 2 angka)", value=0.0)

operasi = st.selectbox("Pilih operasi", [
    "Penjumlahan (+)",
    "Pengurangan (-)",
    "Perkalian (×)",
    "Pembagian (÷)",
    "Pangkat (a^b)",
    "Akar kuadrat (√a)",
    "Persen (a%)",
    "Sin (a°)",
    "Cos (a°)",
    "Tan (a°)",
    "Log basis 10",
    "Ln (natural)",
])

if st.button("Hitung"):
    if operasi == "Penjumlahan (+)":
        hasil = tambah(angka1, angka2)

    elif operasi == "Pengurangan (-)":
        hasil = kurang(angka1, angka2)

    elif operasi == "Perkalian (×)":
        hasil = kali(angka1, angka2)

    elif operasi == "Pembagian (÷)":
        hasil = bagi(angka1, angka2)

    elif operasi == "Pangkat (a^b)":
        hasil = pangkat(angka1, angka2)

    elif operasi == "Akar kuadrat (√a)":
        hasil = akar(angka1)

    elif operasi == "Persen (a%)":
        hasil = persen(angka1)

    elif operasi == "Sin (a°)":
        hasil = sin(angka1)

    elif operasi == "Cos (a°)":
        hasil = cos(angka1)

    elif operasi == "Tan (a°)":
        hasil = tan(angka1)

    elif operasi == "Log basis 10":
        hasil = log(angka1)

    elif operasi == "Ln (natural)":
        hasil = ln(angka1)

    st.session_state.last_result = hasil

if st.session_state.last_result is not None:
    hasil = st.session_state.last_result
    if isinstance(hasil, (int,float)):
        hasil = round(hasil, 10)
    st.success(f"hasil = {hasil}")

st.subheader("💾 Memori")

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("M+"):
        if isinstance(st.session_state.last_result, (int, float)):
            st.session_state.memory += st.session_state.last_result
with c2:
    if st.button("M-"):
        if isinstance(st.session_state.last_result, (int, float)):
            st.session_state.memory -= st.session_state.last_result
with c3:
    if st.button("MR"):
        st.session_state.last_result = st.session_state.memory
with c4:
    if st.button("MC"):
        st.session_state.memory = 0.0

st.info(f"🧠 Memori: {st.session_state.memory}")