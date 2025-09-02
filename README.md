# ⏱️ Consulta de Horas de Personas con Streamlit

Aplicación en **Streamlit** que permite consultar y filtrar información de un archivo **Excel**, mostrando los resultados de horas trabajadas por persona y calculando el **total de horas**.

---

## 🚀 Características

- Carga de datos desde un archivo **Excel** (`.xlsx`).
- Búsqueda por:
  - **Nombre de empresa** (`NOMBRE`)
  - **Empleado** (`EMPLEADO`)
- Visualización de resultados en una tabla interactiva.
- Cálculo automático del **total de horas trabajadas**.
- Uso de **caché de datos** con `st.cache_data` para mejorar el rendimiento.

---

## 🛠️ Tecnologías utilizadas

- [Streamlit](https://streamlit.io/) – Framework para aplicaciones web interactivas en Python.
- [Pandas](https://pandas.pydata.org/) – Manipulación y análisis de datos.
- [Excel (.xlsx)](https://support.microsoft.com/es-es/excel) – Fuente de datos.

---

## 📦 Instalación y uso

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo
