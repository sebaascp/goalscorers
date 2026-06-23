import pandas as pd
import plotly_express as px
import streamlit as st


st.set_page_config(page_title="Goalscorers Dashboard", layout="wide")


@st.cache_data
def load_data():
    data = pd.read_csv("goalscorers.csv")
    data["date"] = pd.to_datetime(data["date"], errors="coerce")
    data["minute"] = pd.to_numeric(data["minute"], errors="coerce")
    return data


df = load_data()

st.header("Analisis exploratorio de goleadores internacionales")

st.write(
    "Este dashboard explora un conjunto de datos historico de goles en partidos internacionales."
)

total_goals = len(df)
total_scorers = df["scorer"].nunique()
total_teams = df["team"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Goles registrados", f"{total_goals:,}")
col2.metric("Goleadores unicos", f"{total_scorers:,}")
col3.metric("Selecciones", f"{total_teams:,}")

st.subheader("Vista previa del conjunto de datos")
st.dataframe(df.head(10))

st.subheader("Distribucion de goles por minuto")

if st.button("Construir histograma"):
    fig = px.histogram(
        df.dropna(subset=["minute"]),
        x="minute",
        nbins=45,
        title="Cantidad de goles segun el minuto del partido",
        labels={"minute": "Minuto", "count": "Cantidad de goles"},
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Goleadores mas frecuentes")

top_n = st.slider("Cantidad de goleadores", min_value=5, max_value=25, value=10)
top_scorers = (
    df["scorer"]
    .value_counts()
    .head(top_n)
    .reset_index()
)
top_scorers.columns = ["scorer", "goals"]

fig_top = px.bar(
    top_scorers,
    x="goals",
    y="scorer",
    orientation="h",
    title=f"Top {top_n} goleadores",
    labels={"goals": "Goles", "scorer": "Jugador"},
)
fig_top.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig_top, use_container_width=True)
