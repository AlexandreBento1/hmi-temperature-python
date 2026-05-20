import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA WEB ---
st.set_page_config(page_title="IHM Visual - Python", layout="wide")

# --- CABEÇALHO ---
st.title("🏭 Visão Esquemática do Sistema (IHM Digital)", anchor=False)
st.write("Use o menu lateral para alterar a temperatura e observe a reação do sistema visual.")

# --- BARRA LATERAL DE CONTROLE (Entrada) ---
# Separamos o controle da visualização para ficar organizado
with st.sidebar:
    st.header("⚙️ Painel de Controle", anchor=False)
    st.markdown("---")
    temperatura = st.slider(
        label="Simular Entrada do Sensor (°C)", 
        min_value=20.0, 
        max_value=50.0, 
        value=25.0, # Valor inicial
        step=0.5
    )

# --- LÓGICA DO PROCESSO ---
if temperatura <= 30:
    nivel_nome = "BAIXA"
    nivel_cor = "blue"
    st_dissipador = "🟢 LIGADO"
    st_refrigerador = "🔴 DESLIGADO"
    simbolo_processo = "💧" 

elif temperatura > 30 and temperatura <= 32:
    nivel_nome = "MÉDIA"
    nivel_cor = "orange"
    st_dissipador = "🔴 DESLIGADO"
    st_refrigerador = "🔴 DESLIGADO"
    simbolo_processo = "✅" 

else:
    nivel_nome = "ALTA"
    nivel_cor = "red"
    st_dissipador = "🔴 DESLIGADO"
    st_refrigerador = "🟢 LIGADO"
    simbolo_processo = "🔥" 

# --- PAINEL DE VISUALIZAÇÃO DO SISTEMA (IHM) ---

# Cartões de Métricas
st.subheader("📊 Resumo Numérico", anchor=False)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🌡️ Temperatura Atual", value=f"{temperatura:.2f} °C")
with col2:
    st.metric(label="📉 Dissipador", value=st_dissipador)
with col3:
    st.metric(label="❄️ Refrigerador", value=st_refrigerador)

st.markdown("---")

# Visão Esquemática 
st.subheader("🖥️ Visão Esquemática do Processo", anchor=False)

sch1, sch2, sch3 = st.columns([1, 2, 1])

# --- Coluna 1---
with sch1:
    st.markdown("#### Dissipador (Aquecimento)")
    if temperatura <= 30: # Ativo em baixa
        st.info("Status: Aquecendo o sistema.")

# --- Coluna 2---
with sch2:
    st.markdown(f"#### Zona do Sensor :{nivel_cor}[**{temperatura:.1f}°C**]")
    # Usamos markdown para centralizar o desenho
    st.markdown(f"""
    <div style="text-align: center; font-size: 70px;">
        {simbolo_processo}
    </div>
    <div style="text-align: center; border: 2px solid grey; border-radius: 10px; padding: 20px; background-color: #f0f2f6;">
        <b>TANQUE DE PROCESSO</b><br>
        Nível de Temperatura: <b style="color:{nivel_cor};">{nivel_nome}</b>
    </div>
    """, unsafe_allow_html=True)

# --- Coluna 3---
with sch3:
    st.markdown("#### Refrigerador (Resfriamento)")
    if temperatura > 32: # Ativo em alta
        st.info("Status: Resfriando o sistema.")
