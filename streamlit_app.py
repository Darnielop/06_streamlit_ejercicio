import streamlit as st
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import json

st.title("Empleatronix")
st.write("Todos los datos sobre los empleados en una aplicación.")

empleados = pd.read_csv('datasets/employees.csv')

# Mostramos los datos del dataframe
st.dataframe(empleados)

# Creamos 3 botones, 1 para seleccionar color y otros dos que al estar marcados muestren datos de una grafica, nombre y sueldos

color, name_toggle, salary_toggle = st.columns(3)

with color:
    color = st.color_picker("Elige un color para las barras", "#00f900")

with name_toggle:
    name_toggle = st.toggle("Mostrar el nombre", value=True)

with salary_toggle:
    salary_toggle = st.toggle("Mostrar sueldo en la barra")

# Creamos una grafica de barras con matplotlib

fig, ax = plt.subplots()

# Cambiar a un gráfico de barras horizontal
bars = ax.barh(empleados['full name'], empleados['salary'], color=color)

# Modificar etiquetas en función de las opciones
if not name_toggle:
    ax.set_yticklabels([''] * len(empleados['full name']))  # Ocultar nombres en el eje Y

if salary_toggle:
    # Añadir etiquetas de salario al final de cada barra
    for bar, salary in zip(bars, empleados['salary']):
        ax.text(bar.get_width() + 50, bar.get_y() + bar.get_height() / 2,
                f'{salary} €', va='center')

# Configurar etiquetas de los ejes
ax.set_xlabel('')
ax.set_ylabel('')

# Configurar el rango del eje X
ax.set_xlim(0, 4500)  # Asegurarse de que el eje X llega hasta 4500

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

st.write("© Darío Nievas López")