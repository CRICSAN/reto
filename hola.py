import streamlit as st
import pandas as pd
from PIL import Image

st.title("Dashboard de desempeño")
st.write("Análisis básico de empleados de Socialize your knowledge. " \
"Nos permitirá identificar fortalezas y áreas de oportunidad, y así lograr mejorar su rendimiento y obtener mayor calidad en los servicios")

# Cargar datos
df = pd.read_csv('Employee_data.csv')

# Codigo que permita desplegar el logotipo de la empresa en la aplicación web.
logo = Image.open("logo.png")
st.sidebar.image(logo, width=200)

# control para seleccionar el género del empleado
genero = st.sidebar.radio("Género:", ["Todos", "M", "F"])

# control para seleccionar el puntaje del empleado 
puntaje = st.sidebar.slider("Puntaje mínimo:", 1, 4, 1)

# control para seleccionar el estado civil del empleado
estado_civil = st.sidebar.multiselect("Estado civil:", options=["Divorced", "Married", "Single", "Separated", "Widowed"])

# Aplicar filtros
datos_filtrados = df[df['marital_status'].isin(estado_civil)] 


if genero == "Todos":
    datos_filtrados = df[df['performance_score'] >= puntaje]
else:
    datos_filtrados = df[(df['gender'] == genero) & (df['performance_score'] >= puntaje)]


if estado_civil:
    datos_filtrados = datos_filtrados[datos_filtrados['marital_status'].isin(estado_civil)]


# Esstadísticas generales
col1, col2, col3 = st.columns(3)
col1.metric("Empleados", len(datos_filtrados)) 
col2.metric("Puntaje desempeño Promedio", f"{datos_filtrados['performance_score'].mean():.2f}")
col3.metric("Salario Promedio", f"${datos_filtrados['salary'].mean():,.0f}")

# •	Código que permita mostrar un gráfico en donde se visualice la distribución de los puntajes de desempeño.
st.subheader("Distribución de Puntajes")
st.bar_chart(datos_filtrados['performance_score'].value_counts()) 

# •	Código que permita mostrar un gráfico en donde se visualice el promedio de horas trabajadas por el género del empleado.
st.subheader("Horas por Género")
st.bar_chart(datos_filtrados.groupby('gender')['average_work_hours'].mean())


# •	Código que permita mostrar un gráfico en donde se visualice la edad de los empleados con respecto al salario de los mismo.
st.subheader("Relación salario vs edad")
st.scatter_chart(datos_filtrados, x='age', y='salary')


# •	Código que permita mostrar un gráfico en donde se visualice la relación del promedio de horas trabajadas versus el puntaje de desempeño.
st.subheader("Relación horas promedio trabajadas vs performance")
st.scatter_chart(datos_filtrados, x='average_work_hours', y='performance_score', color='gender'
)


# Código de conclusiones
st.subheader("Conclusión")
st.write(f"El resultado nos indica que en promedio hay 2.98 de puntaje promedio, en una escala de 1 a 5 siendo 5 el máximo, todo en el total de los 311 empleados. Además, las mujeres en promedio trabajaron un poco más que los hombres  y hay una relación directa entre la edad de los trabajadores y el sueldo obtenido. Dato curioso, las personas viudas tuvieron mayor puntaje de desempeño.")
