import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Simulador Mundial 2026", page_icon="🏆", layout="centered")

# --- 2. CARGA DE MODELOS EN CACHÉ ---
@st.cache_resource
def cargar_recursos():
    # Cargamos los nuevos modelos de regresión y la memoria Elo
    reg_local = joblib.load('models/xgb_reg_home.pkl')
    reg_visitante = joblib.load('models/xgb_reg_away.pkl')
    elos = joblib.load('models/ultimo_elo.pkl')
    return reg_local, reg_visitante, elos

modelo_home, modelo_away, ultimo_elo = cargar_recursos()

# --- 3. REGLAS DE NEGOCIO (MUNDIAL 2026) ---
anfitriones = ['United States', 'Mexico', 'Canada']

# Lista representativa de 48 selecciones fuertes/clasificadas
equipos_mundial = sorted([
    'Argentina', 'Brazil', 'Uruguay', 'Colombia', 'Ecuador', 'Venezuela',
    'United States', 'Mexico', 'Canada', 'Costa Rica', 'Panama', 'Jamaica',
    'Spain', 'France', 'England', 'Germany', 'Portugal', 'Italy', 'Netherlands', 
    'Croatia', 'Belgium', 'Switzerland', 'Denmark', 'Serbia', 'Austria', 'Ukraine',
    'Morocco', 'Senegal', 'Egypt', 'Algeria', 'Nigeria', 'Ivory Coast', 'Cameroon', 'Mali', 'Ghana',
    'Japan', 'Iran', 'South Korea', 'Australia', 'Saudi Arabia', 'Qatar', 'Iraq', 'Uzbekistan',
    'New Zealand', 'Peru', 'Chile', 'Wales', 'Sweden'
])

# --- 4. INTERFAZ GRÁFICA ---
st.title("🏆 Simulador Mundial 2026")
st.markdown("Algoritmo Cuantitativo de Regresión Dual + Sistema Elo")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    equipo_1 = st.selectbox("Equipo Local (Simulado):", equipos_mundial, index=equipos_mundial.index('Argentina'))

with col2:
    equipo_2 = st.selectbox("Equipo Visitante (Simulado):", equipos_mundial, index=equipos_mundial.index('Spain'))

st.write("---")

# --- 5. MOTOR DE PREDICCIÓN ---
if st.button("🔮 Simular Partido", use_container_width=True):
    if equipo_1 == equipo_2:
        st.error("Un equipo no puede jugar contra sí mismo. Elige rivales distintos.")
    else:
        # Extraer fuerza matemática
        elo_1 = ultimo_elo.get(equipo_1, 1500)
        elo_2 = ultimo_elo.get(equipo_2, 1500)
        
        # Evaluar la ventaja de la localía
        if equipo_1 in anfitriones or equipo_2 in anfitriones:
            es_neutral = 0
            st.info("🏟️ Partido con ventaja de localía (Nación Anfitriona)")
        else:
            es_neutral = 1
            st.info("✈️ Partido en cancha neutral")
            
        # Preparar la matriz predictiva
        X_nuevo = pd.DataFrame({
            'elo_home': [elo_1],
            'elo_away': [elo_2],
            'neutral_numeric': [es_neutral]
        })
        
        # Predecir Goles Esperados (Expected Goals - xG)
        xg_home = max(0, modelo_home.predict(X_nuevo)[0]) # max(0) evita goles negativos
        xg_away = max(0, modelo_away.predict(X_nuevo)[0])
        
        # Redondear para el marcador en la pantalla
        goles_home_redondeado = int(round(xg_home))
        goles_away_redondeado = int(round(xg_away))
        
       # --- 6. RENDERIZADO CON SIMULACIÓN MONTE CARLO ---
        st.subheader("Marcador Proyectado (Simulación 10k)")
        
        # Simulamos 10,000 veces
        goles_home_dist = np.random.poisson(max(0.1, xg_home), 10000)
        goles_away_dist = np.random.poisson(max(0.1, xg_away), 10000)
        
        # Crear DataFrame y contar frecuencias
        resultados = pd.DataFrame({'H': goles_home_dist, 'A': goles_away_dist})
        resultados['marcador'] = resultados['H'].astype(str) + "-" + resultados['A'].astype(str)
        
        # Calcular probabilidades y normalizar forzosamente para que sumen 1
        probs = resultados['marcador'].value_counts(normalize=True)
        probs = probs / probs.sum()  # <--- ESTA ES LA LÍNEA QUE EVITA EL ERROR
        
        # Elegir marcador
        marcador_elegido = np.random.choice(probs.index, p=probs.values)
        
        g_h, g_a = map(int, marcador_elegido.split('-'))
        
        st.markdown(f"<h1 style='text-align: center; color: white;'>{equipo_1} {g_h} - {g_a} {equipo_2}</h1>", unsafe_allow_html=True)