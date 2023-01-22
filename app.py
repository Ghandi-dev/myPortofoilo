from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profil.png"
sertif1 = current_dir / "assets" / "sertifikat1.png"
sertif2 = current_dir / "assets" / "sertifikat_ds.png"
sertif3 = current_dir / "assets" / "sertifikat_R.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sonnya Ghandi"
PAGE_ICON = ":wave:"
NAME = "Sonnya Ghandi"
DESCRIPTION = """
Mahasiswa Teknik Informatika, Sekolah Tinggi Teknologi Wastukancana.
"""
EMAIL = "sonnyaghandi@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCyG-d5ve_p6aJ8aggggPLDA",
    "GitHub": "https://github.com/Ghandi-dev",
    "Instagram": "https://www.instagram.com/ghandi_02/",
    "WhatsApp": "https://wa.me/6285927532252",
}
PROJECTS = {
    "🏆 Aplikasi Kredit Barang | PHP - Codeigniter3 ": "https://github.com/Ghandi-dev/AplikasiKreditBarang",
    "🏆 Aplikasi Cek Tingkat Depresi | Python - Streamlit": "https://github.com/Ghandi-dev/CekApp",
    "🏆 Jam Digital (max2719 - RTC DS3231) | Raspberry pi pico": "https://github.com/Ghandi-dev/PicoJamDigital-max7219---RTC-DS3231-",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- link sosial media ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Ringkasan ---
st.write('\n')
st.subheader("Ringkasan")
st.write("---")
st.write(
    """Nama saya Sonnya Ghandi, saya mahasiswa aktif jurusan teknik informatika di STT Wastukancana 
Purwakarta yang memiliki minat terhadap dunia programming. Memiliki kemampuan dalam bahasa 
pemrograman, pemeliharaan perangkat lunak, merancang website dan implementasinya.

"""
)


# --- Pendidikan ---
st.write('\n')
st.subheader("Pendidikan")
st.write("---")
st.write(
    """👩‍💻 STT Wastukancana Purwakarta, Teknik Informatika (2020 – Sekarang)<br><br>
👨‍🎓 SMA Negeri 1 Pasawahan, Jurusan IPA (2014 – 2017)
"""
,unsafe_allow_html=True)


# --- Pengalaman kerja ---
st.write('\n')
st.subheader("Pengalaman Kerja")
st.write("---")

# --- 1
st.write("🧑‍🔧", "**Operator produksi | PT. Astra Honda Motor | 2018 – 2020**")
st.write(
    """Melakukan pengecekan kondisi barang setengah jadi sesuai dengan standart produksi baik secara spec maupun size produk, menambahkan bahan atau material atau komponen berikutnya pada produk menjadi barang setengah jadi atau barang jadi, Mengirim barang produk tersebut ke proses produksi berikutnya.
"""
)

# --- 2
st.write('\n')
st.write("🧑‍🔧", "**Operator produksi | PT. YC Tech | 2022**")
st.write(
    """Menyiapkan mesin yang akan digunakan untuk membuat outsole sepatu, kemudian mengirim outsole sepatu yang sudah jadi ke proses packing.
"""
)


# --- Pengalaman Organisasi
st.write('\n')
st.subheader("Pengalaman Organisasi")
st.write("---")
st.write(
    """🧑‍💼 Panitia Masa Bimbingan Mahasiswa Teknik Informatika STT Wastukancana Purwakarta ( 2021 dan 2022)<br><br>
🏕️ Ketua Pramuka SMA Negeri 1 Pasawahan ( 2016 – 2017 )<br><br>
🧑‍💼 OSIS SMA Negeri 1 Pasawahan

"""
,unsafe_allow_html=True)

# --- Pengalaman Organisasi
st.write('\n')
st.subheader("Skill")
st.write("---")
st.write(
    """✅ Java<br>
✅ PHP<br>
✅ Python<br>
✅ Codeigniter3<br>
✅ Mysql<br>
✅ Adobe Photoshop<br>
✅ Adobe Ilustrator<br>

"""
,unsafe_allow_html=True)

# --- proyek saya 
st.write('\n')
st.subheader("Proyek Saya")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Sertifikat
sertif1 = Image.open(sertif1)
sertif2 = Image.open(sertif2)
sertif3 = Image.open(sertif3)
st.write('\n')
st.subheader("Sertifikat")
st.write("---")
st.write("⭐ Fundamental SQL Using SELECT Statement")
st.image(sertif1,"sertifikat Fundamental SQL Using SELECT Statement ")
st.write("⭐ Python Fudamental for Data Science")
st.image(sertif2,"sertifikat Python Fudamental for Data Science ")
st.write("⭐ R Fudamental for Data Science")
st.image(sertif3,"sertifikat R Fudamental for Data Science ")
