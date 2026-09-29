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
#  - link:  URL de la app
#  - image: nombre del archivo dentro de la carpeta img/
# ============================================================
PROJECTS = [
    {
        "tag": "01 · Voz",
        "title": "Generador de Audio con IA",
        "description": "Convierte texto en voz con distintos idiomas y acentos, con opción de lectura lenta.",
        "link": "https://holaaaa2.streamlit.app/",
        "image": "holaaaa2.jpg",
    },
    {
        "tag": "02 · Introducción",
        "title": "Hola, soy Sofi",
        "description": "Mi primera app en Streamlit: texto, imágenes, entradas de usuario y diseño en columnas.",
        "link": "https://sofyintro.streamlit.app/",
        "image": "sofyintro.jpg",
    },
    {
        "tag": "03 · Texto",
        "title": "Sentiméntmetro AI",
        "description": "Analiza el sentimiento de una frase escrita en español y lo interpreta al instante.",
        "link": "https://clase3sep3.streamlit.app/",
        "image": "clase3sep3.jpg",
    },
    {
        "tag": "04 · Texto",
        "title": "Buscador TF-IDF",
        "description": "Motor de búsqueda que encuentra la respuesta más parecida a tu pregunta usando TF-IDF.",
        "link": "https://clase3sep1.streamlit.app/",
        "image": "clase3sep1.jpg",
    },
    {
        "tag": "05 · Visión",
        "title": "Clasificador con Teachable Machine",
        "description": "Toma una foto con la cámara y un modelo entrenado en Teachable Machine la identifica.",
        "link": "https://clase3sep.streamlit.app/",
        "image": "clase3sep.jpg",
    },
    {
        "tag": "06 · Visión",
        "title": "Reconocimiento de Imágenes",
        "description": "Clasificación en tiempo real desde la cámara, un archivo o una URL.",
        "link": "https://clase10sep2.streamlit.app/",
        "image": "clase10sep2.jpg",
    },
    {
        "tag": "07 · IA generativa",
        "title": "Asistente RAG",
        "description": "Sube un PDF y conversa con su contenido gracias a un modelo de OpenAI.",
        "link": "https://clase24sep.streamlit.app/",
        "image": "clase24sep.jpg",
    },
    {
        "tag": "08 · Visión + IA",
        "title": "Análisis Inteligente de Imágenes",
        "description": "GPT-4o describe una imagen o responde preguntas específicas sobre ella.",
        "link": "https://clase24sep2.streamlit.app/",
        "image": "clase24sep2.jpg",
    },
    {
        "tag": "09 · Visión",
        "title": "AI Vision Studio",
        "description": "Detección de objetos con YOLOv5, con ajustes de confianza y umbral IoU.",
        "link": "https://clase10sep.streamlit.app/",
        "image": "clase10sep.jpg",
    },
    {
        "tag": "10 · Visión + Voz",
        "title": "OCR & Reader Studio",
        "description": "Extrae el texto de una imagen, lo traduce y lo lee en voz alta.",
        "link": "https://otroooo1.streamlit.app/",
        "image": "otroooo1.jpg",
    },
    {
        "tag": "11 · Visión",
        "title": "Studio OCR",
        "description": "Captura con la cámara, aplica filtros de contraste y extrae el texto en tiempo real.",
        "link": "https://otroooo2.streamlit.app/",
        "image": "otroooo2.jpg",
    },
    {
        "tag": "12 · Voz",
        "title": "Traductor por Voz",
        "description": "Escucha lo que dices, lo traduce al idioma que elijas y lo reproduce en voz alta.",
        "link": "https://otroooo3.streamlit.app/",
        "image": "otroooo3.jpg",
    },
]

