import streamlit as st
from kalkulator import (
    tambah, kurang, kali, bagi,
    pangkat, akar, persen,
    sin, cos, tan, log, ln
)

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

    st.write("Hasil =", hasil)