import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image

@st.cache
def run_fxn(n: int) -> list:
  return range(n)

st.title("Titulo : Analítica de Datos")

st.header("Este es un header")
st.subheader("Este es un subheader")

st.text("Texto: Hola streamlit")

st.markdown("# Este es un markdown h1 \n ## Este es un h2 \n ### Este es un h3")
st.header("Colores de texto y mensajes de error")
st.success("Successful")
st.info("Información!")
st.warning("Warning")
st.error("Error")
st.exception("NameError('no está definido')")
st.header("Obtener información de ayuda de Python")
st.help(range)
st.header("Widgets:")
st.subheader("Checkbox")

if st.checkbox("Show/Hide"):
  st.text("Mostrar u ocultar Widget")
  st.subheader("Radio buttons")

status = st.radio("Cual es su estatus", ("Activo","Inactivo"))
if status == "Activo":
  st.success("Estas activo")
else:
  st.warning("Inactivo")
  st.subheader("SelectBox")

occupation = st.selectbox(
    "Tu ocupación", ["Programador", "Científico de datos", "BI", "Ingeniero de Datos"]
)

st.write("Opción seleccionada:", occupation)
st.subheader("MultiSelect")

location = st.multiselect(
    "Donde trabajas?",
    ("México", "New York", "Guadalajara", "Monterrey", "Nepal", "Buenos Aires", "Caracas"),
)

st.write("Seleccionó:", len(location), "locaciones")
st.subheader("Slider")

level = st.slider("Cual es tu nivel?", 1, 5)
st.write("Nivel:",level)
