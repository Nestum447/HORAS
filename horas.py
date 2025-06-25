import streamlit as st
import pandas as pd

# Leer el archivo Excel una sola vez
@st.cache_data
def cargar_datos():
    # Asegúrate de que el archivo Excel esté en el mismo directorio o usa la ruta completa
    return pd.read_excel('datoslemp.xlsx', sheet_name='lempa8')  # Ajusta nombre del archivo y hoja si es necesario

# Función para consultar los datos según los filtros
def consulta_excel(df, NOMBRE, EMPLEADO):
    # Aplicar filtros con pandas
    filtro = (
        df['NOMBRE'].str.contains(NOMBRE, case=False, na=False) &
        df['EMPLEADO'].str.contains(EMPLEADO, case=False, na=False)
    )
    return df[filtro]

# Título de la aplicación
st.title("Consulta de Horas de Personas")

# Crear cuadros de entrada para nombre de empresa y empleado
empresa = st.text_input("Ingrese el nombre")
empleado = st.text_input("Ingrese el Apellido y Nombre")

# Cargar datos desde Excel
df_datos = cargar_datos()

# Botón para consultar
if st.button("Consultar"):
    if empresa or empleado:
        df_filtrado = consulta_excel(df_datos, empresa, empleado)

        if not df_filtrado.empty:
           # st.write(f"Resultados encontrados para: **{empleado}** en Nombre **{empresa}**")
           #st.dataframe(df_filtrado)

            st.write(f"Resultados encontrados para: **{empleado}** en Nombre **{empresa}**")
            st.dataframe(df_filtrado)

            # Convertir a numérico por si hay errores o celdas vacías
            df_filtrado['HORAS'] = pd.to_numeric(df_filtrado['HORAS'], errors='coerce')

            # Sumar la columna HORAS
            total_horas = df_filtrado['HORAS'].sum()

            # Mostrar el total
            st.write(f"**Total de HORAS:** {total_horas}")



        
        else:
            st.write("No se encontraron resultados para los datos ingresados.")
