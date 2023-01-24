import time
import requests
from streamlit_extras.switch_page_button import switch_page
from pathlib import Path
import streamlit as st
from streamlit_lottie import st_lottie
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets10.lottiefiles.com/packages/lf20_ukjcyybw.json"
lottie_loading = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_p8bfn5to.json")
lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="hello")
col1,col2,col3 = st.columns(3)
with col2:
    st_lottie(lottie_loading)
time.sleep(3)
switch_page("app")