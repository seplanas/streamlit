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

st.subheader("Buttons")

if st.button("Acerca"):
  st.text("Streamlit es Cool")
else:
  st.text("")
st.header("Como recibir una entrada y procesarla en streamlit")
st.subheader("Recibiendo texto")

firstname = st.text_input("Escriba su nombre:")
if st.button("Aceptar"):
  result = firstname.title()
  st.success(result)
st.subheader("Area de texto")

message = st.text_area("Escriba un mensaje")
if st.button("Aceptar "):
  result = message.title()
  st.success(result)
st.subheader("Entrada de fecha")

today = st.date_input("Hoy es", datetime.datetime.now())
st.text(f"{today}")
st.subheader("Entrada de tiempo")

the_time = st.time_input("La hora es:",datetime.time())
st.text(f"{the_time}")
st.header("Trabajar con archivos de imágener, audio o vídeos")

st.subheader("Archivo de imagen")
img = Image.open("https://github.com/seplanas/streamlit/blob/main/calor%20y%20control.png")
st.image(img, width=300, caption="Simple Imagen")

st.header("Otras opciones que permite la función write")

st.subheader("Texto con write")
st.write("Texto con write")
st.write(range(10))
st.header("Desplegando códifo puro y json")
st.subheader("Código puro")
st.code("import numpy as np")
with st.echo():
  df = pd.DataFrame()
st.subheader("Desplegando json")
st.text("Mostrando JSON")
st.json({"nombre":"John","apellido":"Doe","genero":"masculino"})
st.header("Mostrar barra de progreso, spinner y balloons")
st.subheader("Barra de progreso")
my_bar = st.progress(0)

