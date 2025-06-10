import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la app
st.title("🚗 Análisis de Autos en Venta - USA")
st.markdown("Explora precios, año & más en este dashboard interactivo. Creado por Julio Tejeida")

# Cargar datos y limpiar
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna("Desconocido")
    return df

df = load_data()

# Mostrar Top 5 por precio
if st.checkbox("👑 Top 5 Precio"):
    top_5 = df.sort_values(by="price", ascending=False).head(5)
    st.dataframe(top_5)

# Histograma de precios
if st.button("📊 Histograma de precios"):
    fig = px.histogram(df, x='price', nbins=50, title='Distribución de precios de autos')
    st.plotly_chart(fig)
    st.info("🔎 **Insight:** La mayoría de los autos se venden por debajo de los $30,000 USD. Existen valores atípicos que superan los $100,000 USD.")

# Dispersión entre año y precio
if st.button("📈 Dispersión año vs precio"):
    fig2 = px.scatter(df, x='model_year', y='price', title='Precio vs Año del Modelo')
    st.plotly_chart(fig2)
    st.info("🔎 **Insight:** Los autos más recientes tienden a tener precios más altos. Algunos modelos antiguos muestran precios elevados debido a rarezas o ediciones especiales.")

# Boxplot de condición vs precio
if st.button("📦 Boxplot condición vs precio"):
    fig3 = px.box(df, x='condition', y='price', title='Precio según condición del vehículo')
    st.plotly_chart(fig3)
    st.info("🔎 **Insight:** Los vehículos en 'excellent' condición tienen mayor precio promedio. Sin embargo, hay muchos en condición 'good' con precios competitivos.")

# Distribución por tipo de combustible
if st.button("⛽ Distribución tipo de combustible"):
    fig4 = px.histogram(df, x='fuel', title='Distribución por tipo de combustible')
    st.plotly_chart(fig4)
    st.info("🔎 **Insight:** La mayoría de los autos usan gasolina. Opciones como diesel o eléctricos aún representan una minoría en el mercado.")