CSS = """
<style>
:root {
  --bg: #ffffff;
  --surface: #f5f5f7;
  --text: #1d1d1f;
  --text-2: #6e6e73;
  --line: rgba(0, 0, 0, 0.08);
  --link: #0066cc;
  --radius: 28px;
  --ease: cubic-bezier(0.25, 1, 0.5, 1);
}

/* Ocultar la interfaz de Streamlit */
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stHeaderActionElements"] { display: none !important; }

.stApp { background: var(--bg); }
.block-container { max-width: 1200px; padding: 0 22px !important; }

.pf, .pf * {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text",
    "Helvetica Neue", Helvetica, Arial, sans-serif !important;
  -webkit-font-smoothing: antialiased;
  letter-spacing: -0.011em;
  box-sizing: border-box;
}
.pf { color: var(--text); line-height: 1.47; }
.pf a { text-decoration: none; }

/* Nav */
.pf-nav {
  display: flex; justify-content: space-between; align-items: center;
  height: 48px; font-size: 13px; border-bottom: 1px solid var(--line);
}
.pf-nav .brand { font-weight: 600; color: var(--text); }
.pf-nav .meta { color: var(--text-2); }

/* Hero */
.pf-hero { padding: 110px 0 72px; text-align: center; }
.pf-hero .eyebrow { font-size: 17px; font-weight: 600; color: var(--text-2); margin-bottom: 12px; }
.pf-hero h1 {
  font-size: clamp(48px, 9vw, 96px); font-weight: 700;
  letter-spacing: -0.035em; line-height: 1.02; color: var(--text);
  padding: 0; margin: 0;
}
.pf-hero p {
  max-width: 620px; margin: 24px auto 0;
  font-size: clamp(19px, 2.2vw, 24px); color: var(--text-2);
  line-height: 1.35; letter-spacing: -0.015em;
}

/* Grid */
.pf-grid {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 20px; padding-bottom: 120px;
}
.pf-card {
  display: flex; flex-direction: column;
  background: var(--surface); border-radius: var(--radius); overflow: hidden;
  color: var(--text) !important;
  transition: transform 0.5s var(--ease), box-shadow 0.5s var(--ease);
  animation: pf-in 0.8s var(--ease) both;
}
.pf-card:hover { transform: scale(1.015); box-shadow: 0 20px 50px rgba(0, 0, 0, 0.08); }
.pf-media { aspect-ratio: 16 / 10; overflow: hidden; border-bottom: 1px solid var(--line); }
.pf-media img { width: 100%; height: 100%; object-fit: cover; object-position: top; display: block; }
.pf-body { padding: 26px 28px 30px; }
.pf-tag {
  font-size: 12px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.06em; color: var(--text-2);
}
.pf-title {
  margin-top: 8px; font-size: 24px; font-weight: 700;
  letter-spacing: -0.025em; line-height: 1.1; color: var(--text);
}
.pf-desc { margin-top: 10px; font-size: 15px; color: var(--text-2); }
.pf-link { display: inline-block; margin-top: 16px; font-size: 15px; color: var(--link); }
.pf-link::after {
  content: "›"; display: inline-block; margin-left: 4px;
  transition: transform 0.3s var(--ease);
}
.pf-card:hover .pf-link { text-decoration: underline; }
.pf-card:hover .pf-link::after { transform: translateX(3px); }

/* Footer */
.pf-footer {
  border-top: 1px solid var(--line); padding: 24px 0 40px;
  font-size: 12px; color: var(--text-2);
  display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap;
}

@keyframes pf-in {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: none; }
}

@media (prefers-reduced-motion: reduce) {
  .pf-card, .pf-link::after { animation: none; transition: none; }
  .pf-card:hover { transform: none; }
}

@media (max-width: 1024px) { .pf-grid { grid-template-columns: repeat(2, 1fr); } }

@media (max-width: 734px) {
  .block-container { padding: 0 16px !important; }
  .pf-hero { padding: 72px 0 48px; }
  .pf-grid { grid-template-columns: 1fr; gap: 16px; padding-bottom: 80px; }
  .pf-body { padding: 24px 24px 28px; }
  .pf-title { font-size: 22px; }
}
</style>
"""


@st.cache_data
def image_data_uri(filename: str) -> str:
    data = (IMG_DIR / filename).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()


def card(p: dict, i: int) -> str:
    # Sin sangría ni saltos de línea: Streamlit interpreta el HTML como Markdown
    return (
        f'<a class="pf-card" href="{p["link"]}" target="_blank" rel="noopener" '
        f'style="animation-delay:{i * 60}ms">'
        f'<div class="pf-media"><img src="{image_data_uri(p["image"])}" alt="{p["title"]}" loading="lazy"></div>'
        f'<div class="pf-body">'
        f'<div class="pf-tag">{p["tag"]}</div>'
        f'<div class="pf-title">{p["title"]}</div>'
        f'<div class="pf-desc">{p["description"]}</div>'
        f'<span class="pf-link">Ver proyecto</span>'
        f"</div></a>"
    )


st.markdown(CSS, unsafe_allow_html=True)

page = (
    '<div class="pf">'
    '<nav class="pf-nav"><span class="brand">Sofía López</span>'
    '<span class="meta">Interfaces Multimodales</span></nav>'
    '<header class="pf-hero">'
    '<div class="eyebrow">Interfaces Multimodales</div>'
    "<h1>Proyectos.</h1>"
    "<p>Doce exploraciones en voz, texto, visión e inteligencia artificial. "
    "Diseñadas para sentirse naturales.</p>"
    "</header>"
    '<main class="pf-grid">' + "".join(card(p, i) for i, p in enumerate(PROJECTS)) + "</main>"
    '<div class="pf-footer"><span>© 2026 Sofía López</span>'
    "<span>Universidad EAFIT · Interfaces Multimodales</span></div>"
    "</div>"
)

st.markdown(page, unsafe_allow_html=True)
