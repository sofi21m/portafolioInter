import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Sofía López · Portafolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

IMG_DIR = Path(__file__).parent / "img"

# ============================================================
#  PROYECTOS
# - link: URL de la app
# - image: nombre del archivo dentro de la carpeta img/
# =================================
