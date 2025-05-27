# dashboards/app.py

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Configuración inicial
st.set_page_config(page_title="Dashboard Estudiantil UPC", layout="wide")

# Leer datos
base_dir = Path(__file__).resolve().parent.parent
df = pd.read_csv(base_dir / "data" / "processed" / "upc_alumnos_limpio.csv")

# Título principal
st.title("📊 Dashboard de Análisis Estudiantil - UPC")
st.markdown("Este dashboard permite explorar patrones en los datos de alumnos y visualizar el comportamiento respecto al uso del correo institucional.")

# Sidebar
st.sidebar.header("🔎 Filtros")
dominios = df['correo'].apply(lambda x: x.split('@')[-1] if isinstance(x, str) and '@' in x else 'desconocido').unique()
dominio_filtro = st.sidebar.selectbox("Filtrar por dominio de correo", options=["Todos"] + sorted(list(dominios)))

if dominio_filtro != "Todos":
    df = df[df['correo'].str.contains(dominio_filtro, na=False)]

# Estadísticas generales
col1, col2, col3 = st.columns(3)
col1.metric("Total de alumnos", f"{len(df):,}")
col2.metric("Correos institucionales", f"{df['usa_correo_institucional'].sum():,}")
col3.metric("Porcentaje uso UPC", f"{df['usa_correo_institucional'].mean() * 100:.2f}%")

st.markdown("---")

# Gráfico 1: Distribución del uso del correo institucional
st.subheader("🎓 Uso del correo institucional")
fig1, ax1 = plt.subplots()
sns.countplot(x='usa_correo_institucional', data=df, ax=ax1)
ax1.set_xticklabels(["No usa", "Sí usa"])
ax1.set_ylabel("Cantidad de alumnos")
st.pyplot(fig1)

# Gráfico 2: Longitud de nombres
st.subheader("🔠 Longitud de nombres")
df['len_nombre'] = df['nombres'].astype(str).apply(len)
fig2, ax2 = plt.subplots()
sns.histplot(df['len_nombre'], bins=20, kde=True, ax=ax2)
ax2.set_xlabel("Longitud del nombre")
st.pyplot(fig2)

# Tabla completa (preview)
st.subheader("📋 Vista previa de la tabla de alumnos")
st.dataframe(df.head(50), use_container_width=True)
