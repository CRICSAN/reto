import streamlit as st
import pandas as pd
import emoji  # ← ¡NO viene por defecto en Streamlit Cloud!
from datetime import datetime
import random

# Configuración de página
st.set_page_config(page_title="App con Librerías Especiales", layout="wide")

# Título con emoji usando la librería 'emoji'
st.title(emoji.emojize(":rocket: Mi App con Requirements.txt :chart_increasing:"))

# Subtítulo
st.subheader("Demostrando que requirements.txt ES necesario")

# 1. USANDO EMOJI (librería no común)
st.write("### 1. Emojis con librería 'emoji'")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(emoji.emojize(":red_heart: Corazón rojo"))
with col2:
    st.write(emoji.emojize(":thumbs_up: Pulgar arriba"))
with col3:
    st.write(emoji.emojize(":fire: Fuego"))

# 2. DATAFRAME con pandas
st.write("### 2. DataFrame con Pandas")
data = {
    'Producto': ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas'],
    'Cantidad': [150, 200, 80, 120],
    'Precio': [25.5, 18.3, 12.8, 45.0],
    'Emoji': [emoji.emojize(":red_apple:"), 
              emoji.emojize(":tangerine:"), 
              emoji.emojize(":banana:"), 
              emoji.emojize(":grapes:")]
}
df = pd.DataFrame(data)
df['Total'] = df['Cantidad'] * df['Precio']
st.dataframe(df, use_container_width=True)

# 3. GRÁFICO simple con Streamlit nativo
st.write("### 3. Gráfico de barras")
st.bar_chart(df.set_index('Producto')['Total'])

# 4. SIMULACIÓN que requiere random
st.write("### 4. Números aleatorios con Random")
if st.button("Generar número aleatorio"):
    num = random.randint(1, 100)
    st.success(f"Número generado: {num} {emoji.emojize(':game_die:')}")

# 5. FECHA actual
st.write("### 5. Fecha y hora actual")
now = datetime.now()
st.info(f"Fecha: {now.strftime('%d/%m/%Y')}")
st.info(f"Hora: {now.strftime('%H:%M:%S')} {emoji.emojize(':alarm_clock:')}")

# 6. EXPLICACIÓN de requirements.txt
with st.expander("¿Por qué funciona esto?"):
    st.write("""
    Esta app FUNCIONA porque `requirements.txt` le dice a Streamlit Cloud:
    
    1. **streamlit>=1.28.0** - El framework principal ✅
    2. **pandas>=2.0.0** - Para DataFrames ✅  
    3. **emoji==2.10.0** - Para mostrar emojis ✅
    4. **python-dotenv==1.0.0** - Para variables de entorno ✅
    
    **Sin requirements.txt**: Fallaría con `ModuleNotFoundError: No module named 'emoji'`
    
    **Con requirements.txt**: Streamlit Cloud instala todo automáticamente ✅
    """)

# Pie de página
st.divider()
st.caption(f"App generada el {now.strftime('%d/%m/%Y %H:%M')} | Requirements.txt funciona correctamente")

